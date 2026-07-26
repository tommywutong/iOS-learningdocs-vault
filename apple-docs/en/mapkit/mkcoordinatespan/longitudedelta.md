---
title: longitudeDelta
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkcoordinatespan/longitudedelta
source_url: 'https://developer.apple.com/documentation/mapkit/mkcoordinatespan/longitudedelta'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcoordinatespan/longitudedelta.json'
content_hash: 'sha256:864d63ddbbab8ce9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCoordinateSpan](../mkcoordinatespan.md)

# longitudeDelta

<sub>Instance Property</sub>

The amount of east-to-west distance (measured in degrees) to display for the map region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var longitudeDelta: CLLocationDegrees
```

## Discussion

The number of kilometers spanned by a longitude range varies based on the current latitude. For example, one degree of longitude spans a distance of approximately 111 kilometers (69 miles) at the equator but shrinks to 0 kilometers at the poles.

## See Also

### Getting the span coordinates

- [latitudeDelta](latitudedelta.md) — The amount of north-to-south distance (measured in degrees) to display on the map.
