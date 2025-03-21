from transformers import pipeline

# Load a sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return result[0]['label'], result[0]['score']

if __name__ == "__main__":
    feedback = input("Enter customer feedback: ")
    label, score = analyze_sentiment(feedback)
    print(f"Sentiment: {label}, Confidence: {score:.2f}")