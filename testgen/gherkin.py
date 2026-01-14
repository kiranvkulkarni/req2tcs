def generate_gherkin(screen):
    lines = [f"Feature: {screen.name}"]

    for state in screen.states:
        for comp in state.components:
            lines.extend([
                "",
                f"Scenario: Verify {comp.label} in {state.name}",
                "  Given App is launched",
                f"  When User opens {screen.name}",
                f"  Then {comp.label} should be visible"
            ])

    for neg in screen.semantics.get("negative_conditions", []):
        lines.extend([
            "",
            f"Scenario: {neg['component']} when {neg['condition']}",
            "  Given App is launched",
            f"  When User opens {screen.name}",
            f"  Then {neg['component']} should be {neg['expected_behavior']}"
        ])

    return "\n".join(lines)
