---
title: latitudeDelta
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkcoordinatespan/latitudedelta
source_url: 'https://developer.apple.com/documentation/mapkit/mkcoordinatespan/latitudedelta'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcoordinatespan/latitudedelta.json'
content_hash: 'sha256:2e9f043c4292668a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCoordinateSpan](../mkcoordinatespan.md)

# latitudeDelta

<sub>Instance Property</sub>

The amount of north-to-south distance (measured in degrees) to display on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var latitudeDelta: CLLocationDegrees
```

## Discussion

Unlike longitudinal distances, which vary based on the latitude, one degree of latitude is always approximately 111 kilometers (69 miles).

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Getting the span coordinates

- [longitudeDelta](longitudedelta.md) — The amount of east-to-west distance (measured in degrees) to display for the map region.
