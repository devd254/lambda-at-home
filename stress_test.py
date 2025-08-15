import asyncio
import httpx
import subprocess
import time
import sys
import json
from src.events.image_update import ImageUpdateEvent
from src.events.memo_update import MemoUpdateEvent

API_URL = "http://localhost:8000"
IMAGE_ENDPOINT = f"{API_URL}/dispatch/image"
MEMO_ENDPOINT = f"{API_URL}/dispatch/memo"
LOGS_ENDPOINT = f"{API_URL}/logs"


async def send_request(client, endpoint, data):
    try:
        response = await client.post(endpoint, data=data)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as e:
        print(f"An error occurred while requesting {e.request.url!r}.")
        return None


async def main(num_requests: int):
    print("Starting API...")
    api_process = subprocess.Popen([sys.executable, "start_api.py"])
    # Give the API time to start
    time.sleep(5)
    print("API started.")

    async with httpx.AsyncClient() as client:
        tasks = []
        for i in range(num_requests):
            image_data = ImageUpdateEvent(bucket=f"bucket_{i}", key=f"key_{i}")
            memo_data = MemoUpdateEvent(user_id=i, memo=f"memo_{i}")
            tasks.append(
                send_request(
                    client, IMAGE_ENDPOINT, image_data.model_dump_json()
                )
            )
            tasks.append(
                send_request(client, MEMO_ENDPOINT, memo_data.model_dump_json())
            )

        results = await asyncio.gather(*tasks)
        print(f"Sent {len(results)} requests.")

    print("Stopping API...")
    api_process.terminate()
    api_process.wait()
    print("API stopped.")

    print("\n--- Logs ---")
    try:
        with open("logs.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No logs found.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Stress test the API.")
    parser.add_argument("-n", "--num-requests", type=int, default=10, help="Number of requests to send to each endpoint.")
    args = parser.parse_args()

    asyncio.run(main(args.num_requests))