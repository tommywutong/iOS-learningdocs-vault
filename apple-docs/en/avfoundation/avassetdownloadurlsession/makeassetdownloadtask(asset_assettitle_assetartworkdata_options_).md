---
title: 'makeAssetDownloadTask(asset:assetTitle:assetArtworkData:options:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+（27.0 起废弃）, iPadOS 10.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetdownloadurlsession/makeassetdownloadtask(asset:assettitle:assetartworkdata:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/makeassetdownloadtask(asset:assettitle:assetartworkdata:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadurlsession/makeassetdownloadtask%28asset%3Aassettitle%3Aassetartworkdata%3Aoptions%3A%29.json'
content_hash: 'sha256:951c3226241d75c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadURLSession](../avassetdownloadurlsession.md)

# makeAssetDownloadTask(asset:assetTitle:assetArtworkData:options:)

<sub>Instance Method</sub>

Creates a download task to download the asset.

> [!warning] Deprecated
> Use assetDownloadTaskWithConfiguration: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func makeAssetDownloadTask(asset URLAsset: AVURLAsset, assetTitle title: String, assetArtworkData artworkData: Data?, options: [String : Any]? = nil) -> AVAssetDownloadTask?
```

## Parameters

- `URLAsset` — The HTTP Live Streaming asset to download.

- `title` — A human readable title for this asset in the user’s preferred language. The system displays this value in the usage pane of the Settings app.

- `artworkData` — Optional artwork data for this asset. The system displays the image in the usage pane of the Settings app.

- `options` — Configures custom behavior on the download task. You must provide an options dictionary to download nondefault media selections for HLS assets.

## Return Value

A new download task.

## Discussion

This method may return `nil` if you call it on an invalidated session.

## Topics

### Download option keys

- [AVAssetDownloadTaskMinimumRequiredMediaBitrateKey](../avassetdownloadtaskminimumrequiredmediabitratekey.md) — A key that indicates the minimum bit rate of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMinimumRequiredPresentationSizeKey](../avassetdownloadtaskminimumrequiredpresentationsizekey.md) — A key that indicates the minimum presentation size of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionKey](../avassetdownloadtaskmediaselectionkey.md) — A key that indicates which media selection to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey](../avassetdownloadtaskmediaselectionprefersmultichannelkey.md) — A key that indicates whether the task downloads media selections with support for multichannel playback, when available. _(deprecated)_
- [AVAssetDownloadTaskPrefersHDRKey](../avassetdownloadtaskprefershdrkey.md) — A key that indicates whether the task downloads HDR instead of SDR video, when available. _(deprecated)_
- [AVAssetDownloadTaskPrefersLosslessAudioKey](../avassetdownloadtaskpreferslosslessaudiokey.md) — A key that indicates whether the task downloads media selections in lossless audio format, when available. _(deprecated)_

## See Also

### Creating download tasks

- [- assetDownloadTaskWithConfiguration:](<makeassetdownloadtask(downloadconfiguration_).md>) — Creates a download task that uses the specified configuration.
- [AVAssetDownloadConfiguration](../avassetdownloadconfiguration.md) — An object that provides the configuration for a download task.
- [- aggregateAssetDownloadTaskWithURLAsset:mediaSelections:assetTitle:assetArtworkData:options:](<aggregateassetdownloadtask(with_mediaselections_assettitle_assetartworkdata_options_).md>) — Creates a download task to download the asset and media selections. _(deprecated)_
- [- assetDownloadTaskWithURLAsset:destinationURL:options:](<makeassetdownloadtask(asset_destinationurl_options_).md>) — Creates a download task to download the asset to the indicated location. _(deprecated)_
