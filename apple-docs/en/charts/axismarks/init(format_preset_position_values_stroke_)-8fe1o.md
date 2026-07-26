---
title: 'init(format:preset:position:values:stroke:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/axismarks/init(format:preset:position:values:stroke:)-8fe1o'
source_url: 'https://developer.apple.com/documentation/charts/axismarks/init(format:preset:position:values:stroke:)-8fe1o'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axismarks/init%28format%3Apreset%3Aposition%3Avalues%3Astroke%3A%29-8fe1o.json'
content_hash: 'sha256:d431e495c30f05ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisMarks](../axismarks.md)

# init(format:preset:position:values:stroke:)

<sub>Initializer</sub>

Creates axis markers with the given properties, will override default markers. Default content will be used for the axis markers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Format>(format: Format, preset: AxisMarkPreset = .automatic, position: AxisMarkPosition = .automatic, values: AxisMarkValues = .automatic, stroke: StrokeStyle? = nil) where Content == Never, Format : FormatStyle, Format.FormatInput : Plottable, Format.FormatOutput == String
```

## Parameters

- `format` — The format to use for the labels.

- `preset` — The preset of the axis markers.

- `position` — The position of the axis markers.

- `values` — The values of the axis markers.

- `stroke` — The stroke to use for grid lines and ticks.
