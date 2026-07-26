---
title: 'strokeBorder(_:style:antialiased:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapeview/strokeborder(_:style:antialiased:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapeview/strokeborder(_:style:antialiased:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapeview/strokeborder%28_%3Astyle%3Aantialiased%3A%29.json'
content_hash: 'sha256:26d35e26ea4ed7d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeView](../shapeview.md)

# strokeBorder(_:style:antialiased:)

<sub>Instance Method</sub>

Returns a view that’s the result of insetting this view by half of its style’s line width.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func strokeBorder<S>(_ content: S = .foreground, style: StrokeStyle, antialiased: Bool = true) -> StrokeBorderShapeView<Self.Content, S, Self> where S : ShapeStyle
```

## Discussion

This method strokes the resulting shape with `style` and fills it with `content`.

## See Also

### Modify the shape

- [fill(_:style:)](<fill(__style_).md>) — Fills this shape with a color or gradient.
- [stroke(_:style:antialiased:)](<stroke(__style_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(_:lineWidth:antialiased:)](<stroke(__linewidth_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [strokeBorder(_:lineWidth:antialiased:)](<strokeborder(__linewidth_antialiased_).md>) — Returns a view that’s the result of filling an inner stroke of this view with the content you supply.
