---
title: VectorizedRectanglePlotContent
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/vectorizedrectangleplotcontent
source_url: 'https://developer.apple.com/documentation/charts/vectorizedrectangleplotcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/vectorizedrectangleplotcontent.json'
content_hash: 'sha256:f46f6b0b40892139'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# VectorizedRectanglePlotContent

<sub>Structure</sub>

An opaque vectorized chart content type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct VectorizedRectanglePlotContent<Data> where Data : RandomAccessCollection
```

## Overview

Don’t use this type directly. Swift Charts automatically instantiates and consumes values of this type.

## Relationships

- **Conforms To**: [ChartContent](chartcontent.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [VectorizedChartContent](vectorizedchartcontent.md)

## See Also

### Supporting types

- [body](chartcontent/body-swift.property.md) — The content and behavior of the chart content.
