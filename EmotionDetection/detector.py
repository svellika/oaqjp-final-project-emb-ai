import requests
import json

def emotion_detector(text_to_analyze):

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)

    # Handle blank input / 400 error
    if response.status_code == 400:
        return {
            "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None,
            "dominant_emotion": None
        }

    response_text = response.text
    data = json.loads(response_text)
    emotions = data['emotionPredictions'][0]['emotion']

    highest_score = 0
    dominant_emotion = ""

    # Loop through each emotion and its score
    for emotion, score in emotions.items():
        if score > highest_score:
            highest_score = score
            dominant_emotion = emotion
    
    emotions['dominant_emotion'] = dominant_emotion

    return emotions    

if __name__ == "__main__":
    text = "I am so happy I'm doing this."
    output = emotion_detector(text)
    print(output)