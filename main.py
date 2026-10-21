from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/logo.png")
def get_logo():
    return FileResponse("logo.png")

@app.get("/health")
def health():
    return {"status": "ok", "app": "PAGO AI"}
