# boot.py (in workspace root)
from __future__ import annotations
import runpy, pathlib
from typing import Any

def _apply_view_defaults() -> None:
    try:
        from ocp_vscode import set_defaults
        try:
            set_defaults(reset_camera=False, axes=False, transparent=False, show_logo=False)  # type: ignore[call-arg]
        except TypeError:
            # if your version doesn't have show_logo
            set_defaults(reset_camera=False, axes=False, transparent=False)
    except Exception:
        pass

def _seed_globals() -> dict[str, Any]:
    seed = {"__name__": "__main__"}
    try:
        import build123d as b3d
        seed.update({k: v for k, v in b3d.__dict__.items() if not k.startswith("_")})
    except Exception:
        pass
    return seed

def _auto_pick_object(ns: dict[str, Any]):
    for k in ("result", "MODEL", "part", "assembly"):
        if k in ns:
            return ns[k]
    try:
        from build123d import Part, Compound, Shape, BuildPart
        last = None
        for v in ns.values():
            if isinstance(v, (Part, Compound, Shape, BuildPart)):
                last = v
        return last
    except Exception:
        return None

def render(path: str) -> None:
    _apply_view_defaults()
    ns = runpy.run_path(path, init_globals=_seed_globals())
    try:
        from ocp_vscode import show
        obj = _auto_pick_object(ns)
        if obj is not None:
            show(obj)
    except Exception:
        pass

def export_stl(path: str, out_path: str | None = None) -> None:
    _apply_view_defaults()
    ns = runpy.run_path(path, init_globals=_seed_globals())
    obj = _auto_pick_object(ns)
    if obj is None:
        raise SystemExit("Geometry not found: put the object in result / MODEL / part / assembly.")

    # Convert BuildPart to Part if needed
    from build123d import BuildPart, export_stl as b3d_export_stl
    if isinstance(obj, BuildPart):
        obj = obj.part

    p = pathlib.Path(out_path) if out_path else pathlib.Path(path).with_suffix(".stl")
    b3d_export_stl(obj, str(p))  # type: ignore[arg-type]
    print(f"STL: {p}")
