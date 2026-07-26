---
title: AVAggregateAssetDownloadTask
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avaggregateassetdownloadtask
source_url: 'https://developer.apple.com/documentation/avfoundation/avaggregateassetdownloadtask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avaggregateassetdownloadtask.json'
content_hash: 'sha256:6fcbff020d5d62dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAggregateAssetDownloadTask

<sub>Class</sub>

A task that downloads multiple media selections for an asset.

> [!warning] Deprecated
> Use assetDownloadTaskWithConfiguration: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class AVAggregateAssetDownloadTask
```

## Relationships

- **Inherits From**: [URLSessionTask](../foundation/urlsessiontask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ProgressReporting](../foundation/progressreporting.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the asset

- [URLAsset](avaggregateassetdownloadtask/urlasset.md) — The asset the parent task downloads. _(deprecated)_

## See Also

### Asset downloading

- [Using AVFoundation to play and persist HTTP live streams](using-avfoundation-to-play-and-persist-http-live-streams.md) — Play HTTP Live Streams and persist streams on disk for offline playback using AVFoundation.
- [AVAssetDownloadURLSession](avassetdownloadurlsession.md) — A URL session that creates and manages asset download tasks.
- [AVAssetDownloadTask](avassetdownloadtask.md) — A URL session task that downloads a remote asset to the device for offline playback.
