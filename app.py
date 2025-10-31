# Our mini FastAPI app place holder
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  return {"message": " Test app deployed successfully"}

