# SUML_03_Docker
# Image Classification using YOLOv5

## Description
This project is for image classification using the YOLOv5 model.  
YOLOv5 (You Only Look Once) is one of the most popular architectures for image processing. It is fast and accurate in detecting and classifying objects in images.

## Requirements
- Docker installed on your computer

## How to Run the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/RutkowskaKarolina/SUML_03_Docker
   cd SUML_03_Docker

2. Build the Docker image:
   To build the Docker image, use the following command:

   ```bash
   docker build -t yolov5s-model .

3. Run the application:
   ```bash
   docker run -p 5000:5000 yolov5s-model

4. Open the application in your browser:

  ```bash
http://localhost:5000
```

## How to Use the Application
Once the application is up and running, you can send an image for classification.

You can send a POST request to the API:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"image_url": "YOUR_IMAGE_URL"}' http://localhost:5000/predict
```

