
import os
from uim.models import Screen, ScreenState, Component
from vision.ocr import extract_text
def build_screen(name, images):
    states=[]
    for img in images:
        state=os.path.basename(img).replace('.png','')
        comps=[Component(label=t,state=state) for t in extract_text(img) if 'HDR' in t]
        states.append(ScreenState(state, comps))
    return Screen(name, states, {})
