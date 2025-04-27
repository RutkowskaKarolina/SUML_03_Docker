from ultralytics import YOLO
from flask import Flask, request, jsonify, send_file
import os
import cv2

app = Flask(__name__)

model = YOLO("yolov5s.pt")

if not os.path.exists('uploads'):
    os.makedirs('uploads')


@app.route('/')
def home():
    return "Welcome to the Image Classification API! Use /predict to classify images."


# Endpoint for uploading an image and making predictions
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    results = model.predict(source=file_path)

    result_image = results[0].plot()

    result_image_path = os.path.join('uploads', 'result_' + file.filename)

    cv2.imwrite(result_image_path, result_image[:, :, ::-1])

    return send_file(result_image_path, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
