# Stubs for networkx.drawing.nx_pylab (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def draw(G: Any, pos: Optional[Any] = ..., ax: Optional[Any] = ..., **kwds: Any) -> None: ...
def draw_networkx(G: Any, pos: Optional[Any] = ..., arrows: bool = ..., with_labels: bool = ..., **kwds: Any) -> None: ...
def draw_networkx_nodes(G: Any, pos: Any, nodelist: Optional[Any] = ..., node_size: int = ..., node_color: str = ..., node_shape: str = ..., alpha: float = ..., cmap: Optional[Any] = ..., vmin: Optional[Any] = ..., vmax: Optional[Any] = ..., ax: Optional[Any] = ..., linewidths: Optional[Any] = ..., edgecolors: Optional[Any] = ..., label: Optional[Any] = ..., **kwds: Any): ...
def draw_networkx_edges(G: Any, pos: Any, edgelist: Optional[Any] = ..., width: float = ..., edge_color: str = ..., style: str = ..., alpha: float = ..., arrowstyle: str = ..., arrowsize: int = ..., edge_cmap: Optional[Any] = ..., edge_vmin: Optional[Any] = ..., edge_vmax: Optional[Any] = ..., ax: Optional[Any] = ..., arrows: bool = ..., label: Optional[Any] = ..., node_size: int = ..., nodelist: Optional[Any] = ..., node_shape: str = ..., connectionstyle: Optional[Any] = ..., **kwds: Any): ...
def draw_networkx_labels(G: Any, pos: Any, labels: Optional[Any] = ..., font_size: int = ..., font_color: str = ..., font_family: str = ..., font_weight: str = ..., alpha: float = ..., bbox: Optional[Any] = ..., ax: Optional[Any] = ..., **kwds: Any): ...
def draw_networkx_edge_labels(G: Any, pos: Any, edge_labels: Optional[Any] = ..., label_pos: float = ..., font_size: int = ..., font_color: str = ..., font_family: str = ..., font_weight: str = ..., alpha: float = ..., bbox: Optional[Any] = ..., ax: Optional[Any] = ..., rotate: bool = ..., **kwds: Any): ...
def draw_circular(G: Any, **kwargs: Any) -> None: ...
def draw_kamada_kawai(G: Any, **kwargs: Any) -> None: ...
def draw_random(G: Any, **kwargs: Any) -> None: ...
def draw_spectral(G: Any, **kwargs: Any) -> None: ...
def draw_spring(G: Any, **kwargs: Any) -> None: ...
def draw_shell(G: Any, **kwargs: Any) -> None: ...
def draw_planar(G: Any, **kwargs: Any) -> None: ...
