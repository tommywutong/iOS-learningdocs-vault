---
title: 'makeAssetDownloadTask(asset:destinationURL:options:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（10.0 起废弃）, iPadOS 9.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetdownloadurlsession/makeassetdownloadtask(asset:destinationurl:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/makeassetdownloadtask(asset:destinationurl:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadurlsession/makeassetdownloadtask%28asset%3Adestinationurl%3Aoptions%3A%29.json'
content_hash: 'sha256:73feecd798407ed5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadURLSession](../avassetdownloadurlsession.md)

# makeAssetDownloadTask(asset:destinationURL:options:)

<sub>Instance Method</sub>

Creates a download task to download the asset to the indicated location.

> [!warning] Deprecated
> Use [- assetDownloadTaskWithURLAsset:assetTitle:assetArtworkData:options:](<makeassetdownloadtask(asset_assettitle_assetartworkdata_options_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func makeAssetDownloadTask(asset URLAsset: AVURLAsset, destinationURL: URL, options: [String : Any]? = nil) -> AVAssetDownloadTask?
```

## Parameters

- `URLAsset` — The asset to download to the local device.

- `destinationURL` — The local file URL to download the asset to.

- `options` — Configures non-default behavior for the download task. To download nondefault media selections, you must indicate download options.

## Return Value

A new download task.

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
- [- assetDownloadTaskWithURLAsset:assetTitle:assetArtworkData:options:](<makeassetdownloadtask(asset_assettitle_assetartworkdata_options_).md>) — Creates a download task to download the asset. _(deprecated)_
- [- aggregateAssetDownloadTaskWithURLAsset:mediaSelections:assetTitle:assetArtworkData:options:](<aggregateassetdownloadtask(with_mediaselections_assettitle_assetartworkdata_options_).md>) — Creates a download task to download the asset and media selections. _(deprecated)_
