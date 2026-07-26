---
title: AVAssetWriterInput.MediaDataLocation
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct.json'
content_hash: 'sha256:35cf407da3dec334'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# AVAssetWriterInput.MediaDataLocation

<sub>Structure</sub>

A structure that indicates how to lay out and interleave media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MediaDataLocation
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Media data locations

- [AVAssetWriterInputMediaDataLocationInterleavedWithMainMediaData](mediadatalocation-swift.struct/interleavedwithmainmediadata.md) — A value that indicates to interleave the input’s media data with other media data.
- [AVAssetWriterInputMediaDataLocationBeforeMainMediaDataNotInterleaved](mediadatalocation-swift.struct/beforemainmediadatanotinterleaved.md) — A value that indicates to use noninterleaved data, and write it before interleaved data.
- [AVAssetWriterInputMediaDataLocationSparselyInterleavedWithMainMediaData](mediadatalocation-swift.struct/sparselyinterleavedwithmainmediadata.md) — Indicates that there may be large segments of time without any media data from this track. When mediaDataLocation is set to this value, AVAssetWriter will interleave the media data, but will not wait for media data from this track to achieve tight interleaving with other tracks.

### Initializers

- [init(rawValue:)](<mediadatalocation-swift.struct/init(rawvalue_).md>) — Creates a location with a string value.

## See Also

### Configuring media data layout

- [preferredMediaChunkAlignment](preferredmediachunkalignment.md) — The boundary, in bytes, for aligning media chunks.
- [preferredMediaChunkDuration](preferredmediachunkduration.md) — The duration to use for each chunk of sample data in the output file.
- [sampleReferenceBaseURL](samplereferencebaseurl.md) — The base URL sample references are relative to.
- [mediaDataLocation](mediadatalocation-swift.property.md) — Specifies how the input lays out and interleaves media data.
