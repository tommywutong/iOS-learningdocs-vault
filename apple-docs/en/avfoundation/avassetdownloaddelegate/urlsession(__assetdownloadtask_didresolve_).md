---
title: 'urlSession(_:assetDownloadTask:didResolve:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didresolve:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didresolve:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloaddelegate/urlsession%28_%3Aassetdownloadtask%3Adidresolve%3A%29.json'
content_hash: 'sha256:c39cc5c93db2ee25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadDelegate](../avassetdownloaddelegate.md)

# urlSession(_:assetDownloadTask:didResolve:)

<sub>Instance Method</sub>

Tells the delegate that a download task resolved the media selection to download, including any automatic selections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, didResolve resolvedMediaSelection: AVMediaSelection)
```

## Parameters

- `session` — The session the asset download task is on.

- `assetDownloadTask` — The task that resolved the media selection.

- `resolvedMediaSelection` — The media selection the task resolved.

## Discussion

For the best chance of playing back downloaded content without further network I/O, set this selection on the associated [AVPlayerItem](../avplayeritem.md).

## See Also

### Responding to download events

- [- URLSession:assetDownloadTask:didLoadTimeRange:totalTimeRangesLoaded:timeRangeExpectedToLoad:](<urlsession(__assetdownloadtask_didload_totaltimerangesloaded_timerangeexpectedtoload_).md>) — Tells the delegate that a download task loaded a new time range. _(deprecated)_
- [- URLSession:assetDownloadTask:didFinishDownloadingToURL:](<urlsession(__assetdownloadtask_didfinishdownloadingto_).md>) — Tells the delegate that a download task finished downloading the requested asset. _(deprecated)_
- [- URLSession:assetDownloadTask:willDownloadVariants:](<urlsession(__assetdownloadtask_willdownloadvariants_).md>) — Tells the delegate that a download task completed variant selection.
- [- URLSession:assetDownloadTask:willDownloadToURL:](<urlsession(__assetdownloadtask_willdownloadto_).md>) — Tells the delegate when a download task determines its download location.
- [- URLSession:assetDownloadTask:didReceiveMetricEvent:](<urlsession(__assetdownloadtask_didreceive_).md>) — Sent when a download task receives an AVMetricEvent.
