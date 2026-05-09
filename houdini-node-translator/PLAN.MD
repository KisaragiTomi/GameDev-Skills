# Houdini Native Node Implementation Plan

本计划定义 `native_nodes` 中每一个 Houdini 原生节点的实现与文档要求。目标是让每个节点都具备 Python 和 GDScript 两种实现，并且每种实现都有对应说明文档。

## Scope

节点清单以 `hda_native_node_totals.csv` 的 `native_base_type` 列为准。

节点目录包括：

- `native_nodes/<node_name>/`
- `native_nodes/vop/<node_name>/`

`native_nodes/vop/` 是分类目录，不作为节点本身处理。

## Required Layout

每个节点目录必须逐步补齐以下结构：

```text
<node_dir>/
  python/
    implementation.py
    README.md
  gdscript/
    implementation.gd
    README.md
```

| Path | Required | Purpose |
| --- | --- | --- |
| `python/implementation.py` | Yes | Python reference implementation or approximation. |
| `python/README.md` | Yes | Python behavior, API, assumptions, and validation notes. |
| `gdscript/implementation.gd` | Yes | Godot/GDScript implementation or approximation. |
| `gdscript/README.md` | Yes | GDScript usage, Godot-specific limits, and validation notes. |

## Implementation Contract

Implementations should expose a small, consistent evaluation surface so nodes can be tested and composed later.

Python implementations should prefer this shape:

```python
def evaluate(inputs: dict, params: dict, context: dict | None = None) -> dict:
    """Evaluate the node with explicit inputs, parameters, and optional context."""
```

GDScript implementations should prefer this shape:

```gdscript
func evaluate(inputs: Dictionary, params: Dictionary, context: Dictionary = {}) -> Dictionary:
    return {}
```

When a node cannot be faithfully implemented outside Houdini, the implementation must still exist and return a documented approximation, stub, or unsupported result.

## Documentation Contract

Each `README.md` must include:

- `# <node_name> Python Implementation` or `# <node_name> GDScript Implementation`
- Houdini node role and source context, such as SOP, VOP, COP, DOP, ROP, TOP, SHOP, or OBJ.
- Supported inputs and outputs.
- Supported parameters.
- Known unsupported Houdini behavior.
- Approximation strategy when exact parity is not possible.
- Minimal usage example.
- Validation notes against Houdini or known expected values.

Use this status vocabulary:

| Status | Meaning |
| --- | --- |
| `exact` | Behavior is expected to match Houdini for documented inputs. |
| `approximate` | Behavior preserves intent but may differ numerically or structurally. |
| `stub` | File exists with API and documentation, but behavior is not implemented yet. |
| `unsupported` | Behavior depends on Houdini-only runtime, renderer, solver, or asset state. |

## Node Classification

Before implementing a node, classify it:

| Class | Examples | Implementation Strategy |
| --- | --- | --- |
| Math/value | `add`, `multiply`, `clamp`, `fit` | Direct Python and GDScript logic. |
| Geometry/SOP | `polyextrude`, `scatter`, `attribpromote` | Approximate with mesh/attribute data structures. |
| VOP/shader | `bind`, `parameter`, `pbrlighting` | Implement numeric core where possible; document shader/runtime gaps. |
| Volume/VDB | `volumesample`, `vdbcombine` | Prefer documented stubs or simplified dense-grid approximations. |
| Simulation/DOP | `popsolver`, `vellumsolver`, `rbdpackedobject` | Usually `unsupported` or high-level approximation. |
| Render/material | `principledshader`, `pyroshader` | Preserve parameter model; renderer parity is usually unsupported. |
| Network/control | `subnet`, `switch`, `merge`, `block_begin` | Implement graph/control behavior where possible. |

## Work Phases

1. Generate missing per-node folders from `hda_native_node_totals.csv`.
2. Create the required `python/` and `gdscript/` subfolders for every node directory.
3. Add stub `implementation.py`, `implementation.gd`, and both `README.md` files for every node.
4. Prioritize high-count nodes from `hda_native_node_totals.csv`.
5. Replace stubs with exact or approximate implementations in small batches.
6. Add validation cases for each completed implementation.
7. Track unsupported Houdini-only behavior explicitly in each language README.

## Priority Order

Implement high-frequency and low-risk nodes first:

1. Pure math and value nodes.
2. Attribute and vector utility nodes.
3. Simple graph/control nodes.
4. Common SOP data transforms.
5. VOP numeric utilities.
6. Volume, material, render, and solver nodes.

## Validation

Each completed node should include at least one small validation case in the language README.

Validation should record:

- Input dictionary.
- Parameter dictionary.
- Expected output dictionary.
- Fidelity status.
- Houdini comparison source when available.

Example:

```yaml
inputs: {"a": 2.0, "b": 3.0}
params: {}
expected: {"result": 5.0}
status: "exact"
```

## Open Questions

- Whether to add shared runtime helpers for geometry, volumes, matrices, and shader values.
- Whether per-node tests should live beside implementations or in a central `tests/` directory.
- Whether VOP nodes should use shader-style types or plain numeric/vector dictionaries.
- Whether generated stubs should include metadata copied from `hda_native_node_totals.csv`.
