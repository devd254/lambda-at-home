# Fast API server that will be ran with uvicorn

# endpoint1: dispatch
#   requests will be in the Pydantic format stored in /src/events
#   Check the registry to see which handler maps to which event
#   schedule found handler

# endpoint2: logs
#   get request with no params, return all logs stored in logs.txt as json