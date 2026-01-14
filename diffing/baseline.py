
from diffing.hasher import stable_hash
def build_baseline(screen):
    return {
        'screen': stable_hash(screen.name),
        'states': {s.name: stable_hash([c.label for c in s.components]) for s in screen.states},
        'semantics': stable_hash(screen.semantics or {})
    }
