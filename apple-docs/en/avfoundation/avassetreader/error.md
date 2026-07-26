---
title: error
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreader/error
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/error.json'
content_hash: 'sha256:7c87df0ff786b9e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# error

<sub>Instance Property</sub>

An error that describes the reason for a failure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var error: (any Error)? { get }
```

## Discussion

The value is `nil` if the asset reader’s status isn’t [AVAssetReaderStatusFailed](status-swift.enum/failed.md).

This property is thread safe.

## See Also

### Configuring reading

- [timeRange](timerange.md) — The time range within the asset to read.
- [status](status-swift.property.md) — The status of reading sample buffers from the asset.
- [Status](status-swift.enum.md) — Values that represent the possible states of an asset reader.
