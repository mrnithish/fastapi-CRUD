
from fastapi import FastAPI, UploadFile, File
import pandas as pd

app = FastAPI()

@app.post("/data/upload")
async def upload_data(file: UploadFile = File(...)):
    data = pd.read_csv(file.file)
    # Process data
    return {"message": "Data uploaded successfully"}

# main.py
from fastapi import FastAPI
from data_upload import upload_data

app = FastAPI()
app.include_router(upload_data.router)
