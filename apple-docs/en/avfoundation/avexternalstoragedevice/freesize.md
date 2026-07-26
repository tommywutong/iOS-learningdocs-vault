---
title: freeSize
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalstoragedevice/freesize
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/freesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalstoragedevice/freesize.json'
content_hash: 'sha256:c09d3e6c723e6838'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalStorageDevice](../avexternalstoragedevice.md)

# freeSize

<sub>Instance Property</sub>

The amount of free storage space, in bytes, that’s available on the external storage device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var freeSize: Int { get }
```

## Discussion

The value is `-1` when the system can’t retrieve information from external storage device.

## See Also

### Inspecting a storage device

- [connected](isconnected.md) — A Boolean value that indicates whether the system has a connection to the external storage device.
- [displayName](displayname.md) — The name of an external storage device that’s appropriate for a user interface.
- [uuid](uuid.md) — The external storage device’s unique identifier.
- [totalSize](totalsize.md) — The total amount of storage space, in bytes, that’s available on the external storage device.
- [notRecommendedForCaptureUse](isnotrecommendedforcaptureuse.md) — A Boolean value that indicates whether the external storage device is suitable for camera capture. _(deprecated)_
- [reasonsNotRecommendedForCaptureUse](reasonsnotrecommendedforcaptureuse.md) _(beta)_
- [ReasonNotRecommendedForCaptureUse](reasonnotrecommendedforcaptureuse.md) _(beta)_
