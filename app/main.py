import hashlib
import io

from PIL import Image
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import Response
from app.detector import detect_people
from app.cache import get_cached_boxes, cache_boxes
from app.drawer import draw_boxes

app = FastAPI()

def get_image_hash(image_bytes):
    return hashlib.sha256(image_bytes).hexdigest()

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Only JPEG and PNG images are supported")

    image_bytes = await file.read()
    image_hash = get_image_hash(image_bytes)
    image = Image.open(io.BytesIO(image_bytes))

    #Check if image is already stored in cache
    boxes = get_cached_boxes(image_hash)

    if boxes is None:
        boxes = detect_people(image)
        cache_boxes(image_hash, boxes)

    result = draw_boxes(image, boxes)
    return Response(content=result, media_type="image/jpeg")