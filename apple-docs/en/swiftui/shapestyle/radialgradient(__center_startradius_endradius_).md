---
title: 'radialGradient(_:center:startRadius:endRadius:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/radialgradient(_:center:startradius:endradius:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/radialgradient(_:center:startradius:endradius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/radialgradient%28_%3Acenter%3Astartradius%3Aendradius%3A%29.json'
content_hash: 'sha256:3d20678813dc4c1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# radialGradient(_:center:startRadius:endRadius:)

<sub>Type Method</sub>

A radial gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func radialGradient(_ gradient: AnyGradient, center: UnitPoint = .center, startRadius: CGFloat = 0, endRadius: CGFloat) -> some ShapeStyle

```

## Discussion

The gradient applies the color function as the distance from a center point, scaled to fit within the defined start and end radii. The gradient maps the unit space center point into the bounding rectangle of each shape filled with the gradient.

For example, a radial gradient used as a background:

```swift
ContentView()
    .background(.radialGradient(.red.gradient, endRadius: 100))
```

For information about how to use shape styles, see [ShapeStyle](../shapestyle.md).

## See Also

### Radial gradients

- [radialGradient(colors:center:startRadius:endRadius:)](<radialgradient(colors_center_startradius_endradius_).md>) — A radial gradient defined by a collection of colors.
- [radialGradient(stops:center:startRadius:endRadius:)](<radialgradient(stops_center_startradius_endradius_).md>) — A radial gradient defined by a collection of color stops.
