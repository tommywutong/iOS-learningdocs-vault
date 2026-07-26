---
title: 'stroke(_:lineWidth:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/stroke(_:linewidth:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/stroke(_:linewidth:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/stroke%28_%3Alinewidth%3A%29.json'
content_hash: 'sha256:605b31266814b489'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# stroke(_:lineWidth:)

<sub>Instance Method</sub>

Traces the outline of this shape with a color or gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func stroke<S>(_ content: S, lineWidth: CGFloat = 1) -> some View where S : ShapeStyle

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

- [stroke(_:lineWidth:antialiased:)](<stroke(__linewidth_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(lineWidth:)](<stroke(linewidth_).md>) — Returns a new shape that is a stroked copy of `self` with line-width defined by `lineWidth` and all other properties of `StrokeStyle` having their default values.
- [stroke(_:style:)](<stroke(__style_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(_:style:antialiased:)](<stroke(__style_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(style:)](<stroke(style_).md>) — Returns a new shape that is a stroked copy of `self`, using the contents of `style` to define the stroke characteristics.
