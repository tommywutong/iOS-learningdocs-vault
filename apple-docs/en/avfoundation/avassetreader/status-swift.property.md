---
title: status
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreader/status-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/status-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/status-swift.property.json'
content_hash: 'sha256:e690e39d411c4e2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# status

<sub>Instance Property</sub>

The status of reading sample buffers from the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var status: AVAssetReader.Status { get }
```

## Discussion

Check the value of this property when the [- copyNextSampleBuffer](<../avassetreaderoutput/copynextsamplebuffer().md>) method on [AVAssetReaderOutput](../avassetreaderoutput.md) returns `nil` to determine why the output can’t read more data.

This property is thread safe.

## See Also

### Configuring reading

- [timeRange](timerange.md) — The time range within the asset to read.
- [Status](status-swift.enum.md) — Values that represent the possible states of an asset reader.
- [error](error.md) — An error that describes the reason for a failure.
