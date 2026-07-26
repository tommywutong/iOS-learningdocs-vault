---
title: 'init(points:count:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkgeodesicpolyline/init(points:count:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeodesicpolyline/init(points:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeodesicpolyline/init%28points%3Acount%3A%29.json'
content_hash: 'sha256:4449c416c214cb85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGeodesicPolyline](../mkgeodesicpolyline.md)

# init(points:count:)

<sub>Initializer</sub>

Creates and returns a geodesic polyline using the specified map points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(points: UnsafePointer<MKMapPoint>, count: Int)
```

## Parameters

- `points` — A pointer to the array of map points that define the path.

- `count` — The number of items in the `points` array.

## Return Value

A new geodesic polyline object.

## See Also

### Creating a geodesic polyline overlay

- [+ polylineWithCoordinates:count:](<init(coordinates_count_).md>) — Creates and returns a geodesic polyline using the specified coordinates.
