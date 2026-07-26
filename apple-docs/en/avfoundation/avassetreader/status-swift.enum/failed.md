---
title: AVAssetReader.Status.failed
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreader/status-swift.enum/failed
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/status-swift.enum/failed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/status-swift.enum/failed.json'
content_hash: 'sha256:7a076f5779ce3647'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetReader](../../avassetreader.md) · [Status](../status-swift.enum.md)

# AVAssetReader.Status.failed

<sub>Case</sub>

The asset reader can no longer read samples from its asset because of an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case failed
```

## Discussion

Query the asset reader’s [error](../error.md) property to determine the reason for the failure.

## See Also

### Status values

- [AVAssetReaderStatusUnknown](unknown.md) — The asset reader is in an unknown state.
- [AVAssetReaderStatusReading](reading.md) — The asset reader is successfully reading samples from its asset.
- [AVAssetReaderStatusCompleted](completed.md) — The asset reader completes reading all samples within its specified time range.
- [AVAssetReaderStatusCancelled](cancelled.md) — The asset reader can no longer read samples because you canceled reading.
