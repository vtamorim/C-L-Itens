from dataclasses import dataclass
from typing import Optional



@dataclass
class Item:
    descricao : str
    quantidade : int
    id: Optional[int] = None