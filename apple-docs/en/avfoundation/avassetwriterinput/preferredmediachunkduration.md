---
title: preferredMediaChunkDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/preferredmediachunkduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/preferredmediachunkduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/preferredmediachunkduration.json'
content_hash: 'sha256:15b6987310ba8c81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# preferredMediaChunkDuration

<sub>Instance Property</sub>

The duration to use for each chunk of sample data in the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preferredMediaChunkDuration: CMTime { get set }
```

## Discussion

This property supports file types that support media chunk alignment, such as QuickTime Movie files. Chunk duration can influence the granularity of the I/O the system performs when reading a media file; for example, during playback. A larger chunk duration can result in fewer reads from disk, at the potential expense of a higher memory footprint.

A chunk contains one or more samples. The total duration of the samples in a chunk is no greater than the preferred chunk duration, or the duration of a single sample if the sample’s duration is greater than this preferred chunk duration.

The default value is [invalid](../../coremedia/cmtime/invalid.md), which means that the input chooses an appropriate default value. It’s an error to set a chunk duration that’s negative or nonnumeric.

You can’t set this value after writing starts.

## See Also

### Configuring media data layout

- [preferredMediaChunkAlignment](preferredmediachunkalignment.md) — The boundary, in bytes, for aligning media chunks.
- [sampleReferenceBaseURL](samplereferencebaseurl.md) — The base URL sample references are relative to.
- [mediaDataLocation](mediadatalocation-swift.property.md) — Specifies how the input lays out and interleaves media data.
- [MediaDataLocation](mediadatalocation-swift.struct.md) — A structure that indicates how to lay out and interleave media data.
