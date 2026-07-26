---
title: 'userLocation(followsHeading:fallback:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcameraposition/userlocation(followsheading:fallback:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcameraposition/userlocation(followsheading:fallback:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcameraposition/userlocation%28followsheading%3Afallback%3A%29.json'
content_hash: 'sha256:d75a9441ee0ec3ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapCameraPosition](../mapcameraposition.md)

# userLocation(followsHeading:fallback:)

<sub>Type Method</sub>

Creates a camera position with the specific fallback position and optionally follows the user’s heading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func userLocation(followsHeading: Bool = false, fallback: MapCameraPosition) -> MapCameraPosition
```

## Parameters

- `followsHeading` — A Boolean value that indicates whether the camera follows the person’s heading.

- `fallback` — A fallback position to use if the map hasn’t resolved the person’s location.

## Return Value

A new [MapCameraPosition](../mapcameraposition.md).

## See Also

### Creating a camera position

- [camera(_:)](<camera(__).md>) — Creates a new camera position from an existing map camera you provide.
- [item(_:allowsAutomaticPitch:)](<item(__allowsautomaticpitch_).md>) — Creates a new camera position centered on a map item and automatic pitch selection you provide.
- [rect(_:)](<rect(__).md>) — Creates a new camera position with the map boundaries you provide.
- [region(_:)](<region(__).md>) — Creates a new camera position the coordinate region you provide.
