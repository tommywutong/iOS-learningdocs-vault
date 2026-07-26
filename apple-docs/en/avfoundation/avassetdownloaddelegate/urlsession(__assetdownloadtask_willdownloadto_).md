---
title: 'urlSession(_:assetDownloadTask:willDownloadTo:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 14.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadto:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloaddelegate/urlsession%28_%3Aassetdownloadtask%3Awilldownloadto%3A%29.json'
content_hash: 'sha256:df45a36139f78d98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadDelegate](../avassetdownloaddelegate.md)

# urlSession(_:assetDownloadTask:willDownloadTo:)

<sub>Instance Method</sub>

Tells the delegate when a download task determines its download location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadTo location: URL)
```

## Parameters

- `session` — The session the asset download task is on.

- `assetDownloadTask` — The download task.

- `location` — The URL the task downloads the asset to.

## Discussion

Save the returned URL to instantiate the asset in the future.

## See Also

### Responding to download events

- [- URLSession:assetDownloadTask:didResolveMediaSelection:](<urlsession(__assetdownloadtask_didresolve_).md>) — Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [- URLSession:assetDownloadTask:didLoadTimeRange:totalTimeRangesLoaded:timeRangeExpectedToLoad:](<urlsession(__assetdownloadtask_didload_totaltimerangesloaded_timerangeexpectedtoload_).md>) — Tells the delegate that a download task loaded a new time range. _(deprecated)_
- [- URLSession:assetDownloadTask:didFinishDownloadingToURL:](<urlsession(__assetdownloadtask_didfinishdownloadingto_).md>) — Tells the delegate that a download task finished downloading the requested asset. _(deprecated)_
- [- URLSession:assetDownloadTask:willDownloadVariants:](<urlsession(__assetdownloadtask_willdownloadvariants_).md>) — Tells the delegate that a download task completed variant selection.
- [- URLSession:assetDownloadTask:didReceiveMetricEvent:](<urlsession(__assetdownloadtask_didreceive_).md>) — Sent when a download task receives an AVMetricEvent.
