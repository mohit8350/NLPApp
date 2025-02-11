import requests
from textblob import TextBlob
from classifier import classifiers as clf

# making API class where we'll create different methods for analysing text
class API:

    def __init__(self):
        
        self.api_key = None # api key for hugging face

        # creating a object of classifiers class and by that object we can call any method of classifiers class
        self.clfo = clf()

    def analyze_sentiment(self, text):
        self.blob = TextBlob(text)
        """Analyze and classify sentiment of the text."""
        polarity_score = self.blob.sentiment.polarity
        polarity_label = self.clfo.classify_polarity(polarity_score)

        return {
            "Polarity Score": polarity_score,
            "Polarity Label": polarity_label,
        }

    def perform_NER(self, text):
        
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }

        # Send the request to Hugging Face API (NER model)
        response = requests.post(
            'https://api-inference.huggingface.co/models/dbmdz/bert-large-cased-finetuned-conll03-english',
            headers=headers,
            json={"inputs": text}
        )

        return response.json()

    def get_label_full_name(self, label):
        return self.clfo.ner_labels_full_names.get(label, "Unknown Label")

    def analyze_emotion(self, text):
        """Send text for emotion analysis via API and generate a sentence based on emotion."""
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }

        # Send the request to Hugging Face API for emotion detection
        response = requests.post(
            "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base",
            headers=headers,
            json={"inputs": text}
        )

        if response.status_code == 200:
            result = response.json()

            if isinstance(result, list) and len(result) > 0:
                # Sort emotions by score in descending order
                sorted_emotions = sorted(result[0], key=lambda x: x['score'], reverse=True)
                
                # Generate the sentence based on the sorted emotions
                final_response =  self.clfo.generate_emotion_sentence(sorted_emotions)
            else:
                final_response =  "No emotion detected or wrong response format."
        else:
            final_response =  f"Error {response.status_code}: {response.text}"
        
        return final_response
