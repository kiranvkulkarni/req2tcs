import json
import hashlib


def stable_hash(obj) -> str:
    """
    Deterministic, order-independent hash.
    """
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, ensure_ascii=True).encode("utf-8")
    ).hexdigest()
