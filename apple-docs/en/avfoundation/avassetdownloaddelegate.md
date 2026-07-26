---
title: AVAssetDownloadDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetdownloaddelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloaddelegate.json'
content_hash: 'sha256:1df35ec36e25921b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadDelegate

<sub>Protocol</sub>

A protocol that defines the methods to implement to respond to asset-download events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
protocol AVAssetDownloadDelegate : URLSessionTaskDelegate
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [URLSessionDelegate](../foundation/urlsessiondelegate.md), [URLSessionTaskDelegate](../foundation/urlsessiontaskdelegate.md)

## Topics

### Responding to download events

- [- URLSession:assetDownloadTask:didResolveMediaSelection:](<avassetdownloaddelegate/urlsession(__assetdownloadtask_didresolve_).md>) — Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [- URLSession:assetDownloadTask:didLoadTimeRange:totalTimeRangesLoaded:timeRangeExpectedToLoad:](<avassetdownloaddelegate/urlsession(__assetdownloadtask_didload_totaltimerangesloaded_timerangeexpectedtoload_).md>) — Tells the delegate that a download task loaded a new time range. _(deprecated)_
- [- URLSession:assetDownloadTask:didFinishDownloadingToURL:](<avassetdownloaddelegate/urlsession(__assetdownloadtask_didfinishdownloadingto_).md>) — Tells the delegate that a download task finished downloading the requested asset. _(deprecated)_
- [- URLSession:assetDownloadTask:willDownloadVariants:](<avassetdownloaddelegate/urlsession(__assetdownloadtask_willdownloadvariants_).md>) — Tells the delegate that a download task completed variant selection.
- [- URLSession:assetDownloadTask:willDownloadToURL:](<avassetdownloaddelegate/urlsession(__assetdownloadtask_willdownloadto_).md>) — Tells the delegate when a download task determines its download location.
- [- URLSession:assetDownloadTask:didReceiveMetricEvent:](<avassetdownloaddelegate/urlsession(__assetdownloadtask_didreceive_).md>) — Sent when a download task receives an AVMetricEvent.

### Responding to aggregate download events

- [- URLSession:aggregateAssetDownloadTask:willDownloadToURL:](<avassetdownloaddelegate/urlsession(__aggregateassetdownloadtask_willdownloadto_).md>) — Tells the delegate the final location of the asset when the download completes. _(deprecated)_
- [- URLSession:aggregateAssetDownloadTask:didLoadTimeRange:totalTimeRangesLoaded:timeRangeExpectedToLoad:forMediaSelection:](<avassetdownloaddelegate/urlsession(__aggregateassetdownloadtask_didload_totaltimerangesloaded_timerangeexpectedtoload_for_).md>) — Tells the delegate that the aggregate download task loaded a new time range. _(deprecated)_
- [- URLSession:aggregateAssetDownloadTask:didCompleteForMediaSelection:](<avassetdownloaddelegate/urlsession(__aggregateassetdownloadtask_didcompletefor_).md>) — Tells the delegate that a child task finished downloading a media selection. _(deprecated)_

## See Also

### Creating a download session

- [+ sessionWithConfiguration:assetDownloadDelegate:delegateQueue:](<avassetdownloadurlsession/init(configuration_assetdownloaddelegate_delegatequeue_).md>) — Creates a URL session to download assets.
