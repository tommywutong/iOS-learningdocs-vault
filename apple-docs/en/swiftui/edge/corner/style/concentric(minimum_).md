---
title: 'concentric(minimum:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/edge/corner/style/concentric(minimum:)'
source_url: 'https://developer.apple.com/documentation/swiftui/edge/corner/style/concentric(minimum:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/edge/corner/style/concentric%28minimum%3A%29.json'
content_hash: 'sha256:655d4582ab815123'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [SwiftUI](../../../../swiftui.md) · [Edge](../../../edge.md) · [Corner](../../corner.md) · [Style](../style.md)

# concentric(minimum:)

<sub>Type Method</sub>

A rounded corner style where the corner’s radius shares a center point with the container shape’s corner radius, with an optional minimum radius.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func concentric(minimum: Edge.Corner.Style? = nil) -> Edge.Corner.Style
```

## Discussion

When a corner is concentric to its container, the system calculates the corner radius to equal the container shape’s corner radius minus the distance between corners. If the radius that the system calculates is less than the minimum radius you provide, the system uses the minimum radius. When the system calculates a zero radius, the corner is square.
