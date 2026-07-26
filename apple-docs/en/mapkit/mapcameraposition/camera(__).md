---
title: 'camera(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcameraposition/camera(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcameraposition/camera(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcameraposition/camera%28_%3A%29.json'
content_hash: 'sha256:48e95abb133f3010'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapCameraPosition](../mapcameraposition.md)

# camera(_:)

<sub>Type Method</sub>

Creates a new camera position from an existing map camera you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func camera(_ camera: MapCamera) -> MapCameraPosition
```

## Parameters

- `camera` — The map camera to convert.

## Return Value

Returns a new camera position.

## See Also

### Creating a camera position

- [item(_:allowsAutomaticPitch:)](<item(__allowsautomaticpitch_).md>) — Creates a new camera position centered on a map item and automatic pitch selection you provide.
- [rect(_:)](<rect(__).md>) — Creates a new camera position with the map boundaries you provide.
- [region(_:)](<region(__).md>) — Creates a new camera position the coordinate region you provide.
- [userLocation(followsHeading:fallback:)](<userlocation(followsheading_fallback_).md>) — Creates a camera position with the specific fallback position and optionally follows the user’s heading.
