
import json,hashlib
def stable_hash(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True).encode()).hexdigest()
