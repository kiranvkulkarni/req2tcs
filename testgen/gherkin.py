
def generate(screen):
    lines=[f'Feature: {screen.name}']
    for s in screen.states:
        for c in s.components:
            lines+=['',f'Scenario: Verify {c.label} in {s.name}',
                    '  Given App is launched',
                    f'  When User opens {screen.name}',
                    f'  Then {c.label} should be visible']
    for n in (screen.semantics or {}).get('negative_conditions',[]):
        lines+=['',f"Scenario: {n['component']} when {n['condition']}",
                '  Given App is launched',
                f'  When User opens {screen.name}',
                f"  Then {n['component']} should be {n['expected_behavior']}"]
    return '\n'.join(lines)
