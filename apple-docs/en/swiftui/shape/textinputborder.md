---
title: textInputBorder
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/shape/textinputborder
source_url: 'https://developer.apple.com/documentation/swiftui/shape/textinputborder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/textinputborder.json'
content_hash: 'sha256:48ea9cd06df1b133'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# textInputBorder

<sub>Type Property</sub>

A shape that defers to the environment to determine the resolved text input border shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var textInputBorder: TextInputBorderShape { get }
```

## Discussion

You can override the resolved shape in a given view hierarchy by using the [textInputBorderShape(_:)](<../view/textinputbordershape(__).md>) modifier. If no text input border shape is specified, it is resolved automatically for the given context and platform.

## See Also

### Getting standard shapes

- [buttonBorder](buttonborder.md) — A shape that defers to the environment to determine the resolved button border shape.
- [capsule](capsule.md) — A capsule shape aligned inside the frame of the view containing it.
- [capsule(style:)](<capsule(style_).md>) — A capsule shape aligned inside the frame of the view containing it.
- [circle](circle.md) — A circle centered on the frame of the view containing it.
- [containerRelative](containerrelative.md) — A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
- [ellipse](ellipse.md) — An ellipse aligned inside the frame of the view containing it.
