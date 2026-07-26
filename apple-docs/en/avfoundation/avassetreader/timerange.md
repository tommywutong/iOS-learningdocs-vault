---
title: timeRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreader/timerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/timerange.json'
content_hash: 'sha256:54a7947418d352dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# timeRange

<sub>Instance Property</sub>

The time range within the asset to read.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var timeRange: CMTimeRange { get set }
```

## Discussion

The default value is a time range with a start time of [zero](../../coremedia/cmtime/zero.md) and a duration of [positiveInfinity](../../coremedia/cmtime/positiveinfinity.md).

You can’t modify this value after reading starts.

## See Also

### Configuring reading

- [status](status-swift.property.md) — The status of reading sample buffers from the asset.
- [Status](status-swift.enum.md) — Values that represent the possible states of an asset reader.
- [error](error.md) — An error that describes the reason for a failure.
