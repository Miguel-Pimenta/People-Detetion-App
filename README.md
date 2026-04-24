# People Detection Service

A REST API that detects people in images and returns the image with bounding boxes drawn around each detected person.

## How it works

1. User uploads an image to the `/detect` endpoint
2. The service runs people detection using YOLOv8
3. Red bounding boxes are drawn around each detected person
4. The modified image is returned

To avoid running the detection algorithm multiple times for the same image, the service caches the results in memory using a hash of the image as the key. If the same image is uploaded again, the cached results are used instead.

Uploaded images are never stored on disk — they are processed in memory and discarded after the request is complete.

## Tech Stack

- Python
- FastAPI
- YOLOv8 (Ultralytics)
- Pillow

## Running the service

### With Docker (recommended)

```bash
docker build -t people-detection .
docker run -p 8000:8000 people-detection
```

## API

### POST /detect
Upload an image and receive it back with bounding boxes drawn around detected people.

- **Content-Type:** multipart/form-data
- **Field:** `file` (JPEG or PNG image)

You can test the API interactively at `http://localhost:8000/docs` after starting the service.

## Future improvements

- Replace in-memory cache with Redis for persistence across restarts
- Support additional image formats