---
title: 'init(angle:innerRadius:outerRadius:angularInset:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/sectormark/init(angle:innerradius:outerradius:angularinset:)'
source_url: 'https://developer.apple.com/documentation/charts/sectormark/init(angle:innerradius:outerradius:angularinset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/sectormark/init%28angle%3Ainnerradius%3Aouterradius%3Aangularinset%3A%29.json'
content_hash: 'sha256:38d97d22f393dbc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [SectorMark](../sectormark.md)

# init(angle:innerRadius:outerRadius:angularInset:)

<sub>Initializer</sub>

Creates a sector mark, which uses the angular size to represent the proportion of the value to the sum of all values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(angle: PlottableValue<some Plottable>, innerRadius: MarkDimension = .automatic, outerRadius: MarkDimension = .automatic, angularInset: CGFloat? = nil)
```

## Parameters

- `angle` — A plottable value that will map to the angular size of the sector. It’s either a value that the angle within the full circle will be proportional with, or a value range for explicit start/end angles.

- `innerRadius` — The inner radius of the sector. It is either a size in points, or a `.ratio` or `.inset` relative to the outer radius.

- `outerRadius` — The outer radius of the sector. It is either a size in points, or a `.ratio`or `.inset` relative to the available plot area.

- `angularInset` — A radius for the corners of the sector.

## Discussion

Use this initializer to map angular positions to a sector for each data element.
