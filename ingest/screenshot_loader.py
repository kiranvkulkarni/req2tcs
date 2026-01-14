
import os
def load_screenshots(base):
    return {d:[os.path.join(base,d,f) for f in os.listdir(os.path.join(base,d)) if f.endswith('.png')]
            for d in os.listdir(base)}
