---
title: AVAssetWriterDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterdelegate.json'
content_hash: 'sha256:f50f97cd2618f892'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetWriterDelegate

<sub>Protocol</sub>

A delegate protocol that defines the methods to implement to respond to asset-writing events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol AVAssetWriterDelegate : NSObjectProtocol, Sendable
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Responding to segment output

- [- assetWriter:didOutputSegmentData:segmentType:](<avassetwriterdelegate/assetwriter(__didoutputsegmentdata_segmenttype_).md>) — Tells the delegate that the asset writer output segment data.
- [- assetWriter:didOutputSegmentData:segmentType:segmentReport:](<avassetwriterdelegate/assetwriter(__didoutputsegmentdata_segmenttype_segmentreport_).md>) — Tells the delegate that the asset writer output segment data and a report.
- [AVAssetSegmentReport](avassetsegmentreport.md) — An object that provides information about segment data.

## See Also

### Configuring segment writing

- [delegate](avassetwriter/delegate.md) — A delegate object that responds to asset-writing events.
- [preferredOutputSegmentInterval](avassetwriter/preferredoutputsegmentinterval.md) — The interval of output segments that you prefer.
- [initialSegmentStartTime](avassetwriter/initialsegmentstarttime.md) — The start time of the initial segment.
- [outputFileTypeProfile](avassetwriter/outputfiletypeprofile.md) — A profile for the output file type.
- [- flushSegment](<avassetwriter/flushsegment().md>) — Closes the current segment and outputs it to a delegate method.
