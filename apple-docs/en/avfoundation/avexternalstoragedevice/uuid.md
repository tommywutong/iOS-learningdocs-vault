---
title: uuid
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalstoragedevice/uuid
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/uuid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalstoragedevice/uuid.json'
content_hash: 'sha256:1501b9121263ec4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalStorageDevice](../avexternalstoragedevice.md)

# uuid

<sub>Instance Property</sub>

The external storage device’s unique identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var uuid: UUID? { get }
```

## Discussion

The value is `nil` when the system can’t retrieve information from external storage device.

## See Also

### Inspecting a storage device

- [connected](isconnected.md) — A Boolean value that indicates whether the system has a connection to the external storage device.
- [displayName](displayname.md) — The name of an external storage device that’s appropriate for a user interface.
- [freeSize](freesize.md) — The amount of free storage space, in bytes, that’s available on the external storage device.
- [totalSize](totalsize.md) — The total amount of storage space, in bytes, that’s available on the external storage device.
- [notRecommendedForCaptureUse](isnotrecommendedforcaptureuse.md) — A Boolean value that indicates whether the external storage device is suitable for camera capture. _(deprecated)_
- [reasonsNotRecommendedForCaptureUse](reasonsnotrecommendedforcaptureuse.md) _(beta)_
- [ReasonNotRecommendedForCaptureUse](reasonnotrecommendedforcaptureuse.md) _(beta)_
