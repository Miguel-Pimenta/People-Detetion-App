import io

from PIL import Image
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import Response
from app.detector import detect_people
from app.cache import get_image_hash, get_cached_boxes, cache_boxes
from app.drawer import draw_boxes

app = FastAPI()

@app.post("/detect")
async def detect(file: UploadFile):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Only JPEG and PNG images are supported")

    image_bytes = await file.read()
    image_hash = get_image_hash(image_bytes)
    image = Image.open(io.BytesIO(image_bytes))

    # Check if image is already stored in cache
    boxes = get_cached_boxes(image_hash)

    if boxes is None:
        boxes = detect_people(image)
        cache_boxes(image_hash, boxes)

    img_format = file.content_type.split("/")[1].upper()
    result = draw_boxes(image, boxes, img_format)
    return Response(content=result, media_type=file.content_type)