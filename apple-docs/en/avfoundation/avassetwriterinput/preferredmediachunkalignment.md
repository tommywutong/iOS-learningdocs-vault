---
title: preferredMediaChunkAlignment
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/preferredmediachunkalignment
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/preferredmediachunkalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/preferredmediachunkalignment.json'
content_hash: 'sha256:7d02406cc79ef5b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# preferredMediaChunkAlignment

<sub>Instance Property</sub>

The boundary, in bytes, for aligning media chunks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preferredMediaChunkAlignment: Int { get set }
```

## Discussion

This property supports file types that support media chunk alignment, such as QuickTime Movie files. The default value is `0`, which means that the input chooses an appropriate default value. A value of `1` indicates not to use padding to achieve a particular chunk alignment. It’s an error to set a negative value for chunk alignment.

You can’t set this value after writing starts.

## See Also

### Configuring media data layout

- [preferredMediaChunkDuration](preferredmediachunkduration.md) — The duration to use for each chunk of sample data in the output file.
- [sampleReferenceBaseURL](samplereferencebaseurl.md) — The base URL sample references are relative to.
- [mediaDataLocation](mediadatalocation-swift.property.md) — Specifies how the input lays out and interleaves media data.
- [MediaDataLocation](mediadatalocation-swift.struct.md) — A structure that indicates how to lay out and interleave media data.
