from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import methods

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://50.116.38.143:3000",
        "http://50.116.38.143"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/download/")
def download(video: methods.Video):
    return methods.download_video(video)