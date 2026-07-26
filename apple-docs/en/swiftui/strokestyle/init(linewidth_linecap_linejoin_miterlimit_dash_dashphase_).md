---
title: 'init(lineWidth:lineCap:lineJoin:miterLimit:dash:dashPhase:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/strokestyle/init(linewidth:linecap:linejoin:miterlimit:dash:dashphase:)'
source_url: 'https://developer.apple.com/documentation/swiftui/strokestyle/init(linewidth:linecap:linejoin:miterlimit:dash:dashphase:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/strokestyle/init%28linewidth%3Alinecap%3Alinejoin%3Amiterlimit%3Adash%3Adashphase%3A%29.json'
content_hash: 'sha256:c0e9854cb6d42270'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [StrokeStyle](../strokestyle.md)

# init(lineWidth:lineCap:lineJoin:miterLimit:dash:dashPhase:)

<sub>Initializer</sub>

Creates a new stroke style from the given components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(lineWidth: CGFloat = 1, lineCap: CGLineCap = .butt, lineJoin: CGLineJoin = .miter, miterLimit: CGFloat = 10, dash: [CGFloat] = [CGFloat](), dashPhase: CGFloat = 0)
```

## Parameters

- `lineWidth` — The width of the segment.

- `lineCap` — The endpoint style of a segment.

- `lineJoin` — The join type of a segment.

- `miterLimit` — The threshold used to determine whether to use a bevel instead of a miter at a join.

- `dash` — The lengths of painted and unpainted segments used to make a dashed line.

- `dashPhase` — How far into the dash pattern the line starts.
