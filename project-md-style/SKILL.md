---
name: project-md-style
description: Use when writing, editing, reviewing, normalizing, or refactoring project Markdown (.md) documentation, including architecture notes, pipeline docs, asset/property docs, API notes, setup guides, code-adjacent specifications, and SVG diagrams referenced by those docs. Also use for 规范化MD编写, 统一Markdown风格, 整理文档, 改写字段说明, drawing or updating SVG documentation diagrams, converting field tables into inline comments, and cleaning up technical docs while preserving meaning. Enforce concise source-grounded structure, stable headings, language consistency, labeled code fences, appropriate schema tables, concise same-line comments, referenced SVG artifacts, unique background styles for core classes or nodes, and SVG pattern texture/background color differences fixed to 20% after opacity blending.
---

# Project Markdown Style

## Overview

Write project Markdown as practical engineering documentation: concise, searchable, easy to diff, and close to the code or data it describes.

Preserve the existing document language and tone. For Chinese project docs, keep prose and comments in Chinese while leaving code identifiers, file paths, method names, keys, and enum values unchanged.

Standardize Markdown without changing technical meaning. Make documents easier to scan, keep examples copy-friendly, and avoid duplicating the same field explanation in both a code block and a table.

## Workflow

1. Read the target `.md` file and nearby project docs before making structural changes.
2. Preserve existing headings and anchors unless renaming clearly improves clarity.
3. Update related examples, field lists, and cross-references together.
4. Mark unknown or inferred behavior explicitly; do not invent implementation details.
5. Prefer small, focused edits over broad rewrites when maintaining an existing doc.
6. Identify whether each table is a structural field table or an overview/comparison table.
7. Convert structural field tables into same-line comments on the matching code/dictionary example when that avoids duplicated maintenance.
8. Re-scan edited sections for stale duplicated explanations, broken heading flow, and code blocks with missing or overlong comments.

## Document Structure

- Start with one `#` title that matches the file purpose.
- Add a short purpose paragraph when the file is longer than a quick note.
- Use `##` sections for stable topics such as Overview, Data Flow, Fields, Rules, Examples, Risks, and Open Questions.
- Use `###` only when a section has multiple meaningful subtopics.
- Keep paragraphs short. Prefer bullets for facts, constraints, and step lists.
- Keep terminology consistent with code and existing docs.
- Put file paths, symbols, keys, commands, and literal values in backticks.
- Avoid decorative prose, marketing language, and unexplained abbreviations.

## Code And Parameters

- Always label fenced code blocks with a language such as `gdscript`, `json`, `yaml`, `bash`, `text`, or the closest accurate option.
- Use code blocks for runnable snippets, short access examples, and compact config examples. Use tables for long record schemas, source-type responsibility lists, field inventories, and dictionaries that would need many commented lines.
- When documenting short parameters, properties, metadata keys, config entries, record fields, or return values inside a code block, put the value or explanation on the same line as the item.
- Align same-line comments into a readable column when the block has repeated fields.
- Prefer a concise same-line `#` comment over a separate explanatory bullet when the field can fit on one line.
- Keep examples realistic and source-grounded. If an example is hypothetical, label it as an example.
- If a code line would become too long or wrap badly, shorten the comment first. If several lines still need long comments, replace the block with a table.
- Match comment syntax to the code block language. Use `#` in `gdscript`, `python`, YAML, and shell-like examples. Use `//` in JavaScript/TypeScript/C-like examples.
- Do not add comments to strict `json` blocks. If comments are important and the block is illustrative, change the fence to `jsonc` or another appropriate non-strict language.
- Keep same-line comments short: `Type, purpose`, default, source, or runtime effect is enough.
- If a value has aliases, document the preferred key and mention aliases only when useful.

Use this style for short metadata access examples:

```gdscript
node.get_meta("auto_id")              # "Cliff_s1_0_m0"
node.get_meta("auto_source")          # "meshfill"
node.get_meta("auto_object_type")     # "rock"
node.get_meta("bound_min_length")     # scaled bound minimum axis length
node.get_meta("min_spacing")          # default bound_min_length * 0.5

var record: Dictionary = node.get_meta("voxel_record")
record.color                          # Color(0.55, 0.50, 0.45, 1.0)
record.complexity                     # 1.0
record.auto_object_id                 # "Cliff_s1_0_m0"
record.instance_mesh_id               # actual MeshInstance3D instance id
```

Use this style for config-like examples:

```yaml
asset_type: "rock"                    # primary asset type
asset_subtype: "cliff"                # asset subtype
min_spacing: 0.5                      # default spacing multiplier
affected_bands: ["ground", "canopy"]  # written height bands
```

Use this style for concrete dictionary/config examples:

```gdscript
{
	"band": "canopy",                         # String, band name
	"channel": 3,                             # int, RGBA channel index
	"radius": 3.0,                            # float, world-space radius
	"color": Color(0.8, 0.2, 0.2, 0.2),       # Color, debug color
	"complexity": 0.2,                        # float, value written to occupancy
}
```

Avoid duplicating the same field list as prose plus a `| Field | Type | Description |` table when the code block already carries clear comments.

Use this style for source/type responsibility descriptions:

| Source Voxel | Producer | Purpose |
| --- | --- | --- |
| `AutoSceneVoxel` | automatic generation such as meshfill, scatter, or procedural placement | derived occupancy, blockers, surfaces, or vegetation |
| `BrushSceneVoxel` | brush and active edits such as paint, erase, lock, or manual override | user/tool-authored scene intent |
| `SceneVoxel` | blend stage | final result read by occupancy, voxel volume, and validation |

## Tables

Use tables when comparing multiple items, documenting schemas, or replacing commented pseudo-objects:

| Field | Type | Meaning |
| --- | --- | --- |
| `auto_id` | `String` | generated object id |
| `voxel_record` | `Dictionary` | record written to voxel/band data |

Keep table cells short. Move long explanations to a following paragraph only when necessary.

Keep tables for:

- Class/type hierarchies
- Asset matrices
- Comparison or decision tables
- File lists
- Validation thresholds
- Workflow stage summaries
- Long record schemas or field inventories where inline comments would wrap badly

Replace tables with same-line comments when:

- The table only explains keys already shown in a dictionary/config example.
- A code block and table must be kept in sync manually.
- The user asks for comments to be written on the same parameter line.

## SVG Diagrams

- Create or edit SVGs when a diagram clarifies architecture, data flow, ownership, class relationships, pipeline stages, or record/schema movement better than prose.
- Store new SVGs in the project's existing graph/diagram location, such as `docs/graphs/`, unless nearby docs already use another convention.
- Reference every newly added SVG from the corresponding Markdown document in the same change. Put the link near the section it explains, or in the document's graph/related-docs list if that is the local pattern.
- Update graph indexes such as `docs/graphs/README.md` when the project already maintains one.
- Keep SVG text explicit with manual line breaks. Do not rely on SVG auto-wrapping.
- Give stable dimensions to nodes, lanes, labels, and legends so text and arrows do not overlap.
- Use semantic SVG classes such as `.autoobject`, `.scene-voxel`, or `.runtime-output` rather than anonymous repeated styling.
- Give core classes, core resources, or central runtime states visually distinct backgrounds. Prefer subtle patterns in `<defs>` such as dots, stripes, grids, crosshatch, or tinted fills over relying only on color.
- Keep texture colors deterministically aligned with the node's base background: after opacity blending, every intentional SVG pattern mark must have a visible texture/background difference fixed at 20% of the RGB channel range.
  - Measure the visible difference after alpha blending, not the raw `fill` colors. For each pattern mark, compute `visible = base * (1 - opacity) + texture * opacity`, then measure `max(abs(visible.r - base.r), abs(visible.g - base.g), abs(visible.b - base.b))`.
  - The target difference is exactly `51` RGB levels, because `51 / 255 = 20%`. Allow at most `±1` level for rounding, antialiasing, or browser color quantization.
  - Choose texture `opacity` from the raw color distance: `opacity = 51 / max(abs(texture - base))`, clamped to `0..1`. Prefer same-hue, slightly darker or lighter texture fills so this opacity remains readable but not harsh.
  - Apply the same 20% rule to dots, stripes, grids, crosshatches, and other repeated background marks used inside `<pattern>`. Decorative shadows, arrows, labels, foreground icons, and non-pattern node fills are not texture marks.
  - When changing a patterned background, re-run a color-difference check and render/screenshot-check the edited SVG before finishing.
- Reuse a background style consistently for the same core concept across related diagrams.
- Keep non-core/support nodes quieter so the primary classes remain visually scannable.
- Include a small legend only when the unique background styles are not obvious from labels.
- Render or screenshot-check edited SVGs before finishing. Verify text readability, no clipping, no overlaps, visible unique backgrounds, and that the Markdown references point to the right file.

## Maintenance Rules

- Update examples when field names, default values, or behavior change.
- Keep outdated behavior only if it is explicitly marked as legacy.
- Do not duplicate the same field list in multiple sections unless each section serves a different reader task.
- Preserve existing TODO/Open Questions sections and add unresolved points there.
- Keep Markdown lint-friendly spacing: blank line before headings, lists, tables, and fenced code blocks.
- Do not add generated timestamps, author signatures, or change logs unless the existing file already uses them.

## Review Checklist

- The title and headings describe the actual content.
- Code fences have language labels.
- Schemas and long field lists use tables; short parameter/property examples use same-line comments where practical.
- Comments explain meaning, default, source, or runtime effect.
- Claims are supported by code, existing docs, or an explicit inference note.
- The document can be scanned without reading every paragraph.
- Nearby field tables are not stale duplicates of edited examples.
- Overview/comparison tables were not flattened unnecessarily.
- New SVGs are referenced by the owning Markdown document and any graph index used by the project.
- Core classes or central nodes in SVGs have unique, readable background styles, with every pattern texture mark fixed to the 20% visible background-difference rule (`51 ± 1` RGB levels after opacity blending).
