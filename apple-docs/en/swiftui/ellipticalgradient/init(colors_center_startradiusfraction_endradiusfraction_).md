---
title: 'init(colors:center:startRadiusFraction:endRadiusFraction:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/ellipticalgradient/init(colors:center:startradiusfraction:endradiusfraction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/ellipticalgradient/init(colors:center:startradiusfraction:endradiusfraction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/ellipticalgradient/init%28colors%3Acenter%3Astartradiusfraction%3Aendradiusfraction%3A%29.json'
content_hash: 'sha256:b1fee5d041316bfe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EllipticalGradient](../ellipticalgradient.md)

# init(colors:center:startRadiusFraction:endRadiusFraction:)

<sub>Initializer</sub>

Creates an elliptical gradient from a collection of colors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(colors: [Color], center: UnitPoint = .center, startRadiusFraction: CGFloat = 0, endRadiusFraction: CGFloat = 0.5)
```

## Discussion

For example, an elliptical gradient centered on the top-leading corner of the view:

```swift
EllipticalGradient(
    colors: [.blue, .green],
    center: .topLeading,
    startRadiusFraction: 0,
    endRadiusFraction: 1)
```

- colors: The colors, evenly distributed throughout the gradient.
- center: The center of the circle, in [0, 1] coordinates.
- startRadiusFraction: The start radius value, as a fraction between zero and one. Zero maps to the center point, one maps to the diameter of the unit circle.
- endRadiusFraction: The end radius value, as a fraction between zero and one. Zero maps to the center point, one maps to the diameter of the unit circle.

## See Also

### Creating an elliptical gradient

- [init(gradient:center:startRadiusFraction:endRadiusFraction:)](<init(gradient_center_startradiusfraction_endradiusfraction_).md>) — Creates an elliptical gradient.
- [init(stops:center:startRadiusFraction:endRadiusFraction:)](<init(stops_center_startradiusfraction_endradiusfraction_).md>) — Creates an elliptical gradient from a collection of color stops.
