import asyncio
import cloudpickle
import base64
from typing import Callable, Any
from python_on_whales import DockerClient

from src.runtime.logger import log_execution

async def execute_handler(runner: DockerClient, handler: Callable, event: Any):
    handler_pkl = base64.b64encode(cloudpickle.dumps(handler)).decode('utf-8')
    event_pkl = base64.b64encode(cloudpickle.dumps(event)).decode('utf-8')

    cmd = f"python -c 'import cloudpickle, base64; handler = cloudpickle.loads(base64.b64decode(\"{handler_pkl}\")); event = cloudpickle.loads(base64.b64decode(\"{event_pkl}\"));handler(event)'"                                                                                                                                                                       

    start_time = asyncio.get_event_loop().time()
    exec_result = runner.execute(cmd, stream=True)
    end_time = asyncio.get_event_loop().time()

    execution_time = end_time - start_time
    start_type = "warm" if execution_time < 10 else "cold"

    await log_execution(execution_time, start_type, runner.name)

    for stream_type, content in exec_result:
        if stream_type == 'stdout':
            print(content.decode('utf-8'))
        else:
            print(f"Error: {content.decode('utf-8')}")