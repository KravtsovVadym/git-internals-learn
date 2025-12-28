from pathlib import Path
import hashlib

GIT_DIR = '.ugit'

def init():
    path = Path(GIT_DIR) / 'objects'
    path.mkdir(parents=True, exist_ok=True)

def hash_object(data):
    oid = hashlib.sha1(data).hexdigest()
    obj_path = Path(GIT_DIR) / 'objects' / oid

    if not obj_path.exists():
        obj_path.write_bytes(data)

    return oid
