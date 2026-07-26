---
title: 'conicGradient(_:center:angle:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/conicgradient(_:center:angle:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/conicgradient(_:center:angle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/conicgradient%28_%3Acenter%3Aangle%3A%29.json'
content_hash: 'sha256:56a57fcd64735768'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# conicGradient(_:center:angle:)

<sub>Type Method</sub>

A conic gradient that completes a full turn, optionally starting from a given angle and anchored to a relative center point within the filled shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func conicGradient(_ gradient: AnyGradient, center: UnitPoint = .center, angle: Angle = .zero) -> some ShapeStyle

```

## Parameters

- `gradient` — The gradient to use for filling the shape, providing the colors and their relative stop locations.

- `center` — The relative center of the gradient, mapped from the unit space into the bounding rectangle of the filled shape.

- `angle` — The angle to offset the beginning of the gradient’s full turn.

## Discussion

For example, a conic gradient used as a background:

```swift
let gradient = Gradient(colors: [.red, .yellow])

ContentView()
    .background(.conicGradient(gradient))
```

For information about how to use shape styles, see [ShapeStyle](../shapestyle.md).

## See Also

### Conic gradients

- [conicGradient(colors:center:angle:)](<conicgradient(colors_center_angle_).md>) — A conic gradient defined by a collection of colors that completes a full turn.
- [conicGradient(stops:center:angle:)](<conicgradient(stops_center_angle_).md>) — A conic gradient defined by a collection of color stops that completes a full turn.
