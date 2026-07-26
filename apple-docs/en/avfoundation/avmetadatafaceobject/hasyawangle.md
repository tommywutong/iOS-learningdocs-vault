---
title: hasYawAngle
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.10+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatafaceobject/hasyawangle
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/hasyawangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatafaceobject/hasyawangle.json'
content_hash: 'sha256:8cbdeaeb6c937a28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataFaceObject](../avmetadatafaceobject.md)

# hasYawAngle

<sub>Instance Property</sub>

A Boolean value indicating whether there is a valid yaw angle associated with the face.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var hasYawAngle: Bool { get }
```

## Discussion

If the value of this property is [false](../../swift/false.md), the value in the [yawAngle](yawangle.md) property is invalid and must not be accessed.

## See Also

### Accessing the face detection data

- [hasRollAngle](hasrollangle.md) — A Boolean value indicating whether there is a valid roll angle associated with the face.
- [rollAngle](rollangle.md) — The roll angle of the face specified in degrees.
- [yawAngle](yawangle.md) — The yaw angle of the face specified in degrees.
