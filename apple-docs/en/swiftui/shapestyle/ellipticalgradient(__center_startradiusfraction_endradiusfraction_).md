---
title: 'ellipticalGradient(_:center:startRadiusFraction:endRadiusFraction:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/ellipticalgradient(_:center:startradiusfraction:endradiusfraction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/ellipticalgradient(_:center:startradiusfraction:endradiusfraction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/ellipticalgradient%28_%3Acenter%3Astartradiusfraction%3Aendradiusfraction%3A%29.json'
content_hash: 'sha256:f91c34e97fd1b98a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# ellipticalGradient(_:center:startRadiusFraction:endRadiusFraction:)

<sub>Type Method</sub>

A radial gradient that draws an ellipse.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func ellipticalGradient(_ gradient: AnyGradient, center: UnitPoint = .center, startRadiusFraction: CGFloat = 0, endRadiusFraction: CGFloat = 0.5) -> some ShapeStyle

```

## Discussion

The gradient maps its coordinate space to the unit space square in which its center and radii are defined, then stretches that square to fill its bounding rect, possibly also stretching the circular gradient to have elliptical contours.

For example, an elliptical gradient used as a background:

```swift
ContentView()
    .background(.ellipticalGradient(.red.gradient))
```

For information about how to use shape styles, see [ShapeStyle](../shapestyle.md).

## See Also

### Elliptical gradients

- [ellipticalGradient(colors:center:startRadiusFraction:endRadiusFraction:)](<ellipticalgradient(colors_center_startradiusfraction_endradiusfraction_).md>) — A radial gradient that draws an ellipse defined by a collection of colors.
- [ellipticalGradient(stops:center:startRadiusFraction:endRadiusFraction:)](<ellipticalgradient(stops_center_startradiusfraction_endradiusfraction_).md>) — A radial gradient that draws an ellipse defined by a collection of color stops.
