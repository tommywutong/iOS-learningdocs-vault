---
title: sparselyInterleavedWithMainMediaData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct/sparselyinterleavedwithmainmediadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct/sparselyinterleavedwithmainmediadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct/sparselyinterleavedwithmainmediadata.json'
content_hash: 'sha256:8abb242f6dc82081'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [MediaDataLocation](../mediadatalocation-swift.struct.md)

# sparselyInterleavedWithMainMediaData

<sub>Type Property</sub>

Indicates that there may be large segments of time without any media data from this track. When mediaDataLocation is set to this value, AVAssetWriter will interleave the media data, but will not wait for media data from this track to achieve tight interleaving with other tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let sparselyInterleavedWithMainMediaData: AVAssetWriterInput.MediaDataLocation
```

## See Also

### Media data locations

- [AVAssetWriterInputMediaDataLocationInterleavedWithMainMediaData](interleavedwithmainmediadata.md) — A value that indicates to interleave the input’s media data with other media data.
- [AVAssetWriterInputMediaDataLocationBeforeMainMediaDataNotInterleaved](beforemainmediadatanotinterleaved.md) — A value that indicates to use noninterleaved data, and write it before interleaved data.
