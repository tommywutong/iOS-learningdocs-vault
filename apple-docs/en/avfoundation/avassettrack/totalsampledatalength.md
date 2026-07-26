---
title: totalSampleDataLength
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/totalsampledatalength
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/totalsampledatalength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/totalsampledatalength.json'
content_hash: 'sha256:422142910860af32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# totalSampleDataLength

<sub>Instance Property</sub>

The total number of bytes of sample data the track requires.

> [!warning] Deprecated
> Load the value of [totalSampleDataLength](../avpartialasyncproperty/totalsampledatalength.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var totalSampleDataLength: Int64 { get }
```

## Discussion

The value may be `0` if the framework can’t determine the total sample data length.
