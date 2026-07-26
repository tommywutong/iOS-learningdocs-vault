---
title: MapCameraPosition
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapcameraposition
source_url: 'https://developer.apple.com/documentation/mapkit/mapcameraposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcameraposition.json'
content_hash: 'sha256:e256bf82214ea768'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapCameraPosition

<sub>Structure</sub>

A structure that describes how to position the map’s camera within the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapCameraPosition
```

## Overview

`MapCameraPosition` contains a variety of properties that you can use to control the semantic framings of the camera in relation to its position to the map, such as [automatic](mapcameraposition/automatic.md), which frames the content of the map, and the [camera](mapcameraposition/camera.md) property, which allows you to specify an explicit camera position.

When you pass `MapCameraPosition` as a binding to a map, the map adjusts its camera to frame the requested content, or to exactly match the camera `MapCameraPosition` specifies. If a person interacts with the [Map](map.md) in a way that moves the map, the map resets the position to a value that specifies [positionedByUser](mapcameraposition/positionedbyuser.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Creating a camera position

- [camera(_:)](<mapcameraposition/camera(__).md>) — Creates a new camera position from an existing map camera you provide.
- [item(_:allowsAutomaticPitch:)](<mapcameraposition/item(__allowsautomaticpitch_).md>) — Creates a new camera position centered on a map item and automatic pitch selection you provide.
- [rect(_:)](<mapcameraposition/rect(__).md>) — Creates a new camera position with the map boundaries you provide.
- [region(_:)](<mapcameraposition/region(__).md>) — Creates a new camera position the coordinate region you provide.
- [userLocation(followsHeading:fallback:)](<mapcameraposition/userlocation(followsheading_fallback_).md>) — Creates a camera position with the specific fallback position and optionally follows the user’s heading.

### Information about camera position and framing

- [automatic](mapcameraposition/automatic.md) — The position that frames the map’s content.
- [allowsAutomaticPitch](mapcameraposition/allowsautomaticpitch.md) — The setting that allows the map’s camera to automatically set the pitch when framing the item.
- [camera](mapcameraposition/camera.md) — A map camera that defines the camera positioning.
- [fallbackPosition](mapcameraposition/fallbackposition.md) — The position to use if the framework hasn’t resolved the person’s location.
- [item](mapcameraposition/item.md) — The item the map is framing.
- [positionedByUser](mapcameraposition/positionedbyuser.md) — A Boolean value that indicates whether the person specified the camera position by interacting with the map.
- [rect](mapcameraposition/rect.md) — The position that frames the given map rectangle.
- [region](mapcameraposition/region.md) — The coordinate region to frame.

### Accessing information about someone’s location

- [followsUserHeading](mapcameraposition/followsuserheading.md) — A Boolean value that indicates whether the map is following someone’s heading.
- [followsUserLocation](mapcameraposition/followsuserlocation.md) — A Boolean value that indicates whether the map is following someone’s location.

## See Also

### Map customization

- [MapCamera](mapcamera.md) — Defines a virtual viewpoint above the map surface.
- [MapCameraBounds](mapcamerabounds.md) — Defines an optional boundary of an area within which the map’s center needs to remain.
- [MapCameraUpdateContext](mapcameraupdatecontext.md) — A structure that defines additional information about the map camera.
- [MapCameraUpdateFrequency](mapcameraupdatefrequency.md) — A structure that describes when the map camera updates.
