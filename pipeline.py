
import os,json
from ingest.screenshot_loader import load_screenshots
from uim.builder import build_screen
from uim.semantic_enricher import enrich
from diffing.baseline import build_baseline
from diffing.diff import has_changes
from testgen.gherkin import generate as gen_gherkin
from testgen.excel import generate as gen_excel

os.makedirs('output',exist_ok=True)
os.makedirs('baseline',exist_ok=True)

screens=load_screenshots('screenshots')
for name,imgs in screens.items():
    screen=enrich(build_screen(name,imgs))
    new_base=build_baseline(screen)
    base_path=f'baseline/{name}.json'
    if os.path.exists(base_path):
        old=json.load(open(base_path))
        if not has_changes(old,new_base):
            print('[SKIP]',name); continue
    open(f'output/{name}.feature','w').write(gen_gherkin(screen))
    gen_excel(screen,f'output/{name}.xlsx')
    json.dump(new_base,open(base_path,'w'),indent=2)
    print('[UPDATED]',name)
