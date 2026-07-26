---
title: yawAngle
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.10+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatafaceobject/yawangle
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/yawangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatafaceobject/yawangle.json'
content_hash: 'sha256:bc1f6ef1c60d02c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataFaceObject](../avmetadatafaceobject.md)

# yawAngle

<sub>Instance Property</sub>

The yaw angle of the face specified in degrees.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var yawAngle: CGFloat { get }
```

## Discussion

The yaw angle represents the rotation of the face around the vertical axis. A value of `0.0` yields a face that is looking directly at the camera, whereas a yaw angle of `90` degrees yields a face whose eye line is perpendicular to that of the camera.

You must check the value of the [hasYawAngle](hasyawangle.md) property before accessing this property. If the value in the [hasYawAngle](hasyawangle.md) property is [false](../../swift/false.md), reading the value in this property raises an exception.

## See Also

### Accessing the face detection data

- [hasRollAngle](hasrollangle.md) — A Boolean value indicating whether there is a valid roll angle associated with the face.
- [rollAngle](rollangle.md) — The roll angle of the face specified in degrees.
- [hasYawAngle](hasyawangle.md) — A Boolean value indicating whether there is a valid yaw angle associated with the face.
