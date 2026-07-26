---
title: AVAssetDownloadTask
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetdownloadtask
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadtask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadtask.json'
content_hash: 'sha256:fb044dced65f832b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadTask

<sub>Class</sub>

A URL session task that downloads a remote asset to the device for offline playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class AVAssetDownloadTask
```

## Overview

You create instances of this class by calling [- assetDownloadTaskWithConfiguration:](<avassetdownloadurlsession/makeassetdownloadtask(downloadconfiguration_).md>) on the download session.

To play an asset while its download is in progress, reuse the [AVURLAsset](avurlasset.md) you supplied to the download configuration. The asset reads locally cached segments during concurrent playback when the streaming variant matches the downloading variant.

Adopt the [AVAssetDownloadDelegate](avassetdownloaddelegate.md) protocol to receive progress and completion callbacks. Use the inherited [progress](../foundation/urlsessiontask/progress.md) property for numeric download progress updates. The delegate method [- URLSession:assetDownloadTask:willDownloadToURL:](<avassetdownloaddelegate/urlsession(__assetdownloadtask_willdownloadto_).md>) provides the local file URL where the system stores the asset.

> [!important] Important
> Save the local file URL the delegate provides. You need it to reconstruct the offline [AVURLAsset](avurlasset.md) on subsequent app launches.

To augment an existing download, initialize a new task with an [AVURLAsset](avurlasset.md) whose URL references the downloaded asset on disk. For example, you can add media selections that you didn’t include in the original download.

### Live Activity

To control how the system schedules downloads, set the `isDiscretionary` property on the [URLSessionConfiguration](../foundation/urlsessionconfiguration.md) you pass when creating the [AVAssetDownloadURLSession](avassetdownloadurlsession.md). Non-discretionary downloads start as soon as possible. The system defers discretionary downloads until conditions like network and battery state are favorable, and runs them silently in the background.

On supported platforms, a non-discretionary download displays a Live Activity on the Lock Screen and in the Dynamic Island that shows real-time download progress. Discretionary downloads don’t display a Live Activity.

When your app has multiple active downloads, the system aggregates them into a single Live Activity that shows combined progress. For a single active download, the activity title displays the asset title.

If any downloads in the group fail, the Live Activity transitions to a failure state after all downloads finish. A person can also cancel all active and queued downloads for your app directly from the Live Activity, which causes the tasks to fail with `NSUserCancelledError` in the `NSCocoaErrorDomain` domain.

The Live Activity doesn’t reflect download tasks until you resume them. If you resume a task while your app runs in the background, the system might demote it to discretionary. The system queues downloads in the order you resume them.

Swift subclasses of this type must conform to [Sendable](../swift/sendable.md).

## Relationships

- **Inherits From**: [URLSessionTask](../foundation/urlsessiontask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ProgressReporting](../foundation/progressreporting.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing task information

- [URLAsset](avassetdownloadtask/urlasset.md) — The asset that this task downloads.
- [loadedTimeRanges](avassetdownloadtask/loadedtimeranges.md) — The time ranges of the downloaded media that are ready for playback. _(deprecated)_
- [options](avassetdownloadtask/options.md) — The configuration options for the task. _(deprecated)_
- [destinationURL](avassetdownloadtask/destinationurl.md) — The local file URL to where the task downloads the asset. _(deprecated)_

## See Also

### Asset downloading

- [Using AVFoundation to play and persist HTTP live streams](using-avfoundation-to-play-and-persist-http-live-streams.md) — Play HTTP Live Streams and persist streams on disk for offline playback using AVFoundation.
- [AVAssetDownloadURLSession](avassetdownloadurlsession.md) — A URL session that creates and manages asset download tasks.
- [AVAggregateAssetDownloadTask](avaggregateassetdownloadtask.md) — A task that downloads multiple media selections for an asset. _(deprecated)_
