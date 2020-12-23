from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def read_home():
    return {"ok": "home"}

@app.get("/health")
async def read_health():
    return {"ok": "health"}
