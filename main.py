import uvicorn
import os
from fastapi import FastAPI, UploadFile
from storage import S3
from dotenv import load_dotenv
from typing import List
from helpers import get_uuid
from convertors.convert import convert

load_dotenv()

AWS_ACCESS_KEY_ID = os.environ.get('aws_access_key_id')
AWS_SECRET_ACCESS_KEY = os.environ.get('aws_secret_access_key')
AWS_REGION = os.environ.get('region')

app = FastAPI()

s3 = S3(
  aws_access_key_id=AWS_ACCESS_KEY_ID,
  aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
  region_name=AWS_REGION)

local_store = './.store/'


@app.post("/upload_manuscript/")
async def upload_manuscript(file: UploadFile):

    input_path = local_store + file.filename
    os.makedirs(os.path.dirname(input_path), exist_ok=True)
    with open(input_path, 'wb') as f:
        f.write(file.file.read())
        f.close()

    file_txt = convert(input_path)

    s_id = get_uuid()

    s3.store_file(file_txt, s_id + ".txt")
    # s3.store_file(file_html, s_id + ".html")
    # s3.store_file(file.file, s_id + "." + extension)

    return {
      "s_id": s_id,
      "title": "zzzz",
      "genre": "fdsfds",
      "tagline": "mmmvvvmm"
      }


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    for file in files:
        s3.store_file(file)
    return {"filenames": [file.filename for file in files]}


@app.get("/")
def root():
    s3.list_buckets()
    return {"message": "Hello World1"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
