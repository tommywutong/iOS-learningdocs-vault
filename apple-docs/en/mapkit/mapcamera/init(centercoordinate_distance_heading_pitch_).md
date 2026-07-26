---
title: 'init(centerCoordinate:distance:heading:pitch:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcamera/init(centercoordinate:distance:heading:pitch:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcamera/init(centercoordinate:distance:heading:pitch:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcamera/init%28centercoordinate%3Adistance%3Aheading%3Apitch%3A%29.json'
content_hash: 'sha256:6a2564f7a73dd3a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapCamera](../mapcamera.md)

# init(centerCoordinate:distance:heading:pitch:)

<sub>Initializer</sub>

Creates a camera using the specified distance, pitch, and heading information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(centerCoordinate: CLLocationCoordinate2D, distance: Double, heading: Double = 0, pitch: Double = 0)
```

## Parameters

- `centerCoordinate` — The map coordinate at the center of the map view.

- `distance` — The distance from the center point of the map to the camera, in meters.

- `heading` — The heading of the camera, in degrees, relative to true North.

- `pitch` — The viewing angle of the camera, in degrees.

## See Also

### Creating a map camera

- [init(_:)](<init(__).md>) — Creates a map camera from the given MapKit camera object.
