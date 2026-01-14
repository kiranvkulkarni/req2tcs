def diff_baseline(old, new):
    return {
        "screen_changed": old["screen_hash"] != new["screen_hash"],
        "state_changes": {
            s for s in new["state_hashes"]
            if s not in old["state_hashes"]
            or old["state_hashes"][s] != new["state_hashes"][s]
        },
        "component_changes": {
            c for c in new["component_hashes"]
            if c not in old["component_hashes"]
            or old["component_hashes"][c] != new["component_hashes"][c]
        },
        "semantic_changed": old["semantic_hash"] != new["semantic_hash"]
    }
