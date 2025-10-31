# Our mini FastAPI app place holder
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
  return {"message": " Test app deployed successfully"}
if __name__ == "__main__":
  uvicorn.run(app, host= "0.0.0.0", port=8000)
