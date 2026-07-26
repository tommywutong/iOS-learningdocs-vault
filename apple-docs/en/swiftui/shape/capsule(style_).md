---
title: 'capsule(style:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/capsule(style:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/capsule(style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/capsule%28style%3A%29.json'
content_hash: 'sha256:654842a2fbe5ecfa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# capsule(style:)

<sub>Type Method</sub>

A capsule shape aligned inside the frame of the view containing it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func capsule(style: RoundedCornerStyle) -> Self
```

## Discussion

A capsule shape is equivalent to a rounded rectangle where the corner radius is chosen as half the length of the rectangle’s smallest edge.

## See Also

### Getting standard shapes

- [buttonBorder](buttonborder.md) — A shape that defers to the environment to determine the resolved button border shape.
- [capsule](capsule.md) — A capsule shape aligned inside the frame of the view containing it.
- [circle](circle.md) — A circle centered on the frame of the view containing it.
- [containerRelative](containerrelative.md) — A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
- [ellipse](ellipse.md) — An ellipse aligned inside the frame of the view containing it.
- [textInputBorder](textinputborder.md) — A shape that defers to the environment to determine the resolved text input border shape. _(beta)_
