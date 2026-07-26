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
doc_path: '/documentation/swiftui/insettableshape/strokeborder(_:linewidth:antialiased:)'
source_url: 'https://developer.apple.com/documentation/swiftui/insettableshape/strokeborder(_:linewidth:antialiased:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/insettableshape/strokeborder%28_%3Alinewidth%3Aantialiased%3A%29.json'
content_hash: 'sha256:3c3fbf56b4293891'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [InsettableShape](../insettableshape.md)

# strokeBorder(_:lineWidth:antialiased:)

<sub>Instance Method</sub>

Returns a view that is the result of filling the `lineWidth`-sized border (aka inner stroke) of `self` with `content`. This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func strokeBorder<S>(_ content: S = .foreground, lineWidth: CGFloat = 1, antialiased: Bool = true) -> StrokeBorderShapeView<Self, S, EmptyView> where S : ShapeStyle
```

## See Also

### Setting the stroke border characteristics

- [strokeBorder(lineWidth:antialiased:)](<strokeborder(linewidth_antialiased_).md>) — Returns a view that is the result of filling the `lineWidth`-sized border (aka inner stroke) of `self` with the foreground color. This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.
- [strokeBorder(_:style:antialiased:)](<strokeborder(__style_antialiased_).md>) — Returns a view that is the result of insetting `self` by `style.lineWidth / 2`, stroking the resulting shape with `style`, and then filling with `content`.
- [strokeBorder(style:antialiased:)](<strokeborder(style_antialiased_).md>) — Returns a view that is the result of insetting `self` by `style.lineWidth / 2`, stroking the resulting shape with `style`, and then filling with the foreground color.
