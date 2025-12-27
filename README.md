# Fake News Detection API

This is a beginner-friendly API that uses a pretrained BERT model to detect fake news articles.

## Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)

## Setup Instructions

Follow these steps to set up and run the API on your laptop:

### 1. Open Terminal/Command Prompt
Navigate to the project directory:
```bash
cd "c:\Users\Kalind Hirpara\Desktop\fakenews"
```

### 2. Create a Virtual Environment (Recommended)
It's best to use a virtual environment to keep dependencies organized.
```bash
# For Windows
python -m venv venv
```

### 3. Activate the Virtual Environment
```bash
# For Windows
.\venv\Scripts\activate
```

### 4. Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```
*Note: This may take a few minutes as it downloads the `torch` and `transformers` libraries.*

### 5. Run the API
You can start the server by running:
```bash
python main.py
```
Alternatively, you can use `uvicorn`:
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## How to Test

Once the server is running, open a **new** terminal (make sure to activate the virtual environment) and run the test script:
```bash
python test_api.py
```

## API Endpoints

- **GET `/`**: Welcome message.
- **POST `/predict`**: Send a JSON body with `"text"` to get a prediction.
    - Example: `{"text": "The moon is made of cheese."}`
