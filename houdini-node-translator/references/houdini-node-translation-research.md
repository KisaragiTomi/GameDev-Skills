# Houdini Node Translation Research

_Last researched: 2026-05-09._

## Summary

No mature public `SKILL.md` was found that directly translates arbitrary SideFX Houdini node networks into pure Python, Blender Geometry Nodes, Maya/Bifrost, Unreal PCG, or other DCC node graphs.

The open-source ecosystem currently clusters around four adjacent capabilities:

1. Exporting or recreating Houdini networks as Houdini Python.
2. Serializing Houdini networks for AI/context inspection.
3. Operating Houdini through AI agents, MCP, or command bridges.
4. Embedding Houdini networks in other software through HDAs/Houdini Engine rather than translating them.

## Relevant Sources

### SideFX HOM: `hou.Node.asCode()`

- URL: <https://www.sidefx.com/docs/houdini/hom/hou/Node.html>
- Relevance: Official Houdini Object Model API for generating Python code that recreates Houdini nodes/networks.
- Use as: Baseline for `Houdini node graph -> Houdini Python` recreation.
- Limitation: It recreates Houdini networks; it does not semantically translate nodes into Blender, Maya, Unreal, or pure algorithmic Python.

### Houdini2Chat

- URL: <https://github.com/rendermagix/houdini2chat>
- Relevance: Exports Houdini network/context information for AI workflows, including node data, parameters, references, and expressions.
- Use as: Front-end extraction/context source before building an intermediate representation.
- Limitation: Oriented toward AI-readable export, not automatic target-DCC graph generation.

### Houdini-Agent

- URL: <https://github.com/Kazama-Suichiku/Houdini-Agent>
- Relevance: In-Houdini AI assistant and skill system. Public descriptions mention geometry analysis, normals, bounding box, connectivity, attribute diff, dead nodes, dependency tracing, and cook performance.
- Use as: Reference for Houdini-side analysis and agent operations.
- Limitation: Built-in skills appear focused on inspection/performance/dependency work, not cross-DCC translation.

### ArtClaw Bridge

- URL: <https://github.com/IvanYangYangXi/artclaw_bridge>
- Houdini skill path: <https://github.com/IvanYangYangXi/artclaw_bridge/tree/main/skills/official/houdini>
- Relevance: Contains official Houdini skill packs such as `houdini-context`, `houdini-node-ops`, `houdini-operation-rules`, and `houdini-simulation`. Also has node-operation concepts for other creative tools.
- Use as: Template/reference for a skill-based workflow that can inspect and operate Houdini nodes.
- Limitation: Not found to provide a complete arbitrary Houdini-to-other-DCC translator.

### dcc-mcp-core

- URL: <https://github.com/loonghao/dcc-mcp-core>
- Relevance: Cross-DCC MCP framework with Skills-First concepts and Houdini/Blender/Maya-style adapter direction.
- Use as: Candidate execution layer for reading a Houdini graph and creating equivalent target-DCC objects.
- Limitation: Framework/backend; target-specific node semantic mappings still need to be authored.

### Houdini MCP Servers

- URL: <https://github.com/eliiik/houdini-mcp>
- Relevance: MCP bridge for controlling Houdini from an agent.
- Use as: Execution backend for extraction, inspection, or applying generated Python inside Houdini.
- Limitation: Bridge layer only; no built-in general translator confirmed.

## Practical Translation Architecture

A robust translator should use an intermediate representation instead of direct string conversion.

```json
{
  "source": {
    "software": "Houdini",
    "version": "unknown",
    "context": "SOP",
    "root_path": "/obj/geo1"
  },
  "nodes": [
    {
      "id": "box1",
      "type": "box",
      "category": "geometry_source",
      "parameters": { "size": [1, 1, 1] },
      "expressions": {},
      "inputs": [],
      "outputs": ["transform1"],
      "mapping_status": "direct"
    }
  ],
  "connections": [
    { "from": "box1", "to": "transform1", "input_index": 0 }
  ],
  "attributes": [],
  "groups": [],
  "time_dependencies": [],
  "unsupported_features": []
}
```

Recommended pipeline:

1. Extract graph from Houdini with HOM, `hou.Node.asCode()`, Houdini2Chat, or MCP.
2. Normalize into IR: nodes, edges, parameters, expressions, attributes, groups, time dependencies, and external assets.
3. Resolve semantic categories: source geometry, transforms, topology edits, attribute operations, instancing, scattering, simulation, rendering, IO.
4. Map to target capabilities with a mapping table.
5. Generate code, node creation script, migration plan, or HDA integration plan.
6. Validate by comparing bounding boxes, point/primitive counts, attributes, visual output, and baked caches.

## Mapping Guidance

| Houdini feature | Target strategy |
| --- | --- |
| Basic SOP geometry sources | Direct node/script creation in target app where available. |
| Transform, merge, switch, delete | Usually direct or simple script mapping. |
| Attribute wrangle/VEX | Translate algorithm separately; target may need Python, shader code, or custom node group. |
| VDB/volumes | Prefer baking/export or target-specific volume nodes. |
| Copy to Points/instancing | Map to target instancing system, preserving attributes such as scale/orient/name. |
| Solver/simulation/DOPs | Prefer HDA/Houdini Engine or baked cache unless equivalent solver exists. |
| USD/LOP/Solaris | Prefer USD-native transfer where target supports USD. |
| Expressions/channels | Convert to target animation drivers when possible; otherwise bake. |
| HDAs | Use as black-box procedural asset through Houdini Engine if direct translation is too expensive. |

## Recommended Skill Behavior

When asked to translate a Houdini node flow:

- Do not promise exact parity without inspecting nodes and parameters.
- Ask for node graph export when only a screenshot is available.
- Prefer `hou.Node.asCode()` for Houdini Python recreation.
- Prefer IR + mapping table for cross-DCC migration.
- Use HDA/Houdini Engine or caches for simulations and complex procedural assets.
- Report unsupported or approximate mappings explicitly.

## Search Conclusion

The community has useful building blocks, but not a complete general-purpose Houdini node translator skill. The most realistic new skill is a workflow skill that:

1. Extracts or accepts Houdini graph data.
2. Converts it into neutral IR.
3. Produces target-specific code, node-construction plans, or migration reports.
4. Separates exact recreation from approximate cross-DCC translation.
