# compile_begin GDScript Implementation

## Status

| Field | Value |
| --- | --- |
| Node | `compile_begin` |
| Source context | `TBD` |
| Fidelity | `stub` |
| Native count | `302` |

## Role

TODO: Document the Houdini behavior for `compile_begin` before replacing the stub.

## API

```gdscript
var impl := preload("implementation.gd").new()
var result := impl.evaluate({}, {}, {})
```

## Supported Inputs And Outputs

No Houdini-compatible inputs or outputs are implemented yet.

## Supported Parameters

No Houdini parameters are implemented yet.

## Unsupported Houdini Behavior

All Houdini runtime behavior is currently unsupported in this stub.

## Approximation Strategy

Return a structured `stub` result until the node is implemented as `exact`, `approximate`, or `unsupported`.

## Validation

```yaml
inputs: {}
params: {}
expected:
  status: "stub"
status: "stub"
```
