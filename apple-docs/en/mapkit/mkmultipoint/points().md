---
title: points()
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmultipoint/points()
source_url: 'https://developer.apple.com/documentation/mapkit/mkmultipoint/points()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmultipoint/points%28%29.json'
content_hash: 'sha256:6957070721a14368'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMultiPoint](../mkmultipoint.md)

# points()

<sub>Instance Method</sub>

Returns an array of map points associated with the shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func points() -> UnsafeMutablePointer<MKMapPoint>
```

## Return Value

An unsafe mutable array of [MKMapPoint](../mkmappoint.md) structures.

## Discussion

The [pointCount](pointcount.md) property specifies the number of points in the array.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Accessing the points in the shape

- [pointCount](pointcount.md) — The number of points associated with the shape.
- [- locationAtPointIndex:](<location(atpointindex_).md>) — Translates a point index into a unit distance along the shape.
- [locations(at:)](<locations(at_).md>) — Translates a point index set into a unit distance along the shape.
