"""

Main app file that contains routings and main methods

"""

from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from config import ORIGINS
from .cipher import encode, decode



# FastApi init
app = FastAPI(
    title = "Cipher Api",
    description = "Caesar cipher api",
    version = "1.0.0"
)

origins = ORIGINS

# Tags for Swagger docs
tags_metadata = [
    {
        "name": "Encode",
        "description": "Method for encoding data",
    },
    {
        "name": "Decode",
        "description": "Method for decoding data",
    },
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# Encode endpoint - takes str(phrase) and int(shift) and runs it through encode method
@app.get("/encode/msg={phrase}&shift={shift}", tags=["Encode"])
async def Encode(phrase: str, shift: int):
    return {"message": encode(phrase, abs(shift))}

# Decode endpoint - takes str(phrase) and int(shift) and runs it through decode method
@app.get("/decode/msg={phrase}&shift={shift}", tags=['Decode'])
async def Decode(phrase: str, shift: int):
    return {"message" : decode(phrase, -abs(shift))}



