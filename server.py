from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import getUpdateUrl

origins = [
  "http://localhost:3000", 
  "https://ps3-update-tool.vercel.app"
]

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins= origins,
  allow_credentials=False,
  allow_methods=["GET"],
  allow_headers=["*"],
)

@app.get('/')
def main(serial: str):
  updates = getUpdateUrl.main(serial)

  if type(updates) == dict and updates["error"]:
    raise HTTPException(status_code=404, detail="not found")
  
  if not updates:
    print('No update avaliable')
  
  return updates
