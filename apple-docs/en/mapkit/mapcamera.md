---
title: MapCamera
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapcamera
source_url: 'https://developer.apple.com/documentation/mapkit/mapcamera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcamera.json'
content_hash: 'sha256:43242d63291d1e44'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapCamera

<sub>Structure</sub>

Defines a virtual viewpoint above the map surface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapCamera
```

## Overview

`MapCamera` allows you to specify the viewpoint of a [Map](map.md), as well as affect how MapKit presents the map to the user.

To create a map view with a 3D perspective, `MapCamera` takes input from the camera and device:

- The location of the camera on the map.
- The compass heading to indicate the camera’s viewing direction.
- The pitch of the camera relative to the map perpendicular.
- The camera’s distance from the target point.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Creating a map camera

- [init(_:)](<mapcamera/init(__).md>) — Creates a map camera from the given MapKit camera object.
- [init(centerCoordinate:distance:heading:pitch:)](<mapcamera/init(centercoordinate_distance_heading_pitch_).md>) — Creates a camera using the specified distance, pitch, and heading information.

### Accessing the camera properties

- [centerCoordinate](mapcamera/centercoordinate.md) — The map coordinate at the center of the map view.
- [distance](mapcamera/distance.md) — The distance from the center point of the map to the camera, in meters.
- [heading](mapcamera/heading.md) — The heading of the camera, in degrees, relative to true North.
- [pitch](mapcamera/pitch.md) — The viewing angle of the camera, in degrees.

## See Also

### Map customization

- [MapCameraBounds](mapcamerabounds.md) — Defines an optional boundary of an area within which the map’s center needs to remain.
- [MapCameraPosition](mapcameraposition.md) — A structure that describes how to position the map’s camera within the map.
- [MapCameraUpdateContext](mapcameraupdatecontext.md) — A structure that defines additional information about the map camera.
- [MapCameraUpdateFrequency](mapcameraupdatefrequency.md) — A structure that describes when the map camera updates.
