from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import methods

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/download/")
def download(video: methods.Video):
    return methods.download_video(video)