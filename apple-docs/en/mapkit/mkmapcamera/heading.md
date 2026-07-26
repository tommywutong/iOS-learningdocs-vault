---
title: heading
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapcamera/heading
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapcamera/heading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapcamera/heading.json'
content_hash: 'sha256:b30cbcc6ac88e3e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapCamera](../mkmapcamera.md)

# heading

<sub>Instance Property</sub>

The heading of the camera (in degrees) relative to true north.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var heading: CLLocationDirection { get set }
```

## Discussion

The value `0` means that the top edge of the map view corresponds to true north. The value `90` means the top of the map is pointing due east. The value `180` means the top of the map points due south, and so on.

## See Also

### Configuring the viewing angle

- [centerCoordinate](centercoordinate.md) — The map coordinate at the center of the map view.
- [centerCoordinateDistance](centercoordinatedistance.md) — The distance from the center point of the map to the camera, in meters.
- [pitch](pitch.md) — The viewing angle of the camera, in degrees.
- [altitude](altitude.md) — The altitude above the ground, in meters. _(deprecated)_
