---
title: 'linearGradient(colors:startPoint:endPoint:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/lineargradient(colors:startpoint:endpoint:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/lineargradient(colors:startpoint:endpoint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/lineargradient%28colors%3Astartpoint%3Aendpoint%3A%29.json'
content_hash: 'sha256:bccfb408add50b81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# linearGradient(colors:startPoint:endPoint:)

<sub>Type Method</sub>

A linear gradient defined by a collection of colors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func linearGradient(colors: [Color], startPoint: UnitPoint, endPoint: UnitPoint) -> LinearGradient
```

## Discussion

The gradient applies the color function along an axis, as defined by its start and end points. The gradient maps the unit space points into the bounding rectangle of each shape filled with the gradient.

For information about how to use shape styles, see [ShapeStyle](../shapestyle.md).

## See Also

### Linear gradients

- [linearGradient(_:startPoint:endPoint:)](<lineargradient(__startpoint_endpoint_).md>) — A linear gradient.
- [linearGradient(stops:startPoint:endPoint:)](<lineargradient(stops_startpoint_endpoint_).md>) — A linear gradient defined by a collection of color stops.
