---
title: 'urlSession(_:assetDownloadTask:didReceive:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didreceive:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didreceive:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloaddelegate/urlsession%28_%3Aassetdownloadtask%3Adidreceive%3A%29.json'
content_hash: 'sha256:1e66f21ac43a9678'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadDelegate](../avassetdownloaddelegate.md)

# urlSession(_:assetDownloadTask:didReceive:)

<sub>Instance Method</sub>

Sent when a download task receives an AVMetricEvent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, didReceive metricEvent: AVMetricEvent)
```

## Parameters

- `session` — The NSURLSession corresponding to this AVAssetDownloadTask.

- `assetDownloadTask` — The asset download task.

- `metricEvent` — The metric event received.

## See Also

### Responding to download events

- [- URLSession:assetDownloadTask:didResolveMediaSelection:](<urlsession(__assetdownloadtask_didresolve_).md>) — Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [- URLSession:assetDownloadTask:didLoadTimeRange:totalTimeRangesLoaded:timeRangeExpectedToLoad:](<urlsession(__assetdownloadtask_didload_totaltimerangesloaded_timerangeexpectedtoload_).md>) — Tells the delegate that a download task loaded a new time range. _(deprecated)_
- [- URLSession:assetDownloadTask:didFinishDownloadingToURL:](<urlsession(__assetdownloadtask_didfinishdownloadingto_).md>) — Tells the delegate that a download task finished downloading the requested asset. _(deprecated)_
- [- URLSession:assetDownloadTask:willDownloadVariants:](<urlsession(__assetdownloadtask_willdownloadvariants_).md>) — Tells the delegate that a download task completed variant selection.
- [- URLSession:assetDownloadTask:willDownloadToURL:](<urlsession(__assetdownloadtask_willdownloadto_).md>) — Tells the delegate when a download task determines its download location.
