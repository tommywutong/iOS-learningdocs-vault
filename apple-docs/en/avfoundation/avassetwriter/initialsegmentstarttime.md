---
title: initialSegmentStartTime
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/initialsegmentstarttime
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/initialsegmentstarttime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/initialsegmentstarttime.json'
content_hash: 'sha256:ee92e7765482d926'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# initialSegmentStartTime

<sub>Instance Property</sub>

The start time of the initial segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var initialSegmentStartTime: CMTime { get set }
```

## Discussion

This value is relevant only when the [preferredOutputSegmentInterval](preferredoutputsegmentinterval.md) property value is positive numeric, in which case you must set a numeric time.

You can’t change this value after writing starts.

## See Also

### Configuring segment writing

- [delegate](delegate.md) — A delegate object that responds to asset-writing events.
- [AVAssetWriterDelegate](../avassetwriterdelegate.md) — A delegate protocol that defines the methods to implement to respond to asset-writing events.
- [preferredOutputSegmentInterval](preferredoutputsegmentinterval.md) — The interval of output segments that you prefer.
- [outputFileTypeProfile](outputfiletypeprofile.md) — A profile for the output file type.
- [- flushSegment](<flushsegment().md>) — Closes the current segment and outputs it to a delegate method.
