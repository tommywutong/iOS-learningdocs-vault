---
title: reasonsNotRecommendedForCaptureUse
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avexternalstoragedevice/reasonsnotrecommendedforcaptureuse
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/reasonsnotrecommendedforcaptureuse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalstoragedevice/reasonsnotrecommendedforcaptureuse.json'
content_hash: 'sha256:030e095e11b370cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalStorageDevice](../avexternalstoragedevice.md)

# reasonsNotRecommendedForCaptureUse

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var reasonsNotRecommendedForCaptureUse: Set<AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse> { get }
```

## Discussion

A set of reasons why the storage device is not recommended for capture.

Contains one or more AVExternalStorageDeviceReasonNotRecommendedForCaptureUse values indicating the issues with the device. Returns an empty set if there are no known issues.

## See Also

### Inspecting a storage device

- [connected](isconnected.md) — A Boolean value that indicates whether the system has a connection to the external storage device.
- [displayName](displayname.md) — The name of an external storage device that’s appropriate for a user interface.
- [uuid](uuid.md) — The external storage device’s unique identifier.
- [freeSize](freesize.md) — The amount of free storage space, in bytes, that’s available on the external storage device.
- [totalSize](totalsize.md) — The total amount of storage space, in bytes, that’s available on the external storage device.
- [notRecommendedForCaptureUse](isnotrecommendedforcaptureuse.md) — A Boolean value that indicates whether the external storage device is suitable for camera capture. _(deprecated)_
- [ReasonNotRecommendedForCaptureUse](reasonnotrecommendedforcaptureuse.md) _(beta)_
