from dataclasses import dataclass
from typing import Optional

@dataclass
class Item:
    description : str
    amount : int
    id: Optional[int] = None
