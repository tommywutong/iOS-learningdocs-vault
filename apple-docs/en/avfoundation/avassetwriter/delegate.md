---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/delegate.json'
content_hash: 'sha256:2332499bf6676999'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# delegate

<sub>Instance Property</sub>

A delegate object that responds to asset-writing events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
weak var delegate: (any AVAssetWriterDelegate)? { get set }
```

## See Also

### Configuring segment writing

- [AVAssetWriterDelegate](../avassetwriterdelegate.md) — A delegate protocol that defines the methods to implement to respond to asset-writing events.
- [preferredOutputSegmentInterval](preferredoutputsegmentinterval.md) — The interval of output segments that you prefer.
- [initialSegmentStartTime](initialsegmentstarttime.md) — The start time of the initial segment.
- [outputFileTypeProfile](outputfiletypeprofile.md) — A profile for the output file type.
- [- flushSegment](<flushsegment().md>) — Closes the current segment and outputs it to a delegate method.
