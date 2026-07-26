---
title: interleavedWithMainMediaData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct/interleavedwithmainmediadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct/interleavedwithmainmediadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct/interleavedwithmainmediadata.json'
content_hash: 'sha256:70e525b4289cf6b4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [MediaDataLocation](../mediadatalocation-swift.struct.md)

# interleavedWithMainMediaData

<sub>Type Property</sub>

A value that indicates to interleave the input’s media data with other media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let interleavedWithMainMediaData: AVAssetWriterInput.MediaDataLocation
```

## See Also

### Media data locations

- [AVAssetWriterInputMediaDataLocationBeforeMainMediaDataNotInterleaved](beforemainmediadatanotinterleaved.md) — A value that indicates to use noninterleaved data, and write it before interleaved data.
- [AVAssetWriterInputMediaDataLocationSparselyInterleavedWithMainMediaData](sparselyinterleavedwithmainmediadata.md) — Indicates that there may be large segments of time without any media data from this track. When mediaDataLocation is set to this value, AVAssetWriter will interleave the media data, but will not wait for media data from this track to achieve tight interleaving with other tracks.
