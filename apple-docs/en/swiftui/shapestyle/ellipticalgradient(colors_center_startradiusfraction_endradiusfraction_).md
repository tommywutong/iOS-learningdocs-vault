---
title: 'ellipticalGradient(colors:center:startRadiusFraction:endRadiusFraction:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/ellipticalgradient(colors:center:startradiusfraction:endradiusfraction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/ellipticalgradient(colors:center:startradiusfraction:endradiusfraction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/ellipticalgradient%28colors%3Acenter%3Astartradiusfraction%3Aendradiusfraction%3A%29.json'
content_hash: 'sha256:2669bb0a3735e004'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# ellipticalGradient(colors:center:startRadiusFraction:endRadiusFraction:)

<sub>Type Method</sub>

A radial gradient that draws an ellipse defined by a collection of colors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func ellipticalGradient(colors: [Color], center: UnitPoint = .center, startRadiusFraction: CGFloat = 0, endRadiusFraction: CGFloat = 0.5) -> EllipticalGradient
```

## Discussion

The gradient maps its coordinate space to the unit space square in which its center and radii are defined, then stretches that square to fill its bounding rect, possibly also stretching the circular gradient to have elliptical contours.

For example, an elliptical gradient used as a background:

```swift
.background(.elliptical(colors: [.red, .yellow]))
```

For information about how to use shape styles, see [ShapeStyle](../shapestyle.md).

## See Also

### Elliptical gradients

- [ellipticalGradient(_:center:startRadiusFraction:endRadiusFraction:)](<ellipticalgradient(__center_startradiusfraction_endradiusfraction_).md>) — A radial gradient that draws an ellipse.
- [ellipticalGradient(stops:center:startRadiusFraction:endRadiusFraction:)](<ellipticalgradient(stops_center_startradiusfraction_endradiusfraction_).md>) — A radial gradient that draws an ellipse defined by a collection of color stops.
