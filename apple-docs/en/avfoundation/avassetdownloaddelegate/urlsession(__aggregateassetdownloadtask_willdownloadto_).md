---
title: 'urlSession(_:aggregateAssetDownloadTask:willDownloadTo:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:willdownloadto:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:willdownloadto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloaddelegate/urlsession%28_%3Aaggregateassetdownloadtask%3Awilldownloadto%3A%29.json'
content_hash: 'sha256:6e720f5300d18698'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadDelegate](../avassetdownloaddelegate.md)

# urlSession(_:aggregateAssetDownloadTask:willDownloadTo:)

<sub>Instance Method</sub>

Tells the delegate the final location of the asset when the download completes.

> [!warning] Deprecated
> Use URLSession:assetDownloadTask:willDownloadToURL: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func urlSession(_ session: URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, willDownloadTo location: URL)
```

## Parameters

- `session` — The session the asset download task is on.

- `aggregateAssetDownloadTask` — The task that downloads the asset.

- `location` — The file URL to which the task downloads media.

## See Also

### Responding to aggregate download events

- [- URLSession:aggregateAssetDownloadTask:didLoadTimeRange:totalTimeRangesLoaded:timeRangeExpectedToLoad:forMediaSelection:](<urlsession(__aggregateassetdownloadtask_didload_totaltimerangesloaded_timerangeexpectedtoload_for_).md>) — Tells the delegate that the aggregate download task loaded a new time range. _(deprecated)_
- [- URLSession:aggregateAssetDownloadTask:didCompleteForMediaSelection:](<urlsession(__aggregateassetdownloadtask_didcompletefor_).md>) — Tells the delegate that a child task finished downloading a media selection. _(deprecated)_
