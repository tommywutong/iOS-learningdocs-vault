---
title: 'init(position:leadingControlPoint:topControlPoint:trailingControlPoint:bottomControlPoint:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/meshgradient/bezierpoint/init(position:leadingcontrolpoint:topcontrolpoint:trailingcontrolpoint:bottomcontrolpoint:)'
source_url: 'https://developer.apple.com/documentation/swiftui/meshgradient/bezierpoint/init(position:leadingcontrolpoint:topcontrolpoint:trailingcontrolpoint:bottomcontrolpoint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/meshgradient/bezierpoint/init%28position%3Aleadingcontrolpoint%3Atopcontrolpoint%3Atrailingcontrolpoint%3Abottomcontrolpoint%3A%29.json'
content_hash: 'sha256:f73aa160240a9bb4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [MeshGradient](../../meshgradient.md) · [BezierPoint](../bezierpoint.md)

# init(position:leadingControlPoint:topControlPoint:trailingControlPoint:bottomControlPoint:)

<sub>Initializer</sub>

Creates a new vertex.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(position: SIMD2<Float>, leadingControlPoint: SIMD2<Float>, topControlPoint: SIMD2<Float>, trailingControlPoint: SIMD2<Float>, bottomControlPoint: SIMD2<Float>)
```

## Parameters

- `position` — The position of the vertex in the coordinate space the gradient is interpreted in.

- `leadingControlPoint` — The Bezier control point of the vertex’s leading edge.

- `topControlPoint` — The Bezier control point of the vertex’s top edge.

- `trailingControlPoint` — The Bezier control point of the vertex’s trailing edge.

- `bottomControlPoint` — The Bezier control point of the vertex’s bottom edge.
