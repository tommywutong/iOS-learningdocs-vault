---
title: buttonBorder
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shape/buttonborder
source_url: 'https://developer.apple.com/documentation/swiftui/shape/buttonborder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/buttonborder.json'
content_hash: 'sha256:57df37813e6aac53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# buttonBorder

<sub>Type Property</sub>

A shape that defers to the environment to determine the resolved button border shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var buttonBorder: ButtonBorderShape { get }
```

## Discussion

You can override the resolved shape in a given view hierarchy by using the [buttonBorderShape(_:)](<../view/buttonbordershape(__).md>) modifier. If no button border shape is specified, it is resolved automatically for the given context and platform.

## See Also

### Getting standard shapes

- [capsule](capsule.md) — A capsule shape aligned inside the frame of the view containing it.
- [capsule(style:)](<capsule(style_).md>) — A capsule shape aligned inside the frame of the view containing it.
- [circle](circle.md) — A circle centered on the frame of the view containing it.
- [containerRelative](containerrelative.md) — A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
- [ellipse](ellipse.md) — An ellipse aligned inside the frame of the view containing it.
- [textInputBorder](textinputborder.md) — A shape that defers to the environment to determine the resolved text input border shape. _(beta)_
