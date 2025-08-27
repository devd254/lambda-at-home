# lambda-at-home
"We Have Lambda at Home". I'm gonna recreate a simple mini "AWS Lambda" locally to figure it out. I wanted to balance learning with practicing using AI tooling. For this project, I wanted to write all code using Gemini CLI. I did this by:
   1. Using ChatGPT as a guide to help me learn and design the project.
   2. Creating the necessary directories and files
   3. Left comments on each file that were specific enough, but left some ambiguity to see limitations on Gemini CLI
   4. Let Gemini CLI get to work, debugging as necessary (ideally through prompts)

## About
Replicate AWS Lambda
    - FastAPI server to handle events
    - Standardized events
    - Custom lambda function handlers
    - Docker containers to simulate elasticity (serverless infrastructure)


### Standardized Events
1. IMAGE_UPDATE
    - This simulates an image being changed in an S3 bucket.
2. MEMO_CREATE
    - This simulates a new memo being created.

### Handlers
This is a user designed lambda function. For now, there is one handler for each standardized event. For simplicity, handlers are hard-coded rather than passed to the Dispatcher via HTTP requests. 
> For example, when an image is updated, the image must be processed and update data in a database.
```
<user_defined_prefix>_handler(event):
    # user-defined handling here
```

### Infrastructure
Docker containers are will simulate the underlying infrastructure.
> Cold start: brand new container is spun up (additional 5 seconds)
> Warm start: existing container is used (no additional time)