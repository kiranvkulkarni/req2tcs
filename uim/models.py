
from dataclasses import dataclass
from typing import List, Dict
@dataclass
class Component:
    label: str
    state: str
@dataclass
class ScreenState:
    name: str
    components: List[Component]
@dataclass
class Screen:
    name: str
    states: List[ScreenState]
    semantics: Dict = None
