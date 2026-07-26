---
title: 'radialGradient(colors:center:startRadius:endRadius:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/radialgradient(colors:center:startradius:endradius:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/radialgradient(colors:center:startradius:endradius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/radialgradient%28colors%3Acenter%3Astartradius%3Aendradius%3A%29.json'
content_hash: 'sha256:2feaeb63331372d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# radialGradient(colors:center:startRadius:endRadius:)

<sub>Type Method</sub>

A radial gradient defined by a collection of colors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func radialGradient(colors: [Color], center: UnitPoint, startRadius: CGFloat, endRadius: CGFloat) -> RadialGradient
```

## Discussion

The gradient applies the color function as the distance from a center point, scaled to fit within the defined start and end radii. The gradient maps the unit space center point into the bounding rectangle of each shape filled with the gradient.

For information about how to use shape styles, see [ShapeStyle](../shapestyle.md).

## See Also

### Radial gradients

- [radialGradient(_:center:startRadius:endRadius:)](<radialgradient(__center_startradius_endradius_).md>) — A radial gradient.
- [radialGradient(stops:center:startRadius:endRadius:)](<radialgradient(stops_center_startradius_endradius_).md>) — A radial gradient defined by a collection of color stops.
