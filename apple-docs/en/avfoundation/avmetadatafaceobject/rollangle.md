---
title: rollAngle
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.10+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatafaceobject/rollangle
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/rollangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatafaceobject/rollangle.json'
content_hash: 'sha256:045509b98d2ba38c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataFaceObject](../avmetadatafaceobject.md)

# rollAngle

<sub>Instance Property</sub>

The roll angle of the face specified in degrees.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var rollAngle: CGFloat { get }
```

## Discussion

The roll angle represents the side-to-side tilt of the face relative to the metadata’s bounding rectangle. A value of `0.0` yields a face that is level relative to the picture, whereas a value of `90` yields a face that is perpendicular relative to the picture.

You must check the value of the [hasRollAngle](hasrollangle.md) property before accessing this property. If the value in the [hasRollAngle](hasrollangle.md) property is [false](../../swift/false.md), reading the value in this property raises an exception.

## See Also

### Accessing the face detection data

- [hasRollAngle](hasrollangle.md) — A Boolean value indicating whether there is a valid roll angle associated with the face.
- [hasYawAngle](hasyawangle.md) — A Boolean value indicating whether there is a valid yaw angle associated with the face.
- [yawAngle](yawangle.md) — The yaw angle of the face specified in degrees.
