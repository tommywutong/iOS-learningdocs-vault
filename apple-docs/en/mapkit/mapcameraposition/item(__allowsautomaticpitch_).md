---
title: 'item(_:allowsAutomaticPitch:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcameraposition/item(_:allowsautomaticpitch:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcameraposition/item(_:allowsautomaticpitch:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcameraposition/item%28_%3Aallowsautomaticpitch%3A%29.json'
content_hash: 'sha256:e07bd7a3f0a98c89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapCameraPosition](../mapcameraposition.md)

# item(_:allowsAutomaticPitch:)

<sub>Type Method</sub>

Creates a new camera position centered on a map item and automatic pitch selection you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func item(_ item: MKMapItem, allowsAutomaticPitch: Bool = true) -> MapCameraPosition
```

## Parameters

- `item` — The [MKMapItem](../mkmapitem.md) to center the map on.

- `allowsAutomaticPitch` — A Boolean value that indicates whether the camera selects a pitch automatically.

## Return Value

Returns a new [MapCameraPosition](../mapcameraposition.md).

## See Also

### Creating a camera position

- [camera(_:)](<camera(__).md>) — Creates a new camera position from an existing map camera you provide.
- [rect(_:)](<rect(__).md>) — Creates a new camera position with the map boundaries you provide.
- [region(_:)](<region(__).md>) — Creates a new camera position the coordinate region you provide.
- [userLocation(followsHeading:fallback:)](<userlocation(followsheading_fallback_).md>) — Creates a camera position with the specific fallback position and optionally follows the user’s heading.
