---
title: mediaDataLocation
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.property.json'
content_hash: 'sha256:cc9791a7b296119a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# mediaDataLocation

<sub>Instance Property</sub>

Specifies how the input lays out and interleaves media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mediaDataLocation: AVAssetWriterInput.MediaDataLocation { get set }
```

## Discussion

Use this property to optimize tracks that contain a small amount of data that you need all at once, such as chapter tracks. Setting the value to [AVAssetWriterInputMediaDataLocationBeforeMainMediaDataNotInterleaved](mediadatalocation-swift.struct/beforemainmediadatanotinterleaved.md) causes the asset writer to try to write the media data for this track before interleaved inputs. For file types that support preloading media data, such as QuickTime files, setting this value also writes an indicator to the file to preload its media data.

Set the value to [AVAssetWriterInputMediaDataLocationInterleavedWithMainMediaData](mediadatalocation-swift.struct/interleavedwithmainmediadata.md) for tracks whose media data you need only as it approaches its presentation time, or when multiple inputs exist that supply media data that plays concurrently.

You can’t set this value after writing starts.

## See Also

### Configuring media data layout

- [preferredMediaChunkAlignment](preferredmediachunkalignment.md) — The boundary, in bytes, for aligning media chunks.
- [preferredMediaChunkDuration](preferredmediachunkduration.md) — The duration to use for each chunk of sample data in the output file.
- [sampleReferenceBaseURL](samplereferencebaseurl.md) — The base URL sample references are relative to.
- [MediaDataLocation](mediadatalocation-swift.struct.md) — A structure that indicates how to lay out and interleave media data.
