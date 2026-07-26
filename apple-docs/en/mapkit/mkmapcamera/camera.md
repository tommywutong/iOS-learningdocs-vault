---
title: camera
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapcamera/camera
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapcamera/camera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapcamera/camera.json'
content_hash: 'sha256:654632e91d0ea30c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapCamera](../mkmapcamera.md)

# camera

<sub>Type Method</sub>

Returns a new camera object for you to configure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) camera;
```

## Return Value

A new camera object.

## Discussion

You must change the values of the returned camera object before using it.

## See Also

### Getting a camera object

- [+ cameraLookingAtCenterCoordinate:fromEyeCoordinate:eyeAltitude:](<init(lookingatcenter_fromeyecoordinate_eyealtitude_).md>) — Returns a new camera object using the specified viewing angle information.
- [+ cameraLookingAtCenterCoordinate:fromDistance:pitch:heading:](<init(lookingatcenter_fromdistance_pitch_heading_).md>) — Returns a new camera object using the specified distance, pitch, and heading information.
- [+ cameraLookingAtMapItem:forViewSize:allowPitch:](<init(lookingat_forviewsize_allowpitch_).md>) — Returns a new camera object using the specified map item, view size, and pitch.
