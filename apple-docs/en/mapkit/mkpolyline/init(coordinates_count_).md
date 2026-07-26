---
title: 'init(coordinates:count:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkpolyline/init(coordinates:count:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolyline/init(coordinates:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolyline/init%28coordinates%3Acount%3A%29.json'
content_hash: 'sha256:594300adafaad668'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPolyline](../mkpolyline.md)

# init(coordinates:count:)

<sub>Initializer</sub>

Creates a polyline object from the specified set of coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(coordinates coords: UnsafePointer<CLLocationCoordinate2D>, count: Int)
```

## Parameters

- `coords` — The array of coordinates defining the shape. The initializer copies the data in this array to the new object.

- `count` — The number of items in the `coords` array.

## Return Value

A new polyline object.

## See Also

### Creating a polyline overlay

- [+ polylineWithPoints:count:](<init(points_count_).md>) — Creates a polyline object from the specified set of map points.
