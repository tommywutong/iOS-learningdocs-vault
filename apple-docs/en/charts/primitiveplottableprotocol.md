---
title: PrimitivePlottableProtocol
framework: Swift Charts
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/primitiveplottableprotocol
source_url: 'https://developer.apple.com/documentation/charts/primitiveplottableprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/primitiveplottableprotocol.json'
content_hash: 'sha256:20db49d116f8a497'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# PrimitivePlottableProtocol

<sub>Protocol</sub>

A type that represents the primitive plottable types supported by the framework. Don’t use this type directly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol PrimitivePlottableProtocol : Plottable where Self == Self.PrimitivePlottable
```

## Overview

A primitive plottable type is a numeric type like a [Float](../swift/float.md) or [UInt32](../swift/uint32.md) for quantitative values, [Date](../foundation/date.md) for temporal values, or [String](../swift/string.md) for categorical values.

Primitive plottable types conform to the [Plottable](plottable.md) protocol.

## Relationships

- **Inherits From**: [Plottable](plottable.md)
