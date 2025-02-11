# NLPApp Documentation

## Overview

NLPApp is a desktop application designed to perform Natural Language Processing (NLP) tasks such as Sentiment Analysis, Named Entity Recognition (NER), and Emotion Analysis. The application is built using Python and Tkinter for the GUI, and it integrates with external APIs like Hugging Face for advanced NLP functionalities.

---

## File Structure

- **`app.py`:** The main application script that handles the GUI and integrates all functionalities.
- **`classifier.py`:** Contains helper methods for classifying and interpreting NLP results.
- **`myapi.py`:** Handles API requests to external services (e.g., Hugging Face) for NLP tasks.
- **`mydb_code.py`:** Manages user authentication and data storage using a local JSON file.
- **`requirements.txt`:** Lists all dependencies required to run the application.
- **`.env`:** Stores environment variables like API keys (not included in the repository).
- **`README.md`:** Provides an overview of the project, installation instructions, and usage guidelines.

---

## How It Works

1. **User Authentication:**
   - Users can register or log in using their email and password. The data is stored in a local JSON file (`mydb.json`).

2. **Sentiment Analysis:**
   - The application uses the `TextBlob` library to analyze the sentiment of the input text and classify it as positive, negative, or neutral.

3. **Named Entity Recognition (NER):**
   - The application sends the input text to a Hugging Face model to identify and classify entities (e.g., names, locations, organizations).

4. **Emotion Analysis:**
   - The application uses a Hugging Face model to detect the emotional tone of the input text (e.g., joy, anger, sadness).

---

## API Integration

The application integrates with the Hugging Face API for NER and Emotion Analysis. To use this feature, you need to:

1. Obtain a Hugging Face API key.
2. Store the API key in a `.env` file as follows:
