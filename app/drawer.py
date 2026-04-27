from PIL import ImageDraw
from PIL.Image import Image
import io

def draw_boxes(image: Image, boxes: list, img_format: str) -> bytes:
    draw = ImageDraw.Draw(image)

    for box in boxes:
        # box: [x1, y1, x2, y2]
        draw.rectangle(box, outline="red", width=3)

    output = io.BytesIO()
    image.save(output, format=img_format)
    return output.getvalue()