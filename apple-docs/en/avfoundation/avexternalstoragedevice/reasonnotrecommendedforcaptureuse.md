---
title: AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avexternalstoragedevice/reasonnotrecommendedforcaptureuse
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/reasonnotrecommendedforcaptureuse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalstoragedevice/reasonnotrecommendedforcaptureuse.json'
content_hash: 'sha256:8a1c8d1cea2b8958'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalStorageDevice](../avexternalstoragedevice.md)

# AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
struct ReasonNotRecommendedForCaptureUse
```

## Overview

Constants indicating the reasons external storage device is not recommended for capturing high data rate videos based on https://support.apple.com/en-us/109041.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a reason

- [init(rawValue:)](<reasonnotrecommendedforcaptureuse/init(rawvalue_).md>) _(beta)_

### Reasons

- [AVExternalStorageDeviceReasonNotRecommendedForCaptureUseEncrypted](reasonnotrecommendedforcaptureuse/encrypted.md) _(beta)_
- [AVExternalStorageDeviceReasonNotRecommendedForCaptureUseSlowWritingSpeed](reasonnotrecommendedforcaptureuse/slowwritingspeed.md) _(beta)_
- [AVExternalStorageDeviceReasonNotRecommendedForCaptureUseUnknownWritingSpeed](reasonnotrecommendedforcaptureuse/unknownwritingspeed.md) _(beta)_
- [AVExternalStorageDeviceReasonNotRecommendedForCaptureUseUnsupportedFileSystem](reasonnotrecommendedforcaptureuse/unsupportedfilesystem.md) _(beta)_

## See Also

### Inspecting a storage device

- [connected](isconnected.md) — A Boolean value that indicates whether the system has a connection to the external storage device.
- [displayName](displayname.md) — The name of an external storage device that’s appropriate for a user interface.
- [uuid](uuid.md) — The external storage device’s unique identifier.
- [freeSize](freesize.md) — The amount of free storage space, in bytes, that’s available on the external storage device.
- [totalSize](totalsize.md) — The total amount of storage space, in bytes, that’s available on the external storage device.
- [notRecommendedForCaptureUse](isnotrecommendedforcaptureuse.md) — A Boolean value that indicates whether the external storage device is suitable for camera capture. _(deprecated)_
- [reasonsNotRecommendedForCaptureUse](reasonsnotrecommendedforcaptureuse.md) _(beta)_
