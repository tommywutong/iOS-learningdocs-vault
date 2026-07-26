---
title: 'init(preset:position:values:content:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/axismarks/init(preset:position:values:content:)-7414i'
source_url: 'https://developer.apple.com/documentation/charts/axismarks/init(preset:position:values:content:)-7414i'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axismarks/init%28preset%3Aposition%3Avalues%3Acontent%3A%29-7414i.json'
content_hash: 'sha256:9b9d3fcd18da8250'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisMarks](../axismarks.md)

# init(preset:position:values:content:)

<sub>Initializer</sub>

Creates axis markers with the given properties,will override default markers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(preset: AxisMarkPreset = .automatic, position: AxisMarkPosition = .automatic, values: AxisMarkValues = .automatic, @AxisMarkBuilder content: @escaping (AxisValue) -> Content)
```

## Parameters

- `preset` — The preset of the axis markers.

- `position` — The position of the axis markers.

- `values` — The values of the axis markers.

- `content` — A result builder that returns the content of the axis marker for a given axis value.
