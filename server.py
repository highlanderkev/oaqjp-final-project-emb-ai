"""
Main server file to run server logic.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Emotion Detector Route Handler for handling main emotion detection input logic.
    """
    text_to_analyze = str(request.args.get("textToAnalyze"))
    response = emotion_detector(text_to_analyze)
    if response is None or response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, \
    the system response is 'anger': {response['anger']}, \
    'disgust': {response['disgust']}, \
    'fear': {response['fear']}, \
    'joy': {response['joy']} and \
    'sadness': {response['sadness']}. \
    The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """
    Render index page route handler to render index.html.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
