---
title: 'linearGradient(_:startPoint:endPoint:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/lineargradient(_:startpoint:endpoint:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/lineargradient(_:startpoint:endpoint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/lineargradient%28_%3Astartpoint%3Aendpoint%3A%29.json'
content_hash: 'sha256:038d9eef802b6806'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# linearGradient(_:startPoint:endPoint:)

<sub>Type Method</sub>

A linear gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func linearGradient(_ gradient: AnyGradient, startPoint: UnitPoint, endPoint: UnitPoint) -> some ShapeStyle

```

## Discussion

The gradient applies the color function along an axis, as defined by its start and end points. The gradient maps the unit space points into the bounding rectangle of each shape filled with the gradient.

For example, a linear gradient used as a background:

```swift
ContentView()
    .background(.linearGradient(.red.gradient,
        startPoint: .top, endPoint: .bottom))
```

For information about how to use shape styles, see [ShapeStyle](../shapestyle.md).

## See Also

### Linear gradients

- [linearGradient(colors:startPoint:endPoint:)](<lineargradient(colors_startpoint_endpoint_).md>) — A linear gradient defined by a collection of colors.
- [linearGradient(stops:startPoint:endPoint:)](<lineargradient(stops_startpoint_endpoint_).md>) — A linear gradient defined by a collection of color stops.
