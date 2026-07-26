---
title: outputFileTypeProfile
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/outputfiletypeprofile
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/outputfiletypeprofile'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/outputfiletypeprofile.json'
content_hash: 'sha256:f4121f786556e284'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# outputFileTypeProfile

<sub>Instance Property</sub>

A profile for the output file type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var outputFileTypeProfile: AVFileTypeProfile? { get set }
```

## Discussion

The default value is `nil`, which indicates that the writer chooses an appropriate default profile for the output file type. If your app requires segment data that’s suitable for streaming, set the value to [AVFileTypeProfileMPEG4AppleHLS](../avfiletypeprofile/mpeg4applehls.md) or [AVFileTypeProfileMPEG4CMAFCompliant](../avfiletypeprofile/mpeg4cmafcompliant.md) to output CMAF-compliant [AVFileTypeMPEG4](../avfiletype/mp4.md) data.

You can’t change this value after writing starts.

## See Also

### Configuring segment writing

- [delegate](delegate.md) — A delegate object that responds to asset-writing events.
- [AVAssetWriterDelegate](../avassetwriterdelegate.md) — A delegate protocol that defines the methods to implement to respond to asset-writing events.
- [preferredOutputSegmentInterval](preferredoutputsegmentinterval.md) — The interval of output segments that you prefer.
- [initialSegmentStartTime](initialsegmentstarttime.md) — The start time of the initial segment.
- [- flushSegment](<flushsegment().md>) — Closes the current segment and outputs it to a delegate method.
