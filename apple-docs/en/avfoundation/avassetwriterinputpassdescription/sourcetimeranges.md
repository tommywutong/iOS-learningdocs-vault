---
title: sourceTimeRanges
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinputpassdescription/sourcetimeranges
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputpassdescription/sourcetimeranges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputpassdescription/sourcetimeranges.json'
content_hash: 'sha256:1cfb0664728128f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputPassDescription](../avassetwriterinputpassdescription.md)

# sourceTimeRanges

<sub>Instance Property</sub>

An array of time ranges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sourceTimeRanges: [NSValue] { get }
```

## Discussion

Each element in the array is an [NSValue](../../foundation/nsvalue.md) object that wraps a [CMTimeRange](../../coremedia/cmtimerange.md) structure that represents one source time range. The value of this property is suitable to pass to the [- resetForReadingTimeRanges:](<../avassetreaderoutput/reset(forreadingtimeranges_).md>) method of [AVAssetReaderOutput](../avassetreaderoutput.md).
