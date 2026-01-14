from openpyxl import Workbook


def generate_excel(screen, output_path):
    wb = Workbook()
    ws = wb.active

    ws.append([
        "Category", "Sub Category", "Feature", "Title",
        "Description", "Precondition", "Steps",
        "Expected Result", "Actual Result", "Comments"
    ])

    for state in screen.states:
        for comp in state.components:
            ws.append([
                "Camera",
                "Settings",
                screen.name,
                f"Verify {comp.label}",
                f"{comp.label} in {state.name} state",
                "App launched",
                f"Open {screen.name}",
                f"{comp.label} visible",
                "",
                ""
            ])

    wb.save(output_path)
