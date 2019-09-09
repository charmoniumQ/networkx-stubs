# Stubs for networkx.algorithms.operators.binary (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, TypeVar, Union

from networkx.classes.graph import Graph

X = TypeVar('X')
Y = TypeVar('Y')
def union(G: Any, H: Any, rename: Any = ..., name: Optional[Any] = ...): ...
def disjoint_union(G: Any, H: Any): ...
def intersection(G: Any, H: Any): ...
def difference(G: Any, H: Any): ...
def symmetric_difference(G: Any, H: Any): ...
def compose(G: Graph[X], H: Graph[Y]) -> Graph[Union[X,Y]]: ...
