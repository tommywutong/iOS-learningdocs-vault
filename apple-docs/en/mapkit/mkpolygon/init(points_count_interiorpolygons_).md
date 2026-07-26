---
title: 'init(points:count:interiorPolygons:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkpolygon/init(points:count:interiorpolygons:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolygon/init(points:count:interiorpolygons:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolygon/init%28points%3Acount%3Ainteriorpolygons%3A%29.json'
content_hash: 'sha256:9418f966d93de5b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPolygon](../mkpolygon.md)

# init(points:count:interiorPolygons:)

<sub>Initializer</sub>

Creates and returns a polygon object from the specified set of map points and interior polygons.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(points: UnsafePointer<MKMapPoint>, count: Int, interiorPolygons: [MKPolygon]?)
```

## Parameters

- `points` — The array of map points defining the shape. The new object copy the data in this array.

- `count` — The number of items in the `points` array.

- `interiorPolygons` — An array of `MKPolygon` objects that define one or more cutout regions for the receiver’s polygon.

## Return Value

A new polygon object.

## See Also

### Creating a polygon overlay

- [+ polygonWithPoints:count:](<init(points_count_).md>) — Creates and returns a polygon object from the specified set of map points.
- [+ polygonWithCoordinates:count:](<init(coordinates_count_).md>) — Creates and returns a polygon object from the specified set of coordinates.
- [+ polygonWithCoordinates:count:interiorPolygons:](<init(coordinates_count_interiorpolygons_).md>) — Creates and returns a polygon object from the specified set of coordinates and interior polygons.
