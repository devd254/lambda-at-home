# store dictionary of active environments (docker containers)

# only 6 (N) containers can exist at a time

# environments can sit idle for 10 seconds after execution finishes

# when requests come in and there's already 6 active (non-idle) environments, build a fifo queue with deque

# use start.py to find the correct runner to execute on.

# pass that runner into execute.py