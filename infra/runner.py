from python_on_whales import docker, DockerClient

def create_runner(runner_id: int):
    try:
        return docker.run(
            "lambda-at-home",
            detach=True,
            name=f"runner_{runner_id}",
            remove=True,
        )
    except Exception as e:
        print(f"Error creating runner: {e}")
        return None

def get_active_runners():
    return docker.ps(filters={"name": "runner_"})

def get_all_runners():
    return docker.ps(all=True, filters={"name": "runner_"})

def stop_runner(runner: DockerClient):
    runner.stop()

def stop_all_runners():
    for container in get_all_runners():
        container.stop()