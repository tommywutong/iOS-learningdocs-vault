---
title: preferredOutputSegmentInterval
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/preferredoutputsegmentinterval
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/preferredoutputsegmentinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/preferredoutputsegmentinterval.json'
content_hash: 'sha256:a82c390e4eef5dc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# preferredOutputSegmentInterval

<sub>Instance Property</sub>

The interval of output segments that you prefer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preferredOutputSegmentInterval: CMTime { get set }
```

## Discussion

The default value is [invalid](../../coremedia/cmtime/invalid.md), which indicates that the asset writer chooses an appropriate default value. You may also set a positive numeric or [indefinite](../../coremedia/cmtime/indefinite.md) time. When the value is [indefinite](../../coremedia/cmtime/indefinite.md), each call you make to [- flushSegment](<flushsegment().md>) outputs a segment data.

You can’t change this value after writing starts.

## See Also

### Configuring segment writing

- [delegate](delegate.md) — A delegate object that responds to asset-writing events.
- [AVAssetWriterDelegate](../avassetwriterdelegate.md) — A delegate protocol that defines the methods to implement to respond to asset-writing events.
- [initialSegmentStartTime](initialsegmentstarttime.md) — The start time of the initial segment.
- [outputFileTypeProfile](outputfiletypeprofile.md) — A profile for the output file type.
- [- flushSegment](<flushsegment().md>) — Closes the current segment and outputs it to a delegate method.
