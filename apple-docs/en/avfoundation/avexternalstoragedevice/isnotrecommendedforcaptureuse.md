---
title: isNotRecommendedForCaptureUse
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+（27.0 起废弃）, iPadOS 17.0+（27.0 起废弃）, Mac Catalyst 17.0+（27.0 起废弃）, macOS 14.0+（27.0 起废弃）, tvOS 17.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avexternalstoragedevice/isnotrecommendedforcaptureuse
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/isnotrecommendedforcaptureuse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalstoragedevice/isnotrecommendedforcaptureuse.json'
content_hash: 'sha256:53d1a30dce337ccc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalStorageDevice](../avexternalstoragedevice.md)

# isNotRecommendedForCaptureUse

<sub>Instance Property</sub>

A Boolean value that indicates whether the external storage device is suitable for camera capture.

> [!warning] Deprecated
> Use reasonsNotRecommendedForCaptureUse instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isNotRecommendedForCaptureUse: Bool { get }
```

## See Also

### Inspecting a storage device

- [connected](isconnected.md) — A Boolean value that indicates whether the system has a connection to the external storage device.
- [displayName](displayname.md) — The name of an external storage device that’s appropriate for a user interface.
- [uuid](uuid.md) — The external storage device’s unique identifier.
- [freeSize](freesize.md) — The amount of free storage space, in bytes, that’s available on the external storage device.
- [totalSize](totalsize.md) — The total amount of storage space, in bytes, that’s available on the external storage device.
- [reasonsNotRecommendedForCaptureUse](reasonsnotrecommendedforcaptureuse.md) _(beta)_
- [ReasonNotRecommendedForCaptureUse](reasonnotrecommendedforcaptureuse.md) _(beta)_
