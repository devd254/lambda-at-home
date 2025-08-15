import sys
import os
import uvicorn

# Add the project root directory to the Python path to resolve the imports correctly.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

if __name__ == "__main__":
    # Run the FastAPI app using uvicorn, pointing to the app instance in src/main.py
    uvicorn.run("src.main:app", host="localhost", port=8000, reload=True)
