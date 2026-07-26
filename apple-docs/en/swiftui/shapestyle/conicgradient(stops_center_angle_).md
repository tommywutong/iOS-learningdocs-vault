---
title: 'conicGradient(stops:center:angle:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/conicgradient(stops:center:angle:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/conicgradient(stops:center:angle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/conicgradient%28stops%3Acenter%3Aangle%3A%29.json'
content_hash: 'sha256:00a571c9f93b9e50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# conicGradient(stops:center:angle:)

<sub>Type Method</sub>

A conic gradient defined by a collection of color stops that completes a full turn.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func conicGradient(stops: [Gradient.Stop], center: UnitPoint, angle: Angle = .zero) -> AngularGradient
```

## Parameters

- `stops` — The color stops of the gradient, defining each component color and their relative location along the gradient’s full length.

- `center` — The relative center of the gradient, mapped from the unit space into the bounding rectangle of the filled shape.

- `angle` — The angle to offset the beginning of the gradient’s full turn.

## Discussion

For more information on how to use conic gradients, see [conicGradient(_:center:angle:)](<conicgradient(__center_angle_).md>).

## See Also

### Conic gradients

- [conicGradient(_:center:angle:)](<conicgradient(__center_angle_).md>) — A conic gradient that completes a full turn, optionally starting from a given angle and anchored to a relative center point within the filled shape.
- [conicGradient(colors:center:angle:)](<conicgradient(colors_center_angle_).md>) — A conic gradient defined by a collection of colors that completes a full turn.
