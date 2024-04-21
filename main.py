from fastapi import FastAPI

# https://fastapi.tiangolo.com/tutorial/first-steps/
app = FastAPI()

# Swagger: http://127.0.0.1:8000/docs
# Doc: http://127.0.0.1:8000/redoc
# Schema: http://127.0.0.1:8000/openapi.json

"""
curl http://127.0.0.1:8000
"""
@app.get("/")
async def root():
    return {"message": "Hello World"}