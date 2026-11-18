from hashlib import sha256
import secrets

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()


class TextRequest(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
def welcome():
    return """
    <html>
        <body>
            <h1>Welcome to the Token Generator API</h1>
            <h2>Immanuel M Shiratibavi</h2>
        </body>
    </html>
    """


def generate():
    return secrets.token_hex(16)


@app.get("/generate")
def generate_token():
    return {"token": generate()}


@app.post(
    "/checksum",
    summary="Generate checksum",
    description="Accept text and return SHA256 checksum"
)
def checksum(request: TextRequest):
    checksum_value = sha256(
        request.text.encode()
    ).hexdigest()

    return {
        "text": request.text,
        "checksum": checksum_value,
        "token": generate()
    }