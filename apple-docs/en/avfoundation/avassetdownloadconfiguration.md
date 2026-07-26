---
title: AVAssetDownloadConfiguration
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetdownloadconfiguration
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadconfiguration.json'
content_hash: 'sha256:985e6cf95a1175e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadConfiguration

<sub>Class</sub>

An object that provides the configuration for a download task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAssetDownloadConfiguration
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a configuration

- [+ downloadConfigurationWithAsset:title:](<avassetdownloadconfiguration/init(asset_title_).md>) — Creates a download configuration for a media asset.

### Accessing configuration details

- [artworkData](avassetdownloadconfiguration/artworkdata.md) — A data value that represents the asset’s artwork.
- [primaryContentConfiguration](avassetdownloadconfiguration/primarycontentconfiguration.md) — The configuration for the primary content that the task downloads.
- [auxiliaryContentConfigurations](avassetdownloadconfiguration/auxiliarycontentconfigurations.md) — The configuration for the auxiliary content that the task downloads.
- [AVAssetDownloadContentConfiguration](avassetdownloadcontentconfiguration.md) — A configuration object that contains variant qualifiers and media options.
- [optimizesAuxiliaryContentConfigurations](avassetdownloadconfiguration/optimizesauxiliarycontentconfigurations.md) — A Boolean value that indicates whether the task optimizes auxiliary content selection.
- [downloadsInterstitialAssets](avassetdownloadconfiguration/downloadsinterstitialassets.md) — Download interstitial assets as listed in the index file. False by default.
- [- setInterstitialMediaSelectionCriteria:forMediaCharacteristic:](<avassetdownloadconfiguration/setinterstitialmediaselectioncriteria(__formediacharacteristic_).md>) — Sets media selection on interstitials for this asset

## See Also

### Creating download tasks

- [- assetDownloadTaskWithConfiguration:](<avassetdownloadurlsession/makeassetdownloadtask(downloadconfiguration_).md>) — Creates a download task that uses the specified configuration.
- [- assetDownloadTaskWithURLAsset:assetTitle:assetArtworkData:options:](<avassetdownloadurlsession/makeassetdownloadtask(asset_assettitle_assetartworkdata_options_).md>) — Creates a download task to download the asset. _(deprecated)_
- [- aggregateAssetDownloadTaskWithURLAsset:mediaSelections:assetTitle:assetArtworkData:options:](<avassetdownloadurlsession/aggregateassetdownloadtask(with_mediaselections_assettitle_assetartworkdata_options_).md>) — Creates a download task to download the asset and media selections. _(deprecated)_
- [- assetDownloadTaskWithURLAsset:destinationURL:options:](<avassetdownloadurlsession/makeassetdownloadtask(asset_destinationurl_options_).md>) — Creates a download task to download the asset to the indicated location. _(deprecated)_
