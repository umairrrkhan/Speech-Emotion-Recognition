import librosa
import numpy as np
from keras.models import load_model

# Load your trained model
model = load_model("speech_model.h5")

# Define a function to preprocess audio
def preprocess_audio(audio_file):
    data, sr = librosa.load(audio_file, duration=3, offset=0.5)
    mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sr, n_mfcc=40).T, axis=0)
    return mfcc

# Provide the path to your recorded audio file
your_audio_file = 'Recording (2).wav'

# Preprocess the audio
preprocessed_audio = preprocess_audio(your_audio_file)

# Expand dimensions to match the model input shape
preprocessed_audio = np.expand_dims(preprocessed_audio, -1)

# Make a prediction using the model
emotion_probabilities = model.predict(np.array([preprocessed_audio]))

# Define the labels based on your training code
labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'ps', 'sad']

# Get the recognized emotion
recognized_emotion = labels[np.argmax(emotion_probabilities)]

print("Recognized Emotion:", recognized_emotion)