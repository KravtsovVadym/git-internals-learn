from pathlib import Path
import hashlib

GIT_DIR = '.ugit'

def init():
    path = Path(GIT_DIR) / 'objects'
    path.mkdir(parents=True, exist_ok=True)

def hash_object(data, type_='blob'):
    obj = type_.encode() + b'\x00' + data
    oid = hashlib.sha1(obj).hexdigest()
    obj_path = Path(GIT_DIR) / 'objects' / oid

    if not obj_path.exists():
        obj_path.write_bytes(obj)

    return oid

def get_object(oid, expected='blob'):
    obj_path = Path(GIT_DIR) / 'objects' / oid

    if not obj_path.exists():
        return "file not found"
    obj = obj_path.read_bytes()

    type_, _, content = obj.partition(b'\x00')

    if expected is not None:
        assert type_ == expected,  f'Expected {expected} got {type_}'

    return content
