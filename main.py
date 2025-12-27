from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Fake News Detection API",
    description="A beginner-friendly API to detect fake news using a pretrained BERT model.",
    version="1.0.0"
)

# Model configuration
# We use a lightweight BERT model: mrm8488/bert-tiny-finetuned-fake-news-detection
MODEL_NAME = "mrm8488/bert-tiny-finetuned-fake-news-detection"

print("Loading model... This might take a moment.")
try:
    classifier = pipeline("text-classification", model=MODEL_NAME)
    print("Model loaded successfully!")
    print(f"Model Labels: {classifier.model.config.id2label}")
except Exception as e:
    print(f"Error loading model: {e}")
    classifier = None

# Define request schema
class NewsArticle(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fake News Detection API. Use the /predict endpoint to classify news articles."}

@app.post("/predict")
async def predict_news(article: NewsArticle):
    if not classifier:
        raise HTTPException(status_code=503, detail="Model not loaded. Please check server logs.")
    
    if not article.text.strip():
        raise HTTPException(status_code=400, detail="Article text cannot be empty.")

    try:
        # Get prediction from the pipeline
        results = classifier(article.text)
        
        # Label mapping for this specific model
        # LABEL_0 -> FAKE, LABEL_1 -> REAL
        label_map = {
            "LABEL_0": "FAKE",
            "LABEL_1": "REAL"
        }
        
        prediction = results[0]
        label = prediction['label']
        confidence = prediction['score']
        
        friendly_label = label_map.get(label, label)

        return {
            "text_snippet": article.text[:100] + "..." if len(article.text) > 100 else article.text,
            "prediction": friendly_label,
            "confidence": round(confidence, 4)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
