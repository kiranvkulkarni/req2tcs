import os
import json

from ingest.screenshot_loader import load_screenshots
from uim.builder import build_screen
from uim.semantic_enricher import enrich_screen
from diffing.baseline import build_baseline
from diffing.diff import diff_baseline
from testgen.gherkin import generate_gherkin
from testgen.excel import generate_excel

os.makedirs("baseline", exist_ok=True)
os.makedirs("output", exist_ok=True)

screens = load_screenshots("screenshots")

for screen_name, images in screens.items():
    screen = build_screen(screen_name, images)
    screen = enrich_screen(screen)

    new_baseline = build_baseline(screen)
    baseline_path = os.path.join("baseline", f"{screen_name}.json")

    if os.path.exists(baseline_path):
        old_baseline = json.load(open(baseline_path))
        changes = diff_baseline(old_baseline, new_baseline)

        if not any(changes.values()):
            print(f"[SKIP] {screen_name} unchanged")
            continue

    with open(f"output/{screen_name}.feature", "w") as f:
        f.write(generate_gherkin(screen))

    generate_excel(screen, f"output/{screen_name}.xlsx")

    json.dump(new_baseline, open(baseline_path, "w"), indent=2)
    print(f"[UPDATED] {screen_name}")
