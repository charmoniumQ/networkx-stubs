# Stubs for networkx.algorithms.simple_paths (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def is_simple_path(G: Any, nodes: Any): ...
def all_simple_paths(G: Any, source: Any, target: Any, cutoff: Optional[Any] = ...): ...
def shortest_simple_paths(G: Any, source: Any, target: Any, weight: Optional[Any] = ...): ...

class PathBuffer:
    paths: Any = ...
    sortedpaths: Any = ...
    counter: Any = ...
    def __init__(self) -> None: ...
    def __len__(self): ...
    def push(self, cost: Any, path: Any) -> None: ...
    def pop(self): ...
