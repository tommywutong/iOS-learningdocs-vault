---
title: AVMetadataFaceObject
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.10+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatafaceobject
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatafaceobject.json'
content_hash: 'sha256:7110e617bd502c0e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetadataFaceObject

<sub>Class</sub>

Face information detected by a metadata capture output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVMetadataFaceObject
```

## Overview

The `AVMetadataFaceObject` class is a concrete subclass of [AVMetadataObject](avmetadataobject.md) that defines the features of a single detected face. You can retrieve instances of this class from the output of an [AVCaptureMetadataOutput](avcapturemetadataoutput.md) object on devices that support face detection.

## Relationships

- **Inherits From**: [AVMetadataObject](avmetadataobject.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the face identifier

- [faceID](avmetadatafaceobject/faceid.md) — The unique ID for this face metadata object.

### Accessing the face detection data

- [hasRollAngle](avmetadatafaceobject/hasrollangle.md) — A Boolean value indicating whether there is a valid roll angle associated with the face.
- [rollAngle](avmetadatafaceobject/rollangle.md) — The roll angle of the face specified in degrees.
- [hasYawAngle](avmetadatafaceobject/hasyawangle.md) — A Boolean value indicating whether there is a valid yaw angle associated with the face.
- [yawAngle](avmetadatafaceobject/yawangle.md) — The yaw angle of the face specified in degrees.

### Constants

- [Face metadata type](face-metadata-type.md) — A metadata type string for face detection metadata.
