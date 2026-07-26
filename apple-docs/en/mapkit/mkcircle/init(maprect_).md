---
title: 'init(mapRect:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkcircle/init(maprect:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkcircle/init(maprect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcircle/init%28maprect%3A%29.json'
content_hash: 'sha256:4be0b1e82acc7f5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCircle](../mkcircle.md)

# init(mapRect:)

<sub>Initializer</sub>

Creates and returns a circle object that derives the circular area from the specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(mapRect: MKMapRect)
```

## Parameters

- `mapRect` — The map rectangle that determines the circular area. The initializer uses the center point of the rectangle as the center point of the circle. If the rectangle isn’t a square, the method uses the longest side of the rectangle to define the radius of the resulting circle.

## Return Value

A circle overlay object.

## See Also

### Creating a circle overlay

- [+ circleWithCenterCoordinate:radius:](<init(center_radius_).md>) — Creates and returns a circle object using the specified coordinate and radius.
