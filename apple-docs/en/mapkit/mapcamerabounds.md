---
title: MapCameraBounds
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapcamerabounds
source_url: 'https://developer.apple.com/documentation/mapkit/mapcamerabounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcamerabounds.json'
content_hash: 'sha256:d984b3400a9a8ce3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapCameraBounds

<sub>Structure</sub>

Defines an optional boundary of an area within which the map’s center needs to remain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapCameraBounds
```

## Overview

Using the `MapCameraBounds` initializers you can also define an optional camera zoom range that limits the distances that a person can zoom the map camera to.

## Topics

### Creating a map camera bounds

- [init(centerCoordinateBounds:minimumDistance:maximumDistance:)](<mapcamerabounds/init(centercoordinatebounds_minimumdistance_maximumdistance_)-97kis.md>) — Creates a camera bounds with the specified region boundary and zoom ranges.
- [init(centerCoordinateBounds:minimumDistance:maximumDistance:)](<mapcamerabounds/init(centercoordinatebounds_minimumdistance_maximumdistance_)-27z4p.md>) — Creates a camera bounds with the specified map rectangle boundary and zoom ranges.
- [init(minimumDistance:maximumDistance:)](<mapcamerabounds/init(minimumdistance_maximumdistance_).md>) — Creates a camera bounds with the zoom ranges you specify.

## See Also

### Map customization

- [MapCamera](mapcamera.md) — Defines a virtual viewpoint above the map surface.
- [MapCameraPosition](mapcameraposition.md) — A structure that describes how to position the map’s camera within the map.
- [MapCameraUpdateContext](mapcameraupdatecontext.md) — A structure that defines additional information about the map camera.
- [MapCameraUpdateFrequency](mapcameraupdatefrequency.md) — A structure that describes when the map camera updates.
