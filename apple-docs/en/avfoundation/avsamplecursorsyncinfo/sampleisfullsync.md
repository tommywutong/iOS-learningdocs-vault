---
title: sampleIsFullSync
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplecursorsyncinfo/sampleisfullsync
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursorsyncinfo/sampleisfullsync'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursorsyncinfo/sampleisfullsync.json'
content_hash: 'sha256:212f1aa6185709b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursorSyncInfo](../avsamplecursorsyncinfo.md)

# sampleIsFullSync

<sub>Instance Property</sub>

A Boolean value that indicates whether a sample is a full sync sample.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sampleIsFullSync: ObjCBool
```

## Discussion

A full sync sample, also called a Instantaneous Decoder Refresh sample, is sufficient in itself to completely resynchronize a decoder.

## See Also

### Sync information

- [sampleIsPartialSync](sampleispartialsync.md) — A Boolean value that indicates whether a sample is a partial sync sample.
- [sampleIsDroppable](sampleisdroppable.md) — A Boolean value that indicates whether a sample is droppable.
