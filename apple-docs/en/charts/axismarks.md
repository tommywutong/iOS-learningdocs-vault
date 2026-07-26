---
title: AxisMarks
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/axismarks
source_url: 'https://developer.apple.com/documentation/charts/axismarks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axismarks.json'
content_hash: 'sha256:a7b67dd812c04570'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# AxisMarks

<sub>Structure</sub>

A group of visual marks that a chart draws to indicate the composition of a chart’s axes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AxisMarks<Content> where Content : AxisMark
```

## Relationships

- **Conforms To**: [AxisContent](axiscontent.md)

## Topics

### Supporting types

- [AxisMarkPreset](axismarkpreset.md) — Describes preset styles for axis markers.
- [AxisMarkValues](axismarkvalues.md) — Describes the values the axis markers will present (one for each value).
- [AxisMarkPosition](axismarkposition.md) — Describes the position of axis markers.

### Initializers

- [init(format:preset:position:values:stroke:)](<axismarks/init(format_preset_position_values_stroke_)-8fe1o.md>) — Creates axis markers with the given properties, will override default markers. Default content will be used for the axis markers.
- [init(format:preset:position:values:stroke:)](<axismarks/init(format_preset_position_values_stroke_)-98cpl.md>) — Creates axis markers with the given properties, will override default markers. Default content will be used for the axis markers.
- [init(preset:position:values:content:)](<axismarks/init(preset_position_values_content_)-1n9x7.md>) — Creates axis markers with the given properties, will override default markers.
- [init(preset:position:values:content:)](<axismarks/init(preset_position_values_content_)-4a4x7.md>) — Creates axis markers with the given properties, will override default markers.
- [init(preset:position:values:content:)](<axismarks/init(preset_position_values_content_)-6b1jq.md>) — Creates axis markers with the given properties,will override default markers.
- [init(preset:position:values:content:)](<axismarks/init(preset_position_values_content_)-7414i.md>) — Creates axis markers with the given properties,will override default markers.
- [init(preset:position:values:stroke:)](<axismarks/init(preset_position_values_stroke_)-8uk65.md>) — Creates axis markers with the given properties, will override default markers. Default content will be used for the axis markers.
- [init(preset:position:values:stroke:)](<axismarks/init(preset_position_values_stroke_)-8xkl5.md>) — Creates axis markers with the given properties, will override default markers. Default content will be used for the axis markers.

## See Also

### Axes

- [Customizing axes in Swift Charts](customizing-axes-in-swift-charts.md) — Improve the clarity of your chart by configuring the appearance of its axes.
- [ChartAxisContent](chartaxiscontent.md) — A view that represents a chart’s axis.
- [AxisContent](axiscontent.md) — A type that represents the elements you use to build a chart’s axes.
- [AnyAxisContent](anyaxiscontent.md) — A type-erased element of a chart’s axis.
- [AxisContentBuilder](axiscontentbuilder.md) — A result builder that constructs axis content.
