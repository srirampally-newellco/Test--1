# Our mini FastAPI app place holder
from fastapi import Fatsapi
app = Fastapi()

@app.get("/")
def read_root():
  return {"message": " Test app deployed successfully}
