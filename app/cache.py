import hashlib

_cache = {}

def get_image_hash(image_bytes: bytes) -> str:
    return hashlib.sha256(image_bytes).hexdigest()

def get_cached_boxes(image_hash: str) -> list | None:
    return _cache.get(image_hash)

def cache_boxes(image_hash: str, boxes: list) -> None:
    _cache[image_hash] = boxes