---
title: 'stroke(_:lineWidth:antialiased:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/stroke(_:linewidth:antialiased:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/stroke(_:linewidth:antialiased:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/stroke%28_%3Alinewidth%3Aantialiased%3A%29.json'
content_hash: 'sha256:22f921e65b2f2107'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# stroke(_:lineWidth:antialiased:)

<sub>Instance Method</sub>

Traces the outline of this shape with a color or gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func stroke<S>(_ content: S, lineWidth: CGFloat = 1, antialiased: Bool = true) -> StrokeShapeView<Self, S, EmptyView> where S : ShapeStyle
```

## Parameters

- `content` — The color or gradient with which to stroke this shape.

- `lineWidth` — The width of the stroke that outlines this shape.

## Return Value

A stroked shape.

## Discussion

The following example draws a circle with a purple stroke:

```swift
Circle().stroke(Color.purple, lineWidth: 5)
```

## See Also

### Setting the stroke characteristics

- [stroke(_:lineWidth:)](<stroke(__linewidth_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(lineWidth:)](<stroke(linewidth_).md>) — Returns a new shape that is a stroked copy of `self` with line-width defined by `lineWidth` and all other properties of `StrokeStyle` having their default values.
- [stroke(_:style:)](<stroke(__style_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(_:style:antialiased:)](<stroke(__style_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(style:)](<stroke(style_).md>) — Returns a new shape that is a stroked copy of `self`, using the contents of `style` to define the stroke characteristics.
