---
title: 'init(points:count:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkpolyline/init(points:count:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolyline/init(points:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolyline/init%28points%3Acount%3A%29.json'
content_hash: 'sha256:51a70fe2626a1ac9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPolyline](../mkpolyline.md)

# init(points:count:)

<sub>Initializer</sub>

Creates a polyline object from the specified set of map points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(points: UnsafePointer<MKMapPoint>, count: Int)
```

## Parameters

- `points` — The array of map points defining the shape. The initializer copies the data in this array to the new object.

- `count` — The number of items in the `points` array.

## Return Value

A new polyline object.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Creating a polyline overlay

- [+ polylineWithCoordinates:count:](<init(coordinates_count_).md>) — Creates a polyline object from the specified set of coordinates.
