---
title: 'urlSession(_:aggregateAssetDownloadTask:didLoad:totalTimeRangesLoaded:timeRangeExpectedToLoad:for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloaddelegate/urlsession%28_%3Aaggregateassetdownloadtask%3Adidload%3Atotaltimerangesloaded%3Atimerangeexpectedtoload%3Afor%3A%29.json'
content_hash: 'sha256:815bc152122426e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadDelegate](../avassetdownloaddelegate.md)

# urlSession(_:aggregateAssetDownloadTask:didLoad:totalTimeRangesLoaded:timeRangeExpectedToLoad:for:)

<sub>Instance Method</sub>

Tells the delegate that the aggregate download task loaded a new time range.

> [!warning] Deprecated
> Use NSURLSessionTask.progress: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func urlSession(_ session: URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, didLoad timeRange: CMTimeRange, totalTimeRangesLoaded loadedTimeRanges: [NSValue], timeRangeExpectedToLoad: CMTimeRange, for mediaSelection: AVMediaSelection)
```

## Parameters

- `session` — The session the asset download task is on.

- `aggregateAssetDownloadTask` — The download task that loaded a new time range.

- `timeRange` — A [CMTimeRange](../../coremedia/cmtimerange.md) value that indicates the time range the task loaded since the last call to this method.

- `loadedTimeRanges` — An array of CMTimeRange values that indicate the time ranges the task has downloaded so far.

- `timeRangeExpectedToLoad` — A CMTimeRange value that indicates the expected duration of the downloaded asset.

- `mediaSelection` — The media selection the task is downloading.

## See Also

### Responding to aggregate download events

- [- URLSession:aggregateAssetDownloadTask:willDownloadToURL:](<urlsession(__aggregateassetdownloadtask_willdownloadto_).md>) — Tells the delegate the final location of the asset when the download completes. _(deprecated)_
- [- URLSession:aggregateAssetDownloadTask:didCompleteForMediaSelection:](<urlsession(__aggregateassetdownloadtask_didcompletefor_).md>) — Tells the delegate that a child task finished downloading a media selection. _(deprecated)_
