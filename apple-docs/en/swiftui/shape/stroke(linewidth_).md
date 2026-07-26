---
title: 'stroke(lineWidth:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/stroke(linewidth:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/stroke(linewidth:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/stroke%28linewidth%3A%29.json'
content_hash: 'sha256:c6ce6523298f6c72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# stroke(lineWidth:)

<sub>Instance Method</sub>

Returns a new shape that is a stroked copy of `self` with line-width defined by `lineWidth` and all other properties of `StrokeStyle` having their default values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func stroke(lineWidth: CGFloat = 1) -> some Shape

```

## See Also

### Setting the stroke characteristics

- [stroke(_:lineWidth:)](<stroke(__linewidth_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(_:lineWidth:antialiased:)](<stroke(__linewidth_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(_:style:)](<stroke(__style_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(_:style:antialiased:)](<stroke(__style_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(style:)](<stroke(style_).md>) — Returns a new shape that is a stroked copy of `self`, using the contents of `style` to define the stroke characteristics.
