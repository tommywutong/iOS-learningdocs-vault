---
title: 'stroke(_:style:antialiased:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapeview/stroke(_:style:antialiased:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapeview/stroke(_:style:antialiased:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapeview/stroke%28_%3Astyle%3Aantialiased%3A%29.json'
content_hash: 'sha256:fdfee3331d6541ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeView](../shapeview.md)

# stroke(_:style:antialiased:)

<sub>Instance Method</sub>

Traces the outline of this shape with a color or gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func stroke<S>(_ content: S, style: StrokeStyle, antialiased: Bool = true) -> StrokeShapeView<Self.Content, S, Self> where S : ShapeStyle
```

## Parameters

- `content` — The color or gradient with which to stroke this shape.

- `style` — The stroke characteristics — such as the line’s width and whether the stroke is dashed — that determine how to render this shape.

## Return Value

A stroked shape.

## Discussion

The following example adds a dashed purple stroke to a `Capsule`:

```swift
Capsule()
.stroke(
    Color.purple,
    style: StrokeStyle(
        lineWidth: 5,
        lineCap: .round,
        lineJoin: .miter,
        miterLimit: 0,
        dash: [5, 10],
        dashPhase: 0
    )
)
```

## See Also

### Modify the shape

- [fill(_:style:)](<fill(__style_).md>) — Fills this shape with a color or gradient.
- [stroke(_:lineWidth:antialiased:)](<stroke(__linewidth_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [strokeBorder(_:style:antialiased:)](<strokeborder(__style_antialiased_).md>) — Returns a view that’s the result of insetting this view by half of its style’s line width.
- [strokeBorder(_:lineWidth:antialiased:)](<strokeborder(__linewidth_antialiased_).md>) — Returns a view that’s the result of filling an inner stroke of this view with the content you supply.
