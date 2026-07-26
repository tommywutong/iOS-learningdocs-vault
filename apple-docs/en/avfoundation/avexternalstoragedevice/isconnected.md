---
title: isConnected
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalstoragedevice/isconnected
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/isconnected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalstoragedevice/isconnected.json'
content_hash: 'sha256:3740488278e3db48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalStorageDevice](../avexternalstoragedevice.md)

# isConnected

<sub>Instance Property</sub>

A Boolean value that indicates whether the system has a connection to the external storage device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isConnected: Bool { get }
```

## See Also

### Inspecting a storage device

- [displayName](displayname.md) — The name of an external storage device that’s appropriate for a user interface.
- [uuid](uuid.md) — The external storage device’s unique identifier.
- [freeSize](freesize.md) — The amount of free storage space, in bytes, that’s available on the external storage device.
- [totalSize](totalsize.md) — The total amount of storage space, in bytes, that’s available on the external storage device.
- [notRecommendedForCaptureUse](isnotrecommendedforcaptureuse.md) — A Boolean value that indicates whether the external storage device is suitable for camera capture. _(deprecated)_
- [reasonsNotRecommendedForCaptureUse](reasonsnotrecommendedforcaptureuse.md) _(beta)_
- [ReasonNotRecommendedForCaptureUse](reasonnotrecommendedforcaptureuse.md) _(beta)_
