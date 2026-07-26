---
title: 'init(lookingAtCenter:fromDistance:pitch:heading:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapcamera/init(lookingatcenter:fromdistance:pitch:heading:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapcamera/init(lookingatcenter:fromdistance:pitch:heading:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapcamera/init%28lookingatcenter%3Afromdistance%3Apitch%3Aheading%3A%29.json'
content_hash: 'sha256:a714a1a983be8a8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapCamera](../mkmapcamera.md)

# init(lookingAtCenter:fromDistance:pitch:heading:)

<sub>Initializer</sub>

Returns a new camera object using the specified distance, pitch, and heading information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(lookingAtCenter centerCoordinate: CLLocationCoordinate2D, fromDistance distance: CLLocationDistance, pitch: CGFloat, heading: CLLocationDirection)
```

## Parameters

- `centerCoordinate` — The coordinate point on which the framework centers the map.

- `distance` — The line-of-sight distance from the camera to the center coordinate of the map.

- `pitch` — The viewing angle of the camera, in degrees. A value of `0` results in a camera that points straight down at the map. Angles greater than `0` result in a camera that pitches toward the horizon by the specified number of degrees.

- `heading` — The heading of the camera (in degrees) relative to true north. The value `0` means that the top edge of the map view corresponds to true north. The value `90` means the top of the map points due east. The value `180` means the top of the map points due south, and so on.

## Return Value

A new camera object that initializes with the specified information.

## Discussion

You can obtain the altitude of the camera by multiplying `distance` by the cosine of the `pitch` value.

## See Also

### Getting a camera object

- [+ cameraLookingAtCenterCoordinate:fromEyeCoordinate:eyeAltitude:](<init(lookingatcenter_fromeyecoordinate_eyealtitude_).md>) — Returns a new camera object using the specified viewing angle information.
- [+ cameraLookingAtMapItem:forViewSize:allowPitch:](<init(lookingat_forviewsize_allowpitch_).md>) — Returns a new camera object using the specified map item, view size, and pitch.
