import asyncio
import time
from python_on_whales import DockerClient

from infra import runner

from typing import Union

async def start_runner(runner_id: int) -> Union[DockerClient, None]:
    print(f"Cold starting runner {runner_id}")
    # Simulate cold start delay
    await asyncio.sleep(10)
    return runner.create_runner(runner_id)