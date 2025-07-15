from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import os
import strawberry
from strawberry.fastapi import GraphQLRouter
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_DIR = "./model"
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

def load_pipeline():
    global pipe
    if os.path.exists(MODEL_DIR):
        tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
    else:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    pipe = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

load_pipeline()

# Watchdog handler
class ModelReloadHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        print("Detected change in model directory. Reloading...")
        load_pipeline()

def start_watcher():
    observer = Observer()
    event_handler = ModelReloadHandler()
    observer.schedule(event_handler, path=MODEL_DIR, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

watcher_thread = threading.Thread(target=start_watcher, daemon=True)
watcher_thread.start()

@strawberry.type
class Prediction:
    label: str
    score: float

@strawberry.type
class Query:
    @strawberry.field
    def predict(self, text: str) -> Prediction:
        result = pipe(text)[0]
        return Prediction(label=result["label"].lower(), score=result["score"])

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
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
    