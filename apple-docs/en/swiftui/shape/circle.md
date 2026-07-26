---
title: circle
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shape/circle
source_url: 'https://developer.apple.com/documentation/swiftui/shape/circle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/circle.json'
content_hash: 'sha256:2dc90fe3eda30ac5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# circle

<sub>Type Property</sub>

A circle centered on the frame of the view containing it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var circle: Circle { get }
```

## Discussion

The circle’s radius equals half the length of the frame rectangle’s smallest edge.

## See Also

### Getting standard shapes

- [buttonBorder](buttonborder.md) — A shape that defers to the environment to determine the resolved button border shape.
- [capsule](capsule.md) — A capsule shape aligned inside the frame of the view containing it.
- [capsule(style:)](<capsule(style_).md>) — A capsule shape aligned inside the frame of the view containing it.
- [containerRelative](containerrelative.md) — A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
- [ellipse](ellipse.md) — An ellipse aligned inside the frame of the view containing it.
- [textInputBorder](textinputborder.md) — A shape that defers to the environment to determine the resolved text input border shape. _(beta)_
