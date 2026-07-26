---
title: 'urlSession(_:assetDownloadTask:didFinishDownloadingTo:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+（27.0 起废弃）, iPadOS 10.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didfinishdownloadingto:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didfinishdownloadingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloaddelegate/urlsession%28_%3Aassetdownloadtask%3Adidfinishdownloadingto%3A%29.json'
content_hash: 'sha256:8d58e75a8632d655'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadDelegate](../avassetdownloaddelegate.md)

# urlSession(_:assetDownloadTask:didFinishDownloadingTo:)

<sub>Instance Method</sub>

Tells the delegate that a download task finished downloading the requested asset.

> [!warning] Deprecated
> Use URLSession:assetDownloadTask:willDownloadToURL: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, didFinishDownloadingTo location: URL)
```

## Parameters

- `session` — The session the asset download task is on.

- `assetDownloadTask` — The download task whose downloaded completed.

- `location` — The download location of the asset.

## Discussion

Don’t move the downloaded asset from this location. Downloaded assets must remain at the system-provided URL. Instead, save a persistent reference to this URL for future use.

## See Also

### Responding to download events

- [- URLSession:assetDownloadTask:didResolveMediaSelection:](<urlsession(__assetdownloadtask_didresolve_).md>) — Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [- URLSession:assetDownloadTask:didLoadTimeRange:totalTimeRangesLoaded:timeRangeExpectedToLoad:](<urlsession(__assetdownloadtask_didload_totaltimerangesloaded_timerangeexpectedtoload_).md>) — Tells the delegate that a download task loaded a new time range. _(deprecated)_
- [- URLSession:assetDownloadTask:willDownloadVariants:](<urlsession(__assetdownloadtask_willdownloadvariants_).md>) — Tells the delegate that a download task completed variant selection.
- [- URLSession:assetDownloadTask:willDownloadToURL:](<urlsession(__assetdownloadtask_willdownloadto_).md>) — Tells the delegate when a download task determines its download location.
- [- URLSession:assetDownloadTask:didReceiveMetricEvent:](<urlsession(__assetdownloadtask_didreceive_).md>) — Sent when a download task receives an AVMetricEvent.
