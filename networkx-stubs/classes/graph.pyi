# Stubs for networkx.classes.graph (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, Generic, TypeVar

from networkx.classes.reportviews import NodeView

T = TypeVar('T')
class Graph(Generic[T]):
    node_dict_factory: Any = ...
    node_attr_dict_factory: Any = ...
    adjlist_outer_dict_factory: Any = ...
    adjlist_inner_dict_factory: Any = ...
    edge_attr_dict_factory: Any = ...
    graph_attr_dict_factory: Any = ...
    def to_directed_class(self): ...
    def to_undirected_class(self): ...
    graph: Any = ...
    def __init__(self, incoming_graph_data: Any = ..., **attr: Any) -> None: ...
    @property
    def adj(self): ...
    @property
    def name(self): ...
    @name.setter
    def name(self, s: Any) -> None: ...
    def __iter__(self): ...
    def __contains__(self, n: Any): ...
    def __len__(self): ...
    def __getitem__(self, n: Any): ...
    def add_node(self, node_for_adding: T, **attr: Any) -> None: ...
    def add_nodes_from(self, nodes_for_adding: Any, **attr: Any) -> None: ...
    def remove_node(self, n: Any) -> None: ...
    def remove_nodes_from(self, nodes: Any) -> None: ...
    @property
    def nodes(self) -> NodeView[T]: ...
    node: Any = ...
    def add_path(self, nodes: Any, **attr: Any): ...
    def add_cycle(self, nodes: Any, **attr: Any): ...
    def add_star(self, nodes: Any, **attr: Any): ...
    def nodes_with_selfloops(self): ...
    def number_of_selfloops(self): ...
    def selfloop_edges(self, data: bool = ..., keys: bool = ..., default: Optional[Any] = ...): ...
    def number_of_nodes(self): ...
    def order(self): ...
    def has_node(self, n: Any): ...
    def add_edge(self, u_of_edge: T, v_of_edge: T, **attr: Any) -> None: ...
    def add_edges_from(self, ebunch_to_add: Any, **attr: Any) -> None: ...
    def add_weighted_edges_from(self, ebunch_to_add: Any, weight: str = ..., **attr: Any) -> None: ...
    def remove_edge(self, u: Any, v: Any) -> None: ...
    def remove_edges_from(self, ebunch: Any) -> None: ...
    def update(self, edges: Optional[Any] = ..., nodes: Optional[Any] = ...) -> None: ...
    def has_edge(self, u: Any, v: Any): ...
    def neighbors(self, n: Any): ...
    @property
    def edges(self): ...
    def get_edge_data(self, u: Any, v: Any, default: Optional[Any] = ...): ...
    def adjacency(self): ...
    @property
    def degree(self): ...
    def clear(self) -> None: ...
    def is_multigraph(self): ...
    def is_directed(self): ...
    def fresh_copy(self): ...
    def copy(self, as_view: bool = ...): ...
    def to_directed(self, as_view: bool = ...): ...
    def to_undirected(self, as_view: bool = ...): ...
    def subgraph(self, nodes: Any): ...
    def edge_subgraph(self, edges: Any): ...
    def size(self, weight: Optional[Any] = ...): ...
    def number_of_edges(self, u: Optional[Any] = ..., v: Optional[Any] = ...): ...
    def nbunch_iter(self, nbunch: Optional[Any] = ...): ...


def _alias(origin, params, inst=True):
    return _GenericAlias(origin, params, special=True, inst=inst)

Graph = _al
