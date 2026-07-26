---
title: 'urlSession(_:assetDownloadTask:willDownloadVariants:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadvariants:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadvariants:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloaddelegate/urlsession%28_%3Aassetdownloadtask%3Awilldownloadvariants%3A%29.json'
content_hash: 'sha256:d550c0476318b1b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadDelegate](../avassetdownloaddelegate.md)

# urlSession(_:assetDownloadTask:willDownloadVariants:)

<sub>Instance Method</sub>

Tells the delegate that a download task completed variant selection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadVariants variants: [AVAssetVariant])
```

## Parameters

- `session` — The session the asset download task is on.

- `assetDownloadTask` — The task that finished selecting variant selection.

- `variants` — The asset variants to download.

## See Also

### Responding to download events

- [- URLSession:assetDownloadTask:didResolveMediaSelection:](<urlsession(__assetdownloadtask_didresolve_).md>) — Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [- URLSession:assetDownloadTask:didLoadTimeRange:totalTimeRangesLoaded:timeRangeExpectedToLoad:](<urlsession(__assetdownloadtask_didload_totaltimerangesloaded_timerangeexpectedtoload_).md>) — Tells the delegate that a download task loaded a new time range. _(deprecated)_
- [- URLSession:assetDownloadTask:didFinishDownloadingToURL:](<urlsession(__assetdownloadtask_didfinishdownloadingto_).md>) — Tells the delegate that a download task finished downloading the requested asset. _(deprecated)_
- [- URLSession:assetDownloadTask:willDownloadToURL:](<urlsession(__assetdownloadtask_willdownloadto_).md>) — Tells the delegate when a download task determines its download location.
- [- URLSession:assetDownloadTask:didReceiveMetricEvent:](<urlsession(__assetdownloadtask_didreceive_).md>) — Sent when a download task receives an AVMetricEvent.
