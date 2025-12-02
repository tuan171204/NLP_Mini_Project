from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="wonrax/phobert-base-vietnamese-sentiment")

def analyze_sentiment(text):
    text = text[:512] 
    
    result = classifier(text)[0]
    label = result['label']
    score = result['score']

    standard_label = "UNKNOWN"
    if label == 'POS':
        standard_label = "POSITIVE (Tích cực)"
    elif label == 'NEG':
        standard_label = "NEGATIVE (Tiêu cực)"
    elif label == 'NEU':
        standard_label = "NEUTRAL (Trung tính)"

    return label, standard_label, score