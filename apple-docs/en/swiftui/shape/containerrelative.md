---
title: containerRelative
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shape/containerrelative
source_url: 'https://developer.apple.com/documentation/swiftui/shape/containerrelative'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/containerrelative.json'
content_hash: 'sha256:cb78a8166f25f7ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# containerRelative

<sub>Type Property</sub>

A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var containerRelative: ContainerRelativeShape { get }
```

## See Also

### Getting standard shapes

- [buttonBorder](buttonborder.md) — A shape that defers to the environment to determine the resolved button border shape.
- [capsule](capsule.md) — A capsule shape aligned inside the frame of the view containing it.
- [capsule(style:)](<capsule(style_).md>) — A capsule shape aligned inside the frame of the view containing it.
- [circle](circle.md) — A circle centered on the frame of the view containing it.
- [ellipse](ellipse.md) — An ellipse aligned inside the frame of the view containing it.
- [textInputBorder](textinputborder.md) — A shape that defers to the environment to determine the resolved text input border shape. _(beta)_
