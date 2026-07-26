---
title: AVAssetReader.Status
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreader/status-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/status-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/status-swift.enum.json'
content_hash: 'sha256:ac3db39389065fa5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# AVAssetReader.Status

<sub>Enumeration</sub>

Values that represent the possible states of an asset reader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Status
```

## Overview

You determine an asset reader’s status using its [status](status-swift.property.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Status values

- [AVAssetReaderStatusUnknown](status-swift.enum/unknown.md) — The asset reader is in an unknown state.
- [AVAssetReaderStatusReading](status-swift.enum/reading.md) — The asset reader is successfully reading samples from its asset.
- [AVAssetReaderStatusCompleted](status-swift.enum/completed.md) — The asset reader completes reading all samples within its specified time range.
- [AVAssetReaderStatusFailed](status-swift.enum/failed.md) — The asset reader can no longer read samples from its asset because of an error.
- [AVAssetReaderStatusCancelled](status-swift.enum/cancelled.md) — The asset reader can no longer read samples because you canceled reading.

### Initializers

- [init(rawValue:)](<status-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring reading

- [timeRange](timerange.md) — The time range within the asset to read.
- [status](status-swift.property.md) — The status of reading sample buffers from the asset.
- [error](error.md) — An error that describes the reason for a failure.
