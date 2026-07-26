---
title: 'angularGradient(colors:center:startAngle:endAngle:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/angulargradient(colors:center:startangle:endangle:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/angulargradient(colors:center:startangle:endangle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/angulargradient%28colors%3Acenter%3Astartangle%3Aendangle%3A%29.json'
content_hash: 'sha256:0b38f2688ad0d00a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# angularGradient(colors:center:startAngle:endAngle:)

<sub>Type Method</sub>

An angular gradient defined by a collection of colors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func angularGradient(colors: [Color], center: UnitPoint, startAngle: Angle, endAngle: Angle) -> AngularGradient
```

## Parameters

- `colors` — The colors of the gradient, evenly spaced along its full length.

- `center` — The relative center of the gradient, mapped from the unit space into the bounding rectangle of the filled shape.

- `startAngle` — The angle that marks the beginning of the gradient.

- `endAngle` — The angle that marks the end of the gradient.

## Discussion

For more information on how to use angular gradients, see [angularGradient(_:center:startAngle:endAngle:)](<angulargradient(__center_startangle_endangle_).md>).

## See Also

### Angular gradients

- [angularGradient(_:center:startAngle:endAngle:)](<angulargradient(__center_startangle_endangle_).md>) — An angular gradient, which applies the color function as the angle changes between the start and end angles, and anchored to a relative center point within the filled shape.
- [angularGradient(stops:center:startAngle:endAngle:)](<angulargradient(stops_center_startangle_endangle_).md>) — An angular gradient defined by a collection of color stops.
