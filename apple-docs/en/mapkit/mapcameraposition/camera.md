---
title: camera
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapcameraposition/camera
source_url: 'https://developer.apple.com/documentation/mapkit/mapcameraposition/camera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcameraposition/camera.json'
content_hash: 'sha256:620db8ad6ddbd1ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapCameraPosition](../mapcameraposition.md)

# camera

<sub>Instance Property</sub>

A map camera that defines the camera positioning.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var camera: MapCamera? { get }
```

## See Also

### Information about camera position and framing

- [automatic](automatic.md) — The position that frames the map’s content.
- [allowsAutomaticPitch](allowsautomaticpitch.md) — The setting that allows the map’s camera to automatically set the pitch when framing the item.
- [fallbackPosition](fallbackposition.md) — The position to use if the framework hasn’t resolved the person’s location.
- [item](item.md) — The item the map is framing.
- [positionedByUser](positionedbyuser.md) — A Boolean value that indicates whether the person specified the camera position by interacting with the map.
- [rect](rect.md) — The position that frames the given map rectangle.
- [region](region.md) — The coordinate region to frame.
