---
title: AVAssetDownloadURLSession
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetdownloadurlsession
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadurlsession.json'
content_hash: 'sha256:3a86237240de0817'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadURLSession

<sub>Class</sub>

A URL session that creates and manages asset download tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class AVAssetDownloadURLSession
```

## Overview

Create an [AVAssetDownloadURLSession](avassetdownloadurlsession.md) by calling [+ sessionWithConfiguration:assetDownloadDelegate:delegateQueue:](<avassetdownloadurlsession/init(configuration_assetdownloaddelegate_delegatequeue_).md>) with a background [URLSessionConfiguration](../foundation/urlsessionconfiguration.md). The background configuration supports reliable downloading while the app is in a suspended state.

> [!important] Important
> The standard `URLSession` initializers and task-creation methods are unavailable on this class. Use [+ sessionWithConfiguration:assetDownloadDelegate:delegateQueue:](<avassetdownloadurlsession/init(configuration_assetdownloaddelegate_delegatequeue_).md>) to create a session and [- assetDownloadTaskWithConfiguration:](<avassetdownloadurlsession/makeassetdownloadtask(downloadconfiguration_).md>) to create download tasks.

Background sessions persist across app launches. The system manages downloads out-of-process so they continue while your app is in a suspended state. If the system terminates your app while downloads are in progress, it relaunches the app and calls [application(_:handleEventsForBackgroundURLSession:completionHandler:)](<../uikit/uiapplicationdelegate/application(__handleeventsforbackgroundurlsession_completionhandler_).md>) with the session identifier. Recreate the [AVAssetDownloadURLSession](avassetdownloadurlsession.md) using the same background configuration identifier to reconnect to the running session and receive pending delegate callbacks. Call the provided completion handler after all callbacks finish. If a person force-quits your app, the system cancels all active downloads and doesn’t relaunch the app.

Mark the background session configuration as discretionary to let the system defer downloads until network and battery conditions are favorable. You can only start a non-discretionary download task while your app is in the foreground. Reserve non-discretionary sessions for downloads that a person explicitly starts. Use a discretionary session for opportunistic downloads that happen without a person’s direct involvement.

Assign an [AVAssetDownloadDelegate](avassetdownloaddelegate.md) to the session to receive download progress, media-selection resolution, and completion callbacks for every download task the session creates.

## Relationships

- **Inherits From**: [URLSession](../foundation/urlsession.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a download session

- [+ sessionWithConfiguration:assetDownloadDelegate:delegateQueue:](<avassetdownloadurlsession/init(configuration_assetdownloaddelegate_delegatequeue_).md>) — Creates a URL session to download assets.
- [AVAssetDownloadDelegate](avassetdownloaddelegate.md) — A protocol that defines the methods to implement to respond to asset-download events.

### Creating download tasks

- [- assetDownloadTaskWithConfiguration:](<avassetdownloadurlsession/makeassetdownloadtask(downloadconfiguration_).md>) — Creates a download task that uses the specified configuration.
- [AVAssetDownloadConfiguration](avassetdownloadconfiguration.md) — An object that provides the configuration for a download task.
- [- assetDownloadTaskWithURLAsset:assetTitle:assetArtworkData:options:](<avassetdownloadurlsession/makeassetdownloadtask(asset_assettitle_assetartworkdata_options_).md>) — Creates a download task to download the asset. _(deprecated)_
- [- aggregateAssetDownloadTaskWithURLAsset:mediaSelections:assetTitle:assetArtworkData:options:](<avassetdownloadurlsession/aggregateassetdownloadtask(with_mediaselections_assettitle_assetartworkdata_options_).md>) — Creates a download task to download the asset and media selections. _(deprecated)_
- [- assetDownloadTaskWithURLAsset:destinationURL:options:](<avassetdownloadurlsession/makeassetdownloadtask(asset_destinationurl_options_).md>) — Creates a download task to download the asset to the indicated location. _(deprecated)_

### Download option keys

- [AVAssetDownloadTaskMinimumRequiredMediaBitrateKey](avassetdownloadtaskminimumrequiredmediabitratekey.md) — A key that indicates the minimum bit rate of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMinimumRequiredPresentationSizeKey](avassetdownloadtaskminimumrequiredpresentationsizekey.md) — A key that indicates the minimum presentation size of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionKey](avassetdownloadtaskmediaselectionkey.md) — A key that indicates which media selection to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey](avassetdownloadtaskmediaselectionprefersmultichannelkey.md) — A key that indicates whether the task downloads media selections with support for multichannel playback, when available. _(deprecated)_
- [AVAssetDownloadTaskPrefersHDRKey](avassetdownloadtaskprefershdrkey.md) — A key that indicates whether the task downloads HDR instead of SDR video, when available. _(deprecated)_
- [AVAssetDownloadTaskPrefersLosslessAudioKey](avassetdownloadtaskpreferslosslessaudiokey.md) — A key that indicates whether the task downloads media selections in lossless audio format, when available. _(deprecated)_

## See Also

### Asset downloading

- [Using AVFoundation to play and persist HTTP live streams](using-avfoundation-to-play-and-persist-http-live-streams.md) — Play HTTP Live Streams and persist streams on disk for offline playback using AVFoundation.
- [AVAssetDownloadTask](avassetdownloadtask.md) — A URL session task that downloads a remote asset to the device for offline playback.
- [AVAggregateAssetDownloadTask](avaggregateassetdownloadtask.md) — A task that downloads multiple media selections for an asset. _(deprecated)_
