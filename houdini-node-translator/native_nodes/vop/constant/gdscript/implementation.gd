extends RefCounted

const NODE_NAME := "constant"
const NODE_CONTEXT := "Vop"
const STATUS := "stub"


func evaluate(inputs: Dictionary, params: Dictionary, context: Dictionary = {}) -> Dictionary:
    return {
        "status": STATUS,
        "node": NODE_NAME,
        "context": NODE_CONTEXT,
        "outputs": {},
        "message": "Stub only; Houdini behavior is not implemented yet."
    }
