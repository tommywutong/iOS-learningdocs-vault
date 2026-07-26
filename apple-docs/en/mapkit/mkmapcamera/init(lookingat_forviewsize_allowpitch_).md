---
title: 'init(lookingAt:forViewSize:allowPitch:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapcamera/init(lookingat:forviewsize:allowpitch:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapcamera/init(lookingat:forviewsize:allowpitch:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapcamera/init%28lookingat%3Aforviewsize%3Aallowpitch%3A%29.json'
content_hash: 'sha256:1e174865aea4a406'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapCamera](../mkmapcamera.md)

# init(lookingAt:forViewSize:allowPitch:)

<sub>Initializer</sub>

Returns a new camera object using the specified map item, view size, and pitch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(lookingAt mapItem: MKMapItem, forViewSize viewSize: CGSize, allowPitch: Bool)
```

## Parameters

- `mapItem` — An [MKMapItem](../mkmapitem.md) that indicates the location of the camera.

- `viewSize` — The view’s size.

- `allowPitch` — A Boolean value that indicates if the camera should the use map’s pitch angle.

## See Also

### Getting a camera object

- [+ cameraLookingAtCenterCoordinate:fromEyeCoordinate:eyeAltitude:](<init(lookingatcenter_fromeyecoordinate_eyealtitude_).md>) — Returns a new camera object using the specified viewing angle information.
- [+ cameraLookingAtCenterCoordinate:fromDistance:pitch:heading:](<init(lookingatcenter_fromdistance_pitch_heading_).md>) — Returns a new camera object using the specified distance, pitch, and heading information.
