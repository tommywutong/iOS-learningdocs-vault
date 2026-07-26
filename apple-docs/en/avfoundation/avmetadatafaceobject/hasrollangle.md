---
title: hasRollAngle
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.10+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatafaceobject/hasrollangle
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/hasrollangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatafaceobject/hasrollangle.json'
content_hash: 'sha256:2468820209f0963a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataFaceObject](../avmetadatafaceobject.md)

# hasRollAngle

<sub>Instance Property</sub>

A Boolean value indicating whether there is a valid roll angle associated with the face.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var hasRollAngle: Bool { get }
```

## Discussion

If the value of this property is [false](../../swift/false.md), the value in the [rollAngle](rollangle.md) property is invalid and must not be accessed.

## See Also

### Accessing the face detection data

- [rollAngle](rollangle.md) — The roll angle of the face specified in degrees.
- [hasYawAngle](hasyawangle.md) — A Boolean value indicating whether there is a valid yaw angle associated with the face.
- [yawAngle](yawangle.md) — The yaw angle of the face specified in degrees.
