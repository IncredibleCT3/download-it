from fastapi import FastAPI
import methods

app = FastAPI()

@app.get("/download/{url}")
def download(url: str):
    return methods.download(url)