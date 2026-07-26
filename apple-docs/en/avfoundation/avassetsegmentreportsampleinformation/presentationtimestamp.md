---
title: presentationTimeStamp
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetsegmentreportsampleinformation/presentationtimestamp
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetsegmentreportsampleinformation/presentationtimestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetsegmentreportsampleinformation/presentationtimestamp.json'
content_hash: 'sha256:6e684ba04c6be3a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetSegmentReportSampleInformation](../avassetsegmentreportsampleinformation.md)

# presentationTimeStamp

<sub>Instance Property</sub>

The presentation timestamp (PTS) of a sample.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var presentationTimeStamp: CMTime { get }
```

## Discussion

This timestamp may be different from the [earliestPresentationTimeStamp](../avassetsegmenttrackreport/earliestpresentationtimestamp.md) if the video’s author encodes it using frame reordering.

## See Also

### Inspecting the information

- [offset](offset.md) — The offset of a sample in the segment.
- [length](length.md) — The length of the sample data.
- [isSyncSample](issyncsample.md) — A Boolean value that indicates whether the sample is a key frame.
