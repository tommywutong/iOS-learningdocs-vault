---
title: BuilderConditional
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/builderconditional
source_url: 'https://developer.apple.com/documentation/charts/builderconditional'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/builderconditional.json'
content_hash: 'sha256:f485661cf3d94c0e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# BuilderConditional

<sub>Structure</sub>

A conditional result from a result builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct BuilderConditional<TrueContent, FalseContent>
```

## Overview

Don’t use this type directly. The result builders defined by the framework, like [ChartContentBuilder](chartcontentbuilder.md) and [AxisContentBuilder](axiscontentbuilder.md), use it as part of the building process.

## Relationships

- **Conforms To**: [AxisContent](axiscontent.md), [AxisMark](axismark.md), [Chart3DContent](chart3dcontent.md), [ChartContent](chartcontent.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md)
