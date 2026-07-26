---
title: flushSegment()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/flushsegment()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/flushsegment()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/flushsegment%28%29.json'
content_hash: 'sha256:5df1b2a50b290c35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# flushSegment()

<sub>Instance Method</sub>

Closes the current segment and outputs it to a delegate method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func flushSegment()
```

## Discussion

Call this method only when the [preferredOutputSegmentInterval](preferredoutputsegmentinterval.md) property value is [indefinite](../../coremedia/cmtime/indefinite.md).

## See Also

### Configuring segment writing

- [delegate](delegate.md) — A delegate object that responds to asset-writing events.
- [AVAssetWriterDelegate](../avassetwriterdelegate.md) — A delegate protocol that defines the methods to implement to respond to asset-writing events.
- [preferredOutputSegmentInterval](preferredoutputsegmentinterval.md) — The interval of output segments that you prefer.
- [initialSegmentStartTime](initialsegmentstarttime.md) — The start time of the initial segment.
- [outputFileTypeProfile](outputfiletypeprofile.md) — A profile for the output file type.
