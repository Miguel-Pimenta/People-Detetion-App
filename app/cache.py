_cache = {}

def get_cached_boxes(image_hash: str):
    return _cache.get(image_hash)

def cache_boxes(image_hash: str, boxes: list):
    _cache[image_hash] = boxes