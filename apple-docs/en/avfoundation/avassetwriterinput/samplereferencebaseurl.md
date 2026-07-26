---
title: sampleReferenceBaseURL
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/samplereferencebaseurl
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplereferencebaseurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/samplereferencebaseurl.json'
content_hash: 'sha256:faf198a71ce01a3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# sampleReferenceBaseURL

<sub>Instance Property</sub>

The base URL sample references are relative to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sampleReferenceBaseURL: URL? { get set }
```

## Discussion

This property is only valid for file types that support writing sample references, such as QuickTime files. If the system resolves the value of this property to an absolute URL, the sample references it appends are relative to this URL. The URL must point to a location that’s in a directory that’s a parent of the sample reference location.

For example, setting the value of this property to `file:///User/johnappleseed/Movies/` and appending sample buffers with the [kCMSampleBufferAttachmentKey_SampleReferenceURL](../../coremedia/kcmsamplebufferattachmentkey_samplereferenceurl.md) attachment set to `file:///User/johnappleseed/Movies/data/movie1.mov` writes a sample reference of `data/movie1.mov` to the movie.

## See Also

### Configuring media data layout

- [preferredMediaChunkAlignment](preferredmediachunkalignment.md) — The boundary, in bytes, for aligning media chunks.
- [preferredMediaChunkDuration](preferredmediachunkduration.md) — The duration to use for each chunk of sample data in the output file.
- [mediaDataLocation](mediadatalocation-swift.property.md) — Specifies how the input lays out and interleaves media data.
- [MediaDataLocation](mediadatalocation-swift.struct.md) — A structure that indicates how to lay out and interleave media data.
