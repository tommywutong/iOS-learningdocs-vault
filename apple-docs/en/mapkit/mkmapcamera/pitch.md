---
title: pitch
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapcamera/pitch
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapcamera/pitch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapcamera/pitch.json'
content_hash: 'sha256:48934878e60923ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapCamera](../mkmapcamera.md)

# pitch

<sub>Instance Property</sub>

The viewing angle of the camera, in degrees.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var pitch: CGFloat { get set }
```

## Discussion

A value of `0` results in a camera that points straight down at the map. Angles greater than `0` result in a camera that pitches toward the horizon by the specified number of degrees. If the map type is [MKMapTypeSatellite](../mkmaptype/satellite.md) or [MKMapTypeHybrid](../mkmaptype/hybrid.md), the object clamps the pitch value to `0`.

The class may clamp the value in this property to a maximum value to maintain map readability. There’s no fixed maximum value, though, because the actual maximum value is dependent on the altitude of the camera.

## See Also

### Configuring the viewing angle

- [centerCoordinate](centercoordinate.md) — The map coordinate at the center of the map view.
- [heading](heading.md) — The heading of the camera (in degrees) relative to true north.
- [centerCoordinateDistance](centercoordinatedistance.md) — The distance from the center point of the map to the camera, in meters.
- [altitude](altitude.md) — The altitude above the ground, in meters. _(deprecated)_
