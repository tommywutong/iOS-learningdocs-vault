---
title: 'init(coordinate:anchorPoint:content:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（17.0 起废弃）, iPadOS 14.0+（17.0 起废弃）, Mac Catalyst 14.0+（17.0 起废弃）, macOS 11.0+（14.0 起废弃）, tvOS 14.0+（17.0 起废弃）, visionOS, watchOS 7.0+（10.0 起废弃）]
languages: [swift, swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mapannotation/init(coordinate:anchorpoint:content:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapannotation/init(coordinate:anchorpoint:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapannotation/init%28coordinate%3Aanchorpoint%3Acontent%3A%29.json'
content_hash: 'sha256:0f155a00a584aca9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapAnnotation](../mapannotation.md)

# init(coordinate:anchorPoint:content:)

<sub>Initializer</sub>

Creates a custom annotation that provides a SwiftUI view to display at the map location that you specify.

> [!warning] Deprecated
> Use Annotation along with Map initializers that take a MapContentBuilder instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(coordinate: CLLocationCoordinate2D, anchorPoint: CGPoint = CGPoint(x: 0.5, y: 0.5), @ViewBuilder content: () -> Content)
```

## Parameters

- `coordinate` — The location of the specified annotation.

- `anchorPoint` — A [CGPoint](../../corefoundation/cgpoint.md) value in unit coordinate space that aligns the coordinate location of the annotation with view created. The default value `0.5`, which represents the center of the view.

- `content` — The closure that returns a custom annotation view.

## Discussion

Use the anchor point to align the SwiftUI view you return in content to the coordinate represented on the map. Anchor point uses unit coordinate space, that represents the distance between the frame edges as values between `0` and `1`. For example, to align the top-right or bottom-middle of the view with the coordinate location on the map use `CGPoint(1,0)` or `CGPoint(0.5,1)`, respectively.
