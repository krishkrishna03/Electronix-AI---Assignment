from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import os

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] for stricter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define model directory and model name
MODEL_DIR = "./model"
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

# Load model from ./model if exists, else from Hugging Face hub
if os.path.exists(MODEL_DIR):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
else:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# Create sentiment analysis pipeline
pipe = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Define input data model
class TextIn(BaseModel):
    text: str

# Define POST /predict endpoint
@app.post("/predict")
async def predict(data: TextIn):
    result = pipe(data.text)[0]
    return {"label": result['label'].lower(), "score": result['score']}
# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)