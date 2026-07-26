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
doc_path: '/documentation/swiftui/shapeview/fill(_:style:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapeview/fill(_:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapeview/fill%28_%3Astyle%3A%29.json'
content_hash: 'sha256:818ed46c0875292c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeView](../shapeview.md)

# fill(_:style:)

<sub>Instance Method</sub>

Fills this shape with a color or gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func fill<S>(_ content: S = .foreground, style: FillStyle = FillStyle()) -> FillShapeView<Self.Content, S, Self> where S : ShapeStyle
```

## Parameters

- `content` — The color or gradient to use when filling this shape.

- `style` — The style options that determine how the fill renders.

## Return Value

A shape filled with the color or gradient you supply.

## See Also

### Modify the shape

- [stroke(_:style:antialiased:)](<stroke(__style_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(_:lineWidth:antialiased:)](<stroke(__linewidth_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [strokeBorder(_:style:antialiased:)](<strokeborder(__style_antialiased_).md>) — Returns a view that’s the result of insetting this view by half of its style’s line width.
- [strokeBorder(_:lineWidth:antialiased:)](<strokeborder(__linewidth_antialiased_).md>) — Returns a view that’s the result of filling an inner stroke of this view with the content you supply.
