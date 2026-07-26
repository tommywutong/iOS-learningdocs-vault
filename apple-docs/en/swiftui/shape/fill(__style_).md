---
title: 'fill(_:style:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/fill(_:style:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/fill(_:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/fill%28_%3Astyle%3A%29.json'
content_hash: 'sha256:3a152139952525c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# fill(_:style:)

<sub>Instance Method</sub>

Fills this shape with a color or gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func fill<S>(_ content: S = .foreground, style: FillStyle = FillStyle()) -> _ShapeView<Self, S> where S : ShapeStyle
```

## Parameters

- `content` — The color or gradient to use when filling this shape.

- `style` — The style options that determine how the fill renders.

## Return Value

A shape filled with the color or gradient you supply.

## See Also

### Filling a shape

- [fill(style:)](<fill(style_).md>) — Fills this shape with the foreground color.
