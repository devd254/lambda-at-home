import asyncio
from collections import deque
from typing import Dict, Any, Callable, Union
from python_on_whales import DockerClient

from src.runtime import execute, start
from infra import runner

MAX_RUNNERS = 6
IDLE_TIME = 10 

class Scheduler:
    def __init__(self):
        self.runners: Dict[int, DockerClient] = {}
        self.idle_runners: Dict[int, asyncio.Task] = {}
        self.request_queue = deque()
        self.next_runner_id = 0

    async def schedule_event(self, handler: Callable, event: Any):
        self.request_queue.append((handler, event))
        asyncio.create_task(self._process_queue())

    async def _process_queue(self):
        if not self.request_queue:
            return

        handler, event = self.request_queue.popleft()
        selected_runner = await self._find_available_runner()

        if selected_runner:
            await self._execute_handler_in_runner(selected_runner, handler, event)
        else:
            self.request_queue.appendleft((handler, event))

    async def _find_available_runner(self) -> Union[DockerClient, None]:
        if self.idle_runners:
            runner_id, idle_task = self.idle_runners.popitem()
            idle_task.cancel()
            return self.runners[runner_id]

        if len(self.runners) < MAX_RUNNERS:
            new_runner = await start.start_runner(self.next_runner_id)
            if new_runner:
                self.runners[self.next_runner_id] = new_runner
                self.next_runner_id += 1
                return new_runner

        return None

    async def _execute_handler_in_runner(self, selected_runner: DockerClient, handler: Callable, event: Any):
        await execute.execute_handler(selected_runner, handler, event)
        self._release_runner(selected_runner)

    def _release_runner(self, selected_runner: DockerClient):
        runner_id = int(selected_runner.name.split("_")[1])
        idle_task = asyncio.create_task(self._idle_timeout(runner_id))
        self.idle_runners[runner_id] = idle_task

    async def _idle_timeout(self, runner_id: int):
        await asyncio.sleep(IDLE_TIME)
        if runner_id in self.idle_runners:
            del self.idle_runners[runner_id]
            runner.stop_runner(self.runners[runner_id])
            del self.runners[runner_id]

scheduler = Scheduler()