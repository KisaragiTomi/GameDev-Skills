---
name: houdini-node-translator
description: Translate, reconstruct, or migrate SideFX Houdini node networks and procedural flows into Python, pseudocode, intermediate JSON/IR, Blender Geometry Nodes plans, Maya/Bifrost-style plans, Unreal/PCG/HDA usage notes, or other DCC/software representations. Use when the user asks to convert Houdini nodes to Python, explain a Houdini node flow as code, serialize SOP/VOP/LOP networks, map Houdini procedural workflows to Blender/Unreal/Maya, or design a cross-DCC node translation pipeline.
---

# Houdini Node Translator

Use this skill for Houdini node-network translation tasks. Prefer faithful analysis over claiming one-click parity: most Houdini networks cannot be translated losslessly to other software without target-specific approximations.

## Workflow

1. Identify the source network scope: SOP, VOP, COP, LOP/Solaris, CHOP, ROP, TOP, HDA, or mixed context.
2. Ask for or extract the node graph: screenshots, `.hip` context, `hou.Node.asCode()` output, Houdini2Chat export, node path, parameter dump, or manual node list.
3. Build a neutral intermediate representation with nodes, connections, parameters, expressions, attributes, groups, inputs, outputs, and side effects.
4. Classify each node as direct mapping, approximate mapping, code generation, baked asset, HDA wrapper, or unsupported.
5. Generate the requested target:
   - Houdini Python recreation code via HOM patterns.
   - Plain Python or NumPy-style pseudocode for algorithm explanation.
   - Blender Geometry Nodes construction plan or `bpy` script outline.
   - Maya/Bifrost-style graph plan.
   - Unreal PCG/HDA integration plan.
   - JSON/Markdown migration report.
6. Include a fidelity table: exact, approximate, manual, unsupported.
7. Preserve procedural intent and call out simulation, solver, VEX, attributes, time dependency, and unit/axis differences.

## Preferred Inputs

- Node path, e.g. `/obj/geo1/subnet1`.
- Houdini version and target software/version.
- Export from `hou.Node.asCode()` for Python recreation tasks.
- Export from Houdini2Chat or a similar node/parameter dump for AI analysis.
- Screenshots only as a fallback; ask for parameter dumps when precision matters.

## Translation Strategy

- Use `hou.Node.asCode()` as the baseline for Houdini-to-Houdini Python recreation.
- For cross-DCC translation, do not copy nodes mechanically. Translate procedural intent into a target-native graph or script.
- For VEX wrangles, extract the algorithm separately and translate to pseudocode, Python, shader code, or target expression language.
- For simulations, prefer HDA/Houdini Engine, baked caches, or high-level approximations unless the target has equivalent solvers.
- For packed primitives, volumes, VDBs, USD, and attributes, explicitly map data model differences.

## Output Checklist

Always include:

- Source scope and assumptions.
- Target format and limitations.
- Node mapping table.
- Generated code/IR/plan.
- Manual follow-up steps.
- Validation suggestions inside Houdini and the target app.

## Research Notes

Load `references/houdini-node-translation-research.md` when the user asks about existing tools, community projects, prior art, or why a direct translator is hard.
