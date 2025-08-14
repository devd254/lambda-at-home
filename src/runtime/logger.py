import json
import aiofiles
from datetime import datetime

async def log_execution(execution_time: float, start_type: str, runner_name: str):
    log_entry = {
        "timestamp": datetime.now(datetime.timezone.utc).isoformat(),
        "execution_time": execution_time,
        "start_type": start_type,
        "runner_name": runner_name,
    }

    async with aiofiles.open("logs.txt", "a") as f:
        await f.write(json.dumps(log_entry) + "\n")