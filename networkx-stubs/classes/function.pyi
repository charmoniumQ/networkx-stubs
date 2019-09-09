# Stubs for networkx.classes.function (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def nodes(G: Any): ...
def edges(G: Any, nbunch: Optional[Any] = ...): ...
def degree(G: Any, nbunch: Optional[Any] = ..., weight: Optional[Any] = ...): ...
def neighbors(G: Any, n: Any): ...
def number_of_nodes(G: Any): ...
def number_of_edges(G: Any): ...
def density(G: Any): ...
def degree_histogram(G: Any): ...
def is_directed(G: Any): ...
def freeze(G: Any): ...
def is_frozen(G: Any): ...
def add_star(G_to_add_to: Any, nodes_for_star: Any, **attr: Any) -> None: ...
def add_path(G_to_add_to: Any, nodes_for_path: Any, **attr: Any) -> None: ...
def add_cycle(G_to_add_to: Any, nodes_for_cycle: Any, **attr: Any) -> None: ...
def subgraph(G: Any, nbunch: Any): ...
def induced_subgraph(G: Any, nbunch: Any): ...
def edge_subgraph(G: Any, edges: Any): ...
def restricted_view(G: Any, nodes: Any, edges: Any): ...
def reverse_view(digraph: Any): ...
def to_directed(graph: Any): ...
def to_undirected(graph: Any): ...
def create_empty_copy(G: Any, with_data: bool = ...): ...
def info(G: Any, n: Optional[Any] = ...): ...
def set_node_attributes(G: Any, values: Any, name: Optional[Any] = ...) -> None: ...
def get_node_attributes(G: Any, name: Any): ...
def set_edge_attributes(G: Any, values: Any, name: Optional[Any] = ...) -> None: ...
def get_edge_attributes(G: Any, name: Any): ...
def all_neighbors(graph: Any, node: Any): ...
def non_neighbors(graph: Any, node: Any): ...
def non_edges(graph: Any) -> None: ...
def common_neighbors(G: Any, u: Any, v: Any): ...
def is_weighted(G: Any, edge: Optional[Any] = ..., weight: str = ...): ...
def is_negatively_weighted(G: Any, edge: Optional[Any] = ..., weight: str = ...): ...
def is_empty(G: Any): ...
def nodes_with_selfloops(G: Any): ...
def selfloop_edges(G: Any, data: bool = ..., keys: bool = ..., default: Optional[Any] = ...): ...
def number_of_selfloops(G: Any): ...
