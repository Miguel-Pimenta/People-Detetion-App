from PIL import ImageDraw
import io


def draw_boxes(image, boxes):
    draw = ImageDraw.Draw(image)

    for box in boxes:
        x1, y1, x2, y2 = box
        draw.rectangle([x1, y1, x2, y2], outline="red", width=3)

    output = io.BytesIO()
    image.save(output, format="JPEG")
    return output.getvalue()