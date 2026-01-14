from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class UIComponent:
    label: str
    state: str


@dataclass
class ScreenState:
    name: str
    components: List[UIComponent]


@dataclass
class Screen:
    name: str
    states: List[ScreenState]
    semantics: Dict = field(default_factory=dict)
