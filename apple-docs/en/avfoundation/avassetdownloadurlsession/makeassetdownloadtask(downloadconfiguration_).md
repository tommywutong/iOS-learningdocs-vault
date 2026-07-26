---
title: 'makeAssetDownloadTask(downloadConfiguration:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetdownloadurlsession/makeassetdownloadtask(downloadconfiguration:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/makeassetdownloadtask(downloadconfiguration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadurlsession/makeassetdownloadtask%28downloadconfiguration%3A%29.json'
content_hash: 'sha256:1a3c84fde9023c95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadURLSession](../avassetdownloadurlsession.md)

# makeAssetDownloadTask(downloadConfiguration:)

<sub>Instance Method</sub>

Creates a download task that uses the specified configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func makeAssetDownloadTask(downloadConfiguration: AVAssetDownloadConfiguration) -> AVAssetDownloadTask
```

## Parameters

- `downloadConfiguration` — The configuration that the task uses.

## Return Value

A new download task.

## Discussion

This method raises an exception if you call it on an invalidated session.

## See Also

### Creating download tasks

- [AVAssetDownloadConfiguration](../avassetdownloadconfiguration.md) — An object that provides the configuration for a download task.
- [- assetDownloadTaskWithURLAsset:assetTitle:assetArtworkData:options:](<makeassetdownloadtask(asset_assettitle_assetartworkdata_options_).md>) — Creates a download task to download the asset. _(deprecated)_
- [- aggregateAssetDownloadTaskWithURLAsset:mediaSelections:assetTitle:assetArtworkData:options:](<aggregateassetdownloadtask(with_mediaselections_assettitle_assetartworkdata_options_).md>) — Creates a download task to download the asset and media selections. _(deprecated)_
- [- assetDownloadTaskWithURLAsset:destinationURL:options:](<makeassetdownloadtask(asset_destinationurl_options_).md>) — Creates a download task to download the asset to the indicated location. _(deprecated)_
