---
title: 'assetWriter(_:didOutputSegmentData:segmentType:segmentReport:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterdelegate/assetwriter(_:didoutputsegmentdata:segmenttype:segmentreport:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterdelegate/assetwriter(_:didoutputsegmentdata:segmenttype:segmentreport:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterdelegate/assetwriter%28_%3Adidoutputsegmentdata%3Asegmenttype%3Asegmentreport%3A%29.json'
content_hash: 'sha256:06ad3f957241840c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterDelegate](../avassetwriterdelegate.md)

# assetWriter(_:didOutputSegmentData:segmentType:segmentReport:)

<sub>Instance Method</sub>

Tells the delegate that the asset writer output segment data and a report.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func assetWriter(_ writer: AVAssetWriter, didOutputSegmentData segmentData: Data, segmentType: AVAssetSegmentType, segmentReport: AVAssetSegmentReport?)
```

## Parameters

- `writer` — The asset writer that output segment data.

- `segmentData` — The data for the segment.

- `segmentType` — The type of segment data.

- `segmentReport` — A report for the segment data.

## Discussion

The asset writer stops normal file writing when you implement this method.

## See Also

### Responding to segment output

- [- assetWriter:didOutputSegmentData:segmentType:](<assetwriter(__didoutputsegmentdata_segmenttype_).md>) — Tells the delegate that the asset writer output segment data.
- [AVAssetSegmentReport](../avassetsegmentreport.md) — An object that provides information about segment data.
