---
title: 'init(lookingAtCenter:fromEyeCoordinate:eyeAltitude:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapcamera/init(lookingatcenter:fromeyecoordinate:eyealtitude:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapcamera/init(lookingatcenter:fromeyecoordinate:eyealtitude:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapcamera/init%28lookingatcenter%3Afromeyecoordinate%3Aeyealtitude%3A%29.json'
content_hash: 'sha256:35bd1ee53460074a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapCamera](../mkmapcamera.md)

# init(lookingAtCenter:fromEyeCoordinate:eyeAltitude:)

<sub>Initializer</sub>

Returns a new camera object using the specified viewing angle information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(lookingAtCenter centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude: CLLocationDistance)
```

## Parameters

- `centerCoordinate` — The coordinate point on which the framework centers the map.

- `eyeCoordinate` — The coordinate point at which to place the camera. If the value for this parameter is equal to the value in the `centerCoordinate` parameter, the framework displays the map as if the camera is looking straight down. If this point is offset from the `centerCoordinate` value, the framework displays the map with an appropriate heading and pitch angle.

- `eyeAltitude` — The altitude (in meters) above the ground at which to place the camera.

## Return Value

A new camera object that initializes with the specified information.

## Discussion

This method calculates the required pitch and heading angles to accommodate the specified eye position and altitude.

## See Also

### Getting a camera object

- [+ cameraLookingAtCenterCoordinate:fromDistance:pitch:heading:](<init(lookingatcenter_fromdistance_pitch_heading_).md>) — Returns a new camera object using the specified distance, pitch, and heading information.
- [+ cameraLookingAtMapItem:forViewSize:allowPitch:](<init(lookingat_forviewsize_allowpitch_).md>) — Returns a new camera object using the specified map item, view size, and pitch.
