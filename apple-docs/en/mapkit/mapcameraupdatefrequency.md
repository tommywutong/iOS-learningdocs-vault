---
title: MapCameraUpdateFrequency
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapcameraupdatefrequency
source_url: 'https://developer.apple.com/documentation/mapkit/mapcameraupdatefrequency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcameraupdatefrequency.json'
content_hash: 'sha256:bbb1e1332dcb08b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapCameraUpdateFrequency

<sub>Structure</sub>

A structure that describes when the map camera updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapCameraUpdateFrequency
```

## Topics

### Timing of camera updates

- [continuous](mapcameraupdatefrequency/continuous.md) — A value that indicates that all camera updates are continuous, including while interactions are taking place.
- [onEnd](mapcameraupdatefrequency/onend.md) — A value that indicates the camera updates when map interactions are complete.

## See Also

### Map customization

- [MapCamera](mapcamera.md) — Defines a virtual viewpoint above the map surface.
- [MapCameraBounds](mapcamerabounds.md) — Defines an optional boundary of an area within which the map’s center needs to remain.
- [MapCameraPosition](mapcameraposition.md) — A structure that describes how to position the map’s camera within the map.
- [MapCameraUpdateContext](mapcameraupdatecontext.md) — A structure that defines additional information about the map camera.
