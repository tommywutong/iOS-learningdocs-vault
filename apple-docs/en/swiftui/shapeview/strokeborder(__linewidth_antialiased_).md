---
title: 'strokeBorder(_:lineWidth:antialiased:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapeview/strokeborder(_:linewidth:antialiased:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapeview/strokeborder(_:linewidth:antialiased:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapeview/strokeborder%28_%3Alinewidth%3Aantialiased%3A%29.json'
content_hash: 'sha256:cf53f0e02bae2456'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeView](../shapeview.md)

# strokeBorder(_:lineWidth:antialiased:)

<sub>Instance Method</sub>

Returns a view that’s the result of filling an inner stroke of this view with the content you supply.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func strokeBorder<S>(_ content: S = .foreground, lineWidth: CGFloat = 1, antialiased: Bool = true) -> StrokeBorderShapeView<Self.Content, S, Self> where S : ShapeStyle
```

## Discussion

This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.

## See Also

### Modify the shape

- [fill(_:style:)](<fill(__style_).md>) — Fills this shape with a color or gradient.
- [stroke(_:style:antialiased:)](<stroke(__style_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(_:lineWidth:antialiased:)](<stroke(__linewidth_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [strokeBorder(_:style:antialiased:)](<strokeborder(__style_antialiased_).md>) — Returns a view that’s the result of insetting this view by half of its style’s line width.
