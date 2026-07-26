---
title: concentric
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/edge/corner/style/concentric
source_url: 'https://developer.apple.com/documentation/swiftui/edge/corner/style/concentric'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/edge/corner/style/concentric.json'
content_hash: 'sha256:c0bd4c8d9e2d303c'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [SwiftUI](../../../../swiftui.md) · [Edge](../../../edge.md) · [Corner](../../corner.md) · [Style](../style.md)

# concentric

<sub>Type Property</sub>

A rounded corner style where the corner’s radius shares a center point with the container shape’s corner radius.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var concentric: Edge.Corner.Style { get }
```

## Discussion

When a corner is concentric to its container, the system calculates the corner radius to equal the container shape’s corner radius minus the distance between corners. When the system calculates a zero radius, the corner is square.
