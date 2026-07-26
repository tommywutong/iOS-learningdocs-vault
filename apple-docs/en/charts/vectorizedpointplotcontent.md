---
title: VectorizedPointPlotContent
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/vectorizedpointplotcontent
source_url: 'https://developer.apple.com/documentation/charts/vectorizedpointplotcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/vectorizedpointplotcontent.json'
content_hash: 'sha256:cce33d600e7f42a4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# VectorizedPointPlotContent

<sub>Structure</sub>

An opaque vectorized chart content type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct VectorizedPointPlotContent<Data> where Data : RandomAccessCollection
```

## Overview

Don’t use this type directly. Swift Charts automatically instantiates and consumes values of this type.

## Relationships

- **Conforms To**: [ChartContent](chartcontent.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [VectorizedChartContent](vectorizedchartcontent.md)

## See Also

### Supporting types

- [body](chartcontent/body-swift.property.md) — The content and behavior of the chart content.
