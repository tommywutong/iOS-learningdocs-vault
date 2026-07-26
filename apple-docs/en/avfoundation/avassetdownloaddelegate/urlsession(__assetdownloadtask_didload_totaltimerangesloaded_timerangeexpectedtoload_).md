---
title: 'urlSession(_:assetDownloadTask:didLoad:totalTimeRangesLoaded:timeRangeExpectedToLoad:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloaddelegate/urlsession%28_%3Aassetdownloadtask%3Adidload%3Atotaltimerangesloaded%3Atimerangeexpectedtoload%3A%29.json'
content_hash: 'sha256:2454718540b2633a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadDelegate](../avassetdownloaddelegate.md)

# urlSession(_:assetDownloadTask:didLoad:totalTimeRangesLoaded:timeRangeExpectedToLoad:)

<sub>Instance Method</sub>

Tells the delegate that a download task loaded a new time range.

> [!warning] Deprecated
> Use NSURLSessionTask.progress instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, didLoad timeRange: CMTimeRange, totalTimeRangesLoaded loadedTimeRanges: [NSValue], timeRangeExpectedToLoad: CMTimeRange)
```

## Parameters

- `session` — The session the asset download task is on.

- `assetDownloadTask` — The download task that loaded a new time range.

- `timeRange` — A [CMTimeRange](../../coremedia/cmtimerange.md) value that indicates the time range the task loaded since the last call to this method.

- `loadedTimeRanges` — An array of [CMTimeRange](../../coremedia/cmtimerange.md) values that indicate the time ranges the task has downloaded so far.

- `timeRangeExpectedToLoad` — A [CMTimeRange](../../coremedia/cmtimerange.md) value that indicates the expected duration of the downloaded asset.

## Discussion

Implement this method to track the download status of an asset. The following example shows how to calculate the percentage complete for the current download.

**Swift**

```swift
func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, didLoad timeRange: CMTimeRange, totalTimeRangesLoaded loadedTimeRanges: [NSValue], timeRangeExpectedToLoad: CMTimeRange) {
    var percentageComplete = 0.0
    // Iterate over loaded time ranges
    for value in loadedTimeRanges {
        // Unpack CMTimeRange value
        let loadedTimeRange = value.timeRangeValue
        percentageComplete += loadedTimeRange.duration.seconds / timeRangeExpectedToLoad.duration.seconds
    }
    percentageComplete *= 100
    // Updated interested observers of percentage change
}
```

**Objective-C**

```objc
- (void)URLSession:(NSURLSession *)session assetDownloadTask:(AVAssetDownloadTask *)assetDownloadTask
                                            didLoadTimeRange:(CMTimeRange)timeRange
                                       totalTimeRangesLoaded:(NSArray<NSValue *> *)loadedTimeRanges
                                     timeRangeExpectedToLoad:(CMTimeRange)timeRangeExpectedToLoad {
    double percentageComplete = 0.0f;
    // Iterate over loaded time ranges
    for (NSValue *value in loadedTimeRanges) {
        // Unpack CMTimeRange value
        CMTimeRange loadedTimeRange = value.CMTimeRangeValue;
        percentageComplete +=
            CMTimeGetSeconds(loadedTimeRange.duration) / CMTimeGetSeconds(timeRangeExpectedToLoad.duration);
    }
    percentageComplete *= 100;
    // Updated interested observers of percentage change
}
```

## See Also

### Responding to download events

- [- URLSession:assetDownloadTask:didResolveMediaSelection:](<urlsession(__assetdownloadtask_didresolve_).md>) — Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [- URLSession:assetDownloadTask:didFinishDownloadingToURL:](<urlsession(__assetdownloadtask_didfinishdownloadingto_).md>) — Tells the delegate that a download task finished downloading the requested asset. _(deprecated)_
- [- URLSession:assetDownloadTask:willDownloadVariants:](<urlsession(__assetdownloadtask_willdownloadvariants_).md>) — Tells the delegate that a download task completed variant selection.
- [- URLSession:assetDownloadTask:willDownloadToURL:](<urlsession(__assetdownloadtask_willdownloadto_).md>) — Tells the delegate when a download task determines its download location.
- [- URLSession:assetDownloadTask:didReceiveMetricEvent:](<urlsession(__assetdownloadtask_didreceive_).md>) — Sent when a download task receives an AVMetricEvent.
