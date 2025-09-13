# Emotion Detector from Text

def detect_emotion(sentence):
    # Predefined keywords mapped to emotions
    emotion_dict = {
        "happy": "Joy 😊",
        "joy": "Joy 😊",
        "smile": "Joy 😊",
        "sad": "Sadness 😔",
        "cry": "Sadness 😢",
        "tears": "Sadness 😢",
        "angry": "Anger 😡",
        "mad": "Anger 😡",
        "upset": "Anger 😡",
        "fear": "Fear 😨",
        "scared": "Fear 😰",
        "afraid": "Fear 😱"
    }

    # Convert input to lowercase words
    words = sentence.lower().split()

    # Count matched emotions
    detected = {}

    for word in words:
        if word in emotion_dict:
            emotion = emotion_dict[word]
            detected[emotion] = detected.get(emotion, 0) + 1

    # If any emotions detected, show the one with highest count
    if detected:
        result = max(detected, key=detected.get)
        print(f"Detected Emotion: {result}")
    else:
        print("No clear emotion detected 🤔")


def start_detector():
    print("Welcome to Emotion Detector! (type 'exit' to quit)\n")

    while True:
        sentence = input("Enter a sentence: ").strip()

        if sentence.lower() == "exit":
            print("Goodbye! 👋")
            break

        detect_emotion(sentence)


# Run program
start_detector()