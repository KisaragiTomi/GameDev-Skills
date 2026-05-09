"""Stub implementation for Houdini native node 'floor'.

Status: stub. Replace this file with an exact or approximate implementation
after validating the node behavior against Houdini.
"""
from __future__ import annotations

from typing import Any

NODE_NAME = "floor"
NODE_CONTEXT = "Vop"
STATUS = "stub"


def evaluate(
    inputs: dict[str, Any],
    params: dict[str, Any],
    context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Evaluate the node with explicit inputs, parameters, and optional context."""
    return {
        "status": STATUS,
        "node": NODE_NAME,
        "context": NODE_CONTEXT,
        "outputs": {},
        "message": "Stub only; Houdini behavior is not implemented yet.",
    }
