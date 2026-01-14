from diffing.hasher import stable_hash


def build_baseline(screen):
    screen_fingerprint = {
        "state_count": len(screen.states),
        "components": sorted(
            {c.label for s in screen.states for c in s.components}
        )
    }

    state_hashes = {
        s.name: stable_hash(
            sorted(c.label for c in s.components)
        )
        for s in screen.states
    }

    component_states = {}
    for s in screen.states:
        for c in s.components:
            component_states.setdefault(c.label, set()).add(s.name)

    component_hashes = {
        label: stable_hash(
            {"label": label, "states": sorted(states)}
        )
        for label, states in component_states.items()
    }

    semantic_fingerprint = {
        "mandatory_components": sorted(
            screen.semantics.get("mandatory_components", [])
        ),
        "negative_conditions": sorted(
            (
                n["component"],
                n["condition"],
                n["expected_behavior"]
            )
            for n in screen.semantics.get("negative_conditions", [])
        )
    }

    return {
        "screen_hash": stable_hash(screen_fingerprint),
        "state_hashes": state_hashes,
        "component_hashes": component_hashes,
        "semantic_hash": stable_hash(semantic_fingerprint)
    }
