---
title: MeshGradient.BezierPoint
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/meshgradient/bezierpoint
source_url: 'https://developer.apple.com/documentation/swiftui/meshgradient/bezierpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/meshgradient/bezierpoint.json'
content_hash: 'sha256:0af514907e90fa62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MeshGradient](../meshgradient.md)

# MeshGradient.BezierPoint

<sub>Structure</sub>

One location in a gradient mesh, along with the four Bezier control points surrounding it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct BezierPoint
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(position:leadingControlPoint:topControlPoint:trailingControlPoint:bottomControlPoint:)](<bezierpoint/init(position_leadingcontrolpoint_topcontrolpoint_trailingcontrolpoint_bottomcontrolpoint_).md>) — Creates a new vertex.

### Instance Properties

- [bottomControlPoint](bezierpoint/bottomcontrolpoint.md) — The Bezier control point of the vertex’s bottom edge.
- [leadingControlPoint](bezierpoint/leadingcontrolpoint.md) — The Bezier control point of the vertex’s leading edge.
- [position](bezierpoint/position.md) — The position of the vertex.
- [topControlPoint](bezierpoint/topcontrolpoint.md) — The Bezier control point of the vertex’s top edge.
- [trailingControlPoint](bezierpoint/trailingcontrolpoint.md) — The Bezier control point of the vertex’s trailing edge.
