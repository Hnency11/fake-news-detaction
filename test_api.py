import requests
import json

URL = "http://127.0.0.1:8000/predict"

test_articles = [
    {
        "text": "The earth revolves around the sun."
    },
    {
        "text": "Hillary Clinton has been arrested by the military and is being held at Guantanamo Bay."
    }
]

def test_api():
    print("Testing Fake News Detection API...")
    for article in test_articles:
        try:
            response = requests.post(URL, json=article)
            if response.status_code == 200:
                print(f"\nArticle: {article['text'][:50]}...")
                print(f"Result: {json.dumps(response.json(), indent=2)}")
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Failed to connect: {e}")

if __name__ == "__main__":
    test_api()
