# Define a Pydantic model for the JSON request body
from pydantic import BaseModel

class TextModel(BaseModel):
    text: str
# Create a FastAPI endpoint to accept a POST request with a JSON body
# The JSON body should contain a single field called "text"
# The endpoint should return a checksum of the text

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()

class TextModel(BaseModel):
    text: str
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()

class TextModel(BaseModel):
    text: str

@app.post("/generate")
async def generate(data: TextModel):
    """
    Endpoint to generate a checksum for the provided text.

    - **text**: A string field in the JSON body to be hashed.

    Returns a JSON object with the checksum of the provided text.
    """
    text = data.text
    checksum = hashlib.md5(text.encode()).hexdigest()
    return {"checksum": checksum}

@app.get("/")
def read_root():
    """
    Welcome endpoint that provides a custom message.

    Returns a welcome message.
    """
    return {"message": "Welcome to the FastAPI application! This is [Roxette]'s API."}

@app.post("/generate")
async def generate(data: TextModel):
    text = data.text
    checksum = hashlib.md5(text.encode()).hexdigest()
    return {"checksum": checksum}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()

class TextModel(BaseModel):
    text: str

@app.post("/generate")
async def generate(data: TextModel):
    """
    Endpoint to generate a checksum for the provided text.

    - **text**: A string field in the JSON body to be hashed.

    Returns a JSON object with the checksum of the provided text.
    """
    text = data.text
    checksum = hashlib.md5(text.encode()).hexdigest()
    return {"checksum": checksum}

@app.get("/")
def read_root():
    """
    Welcome endpoint that provides a custom message.

    Returns a welcome message.
    """
    return {"message": "Welcome to the FastAPI application! This is [Your Name]'s API."}

from fastapi.testclient import TestClient

client = TestClient(app)

def test_generate():
    response = client.post("/generate", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json() == {"checksum": "5d41402abc4b2a76b9719d911017c592"}

def test_generate_empty_text():
    response = client.post("/generate", json={"text": ""})
    assert response.status_code == 200
    assert response.json() == {"checksum": "d41d8cd98f00b204e9800998ecf8427e"}
