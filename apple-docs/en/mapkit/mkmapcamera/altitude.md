---
title: altitude
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.9+（27.0 起废弃）, tvOS 9.2+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkmapcamera/altitude
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapcamera/altitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapcamera/altitude.json'
content_hash: 'sha256:6769a61eb4e28209'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapCamera](../mkmapcamera.md)

# altitude

<sub>Instance Property</sub>

The altitude above the ground, in meters.

> [!warning] Deprecated
> Use [centerCoordinateDistance](centercoordinatedistance.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var altitude: CLLocationDistance { get set }
```

## Discussion

The value you specify for this property can’t be less than `0`.

Changing this property may also change the maximum pitch for the map. If the current pitch value exceeds the new maximum, the class clamps the [pitch](pitch.md) property to the new maximum.

## See Also

### Configuring the viewing angle

- [centerCoordinate](centercoordinate.md) — The map coordinate at the center of the map view.
- [heading](heading.md) — The heading of the camera (in degrees) relative to true north.
- [centerCoordinateDistance](centercoordinatedistance.md) — The distance from the center point of the map to the camera, in meters.
- [pitch](pitch.md) — The viewing angle of the camera, in degrees.
