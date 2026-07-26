---
title: downloadsInterstitialAssets
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetdownloadconfiguration/downloadsinterstitialassets
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadconfiguration/downloadsinterstitialassets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadconfiguration/downloadsinterstitialassets.json'
content_hash: 'sha256:188ba74d1448978d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadConfiguration](../avassetdownloadconfiguration.md)

# downloadsInterstitialAssets

<sub>Instance Property</sub>

Download interstitial assets as listed in the index file. False by default.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var downloadsInterstitialAssets: Bool { get set }
```

## Discussion

Ordinarily, interstitial assets are skipped when downloading content for later playback. Setting this property to true will cause interstitial assets to be downloaded as well. Playback of the downloaded content can then match the experience of online streaming playback as closely as possible.

## See Also

### Accessing configuration details

- [artworkData](artworkdata.md) — A data value that represents the asset’s artwork.
- [primaryContentConfiguration](primarycontentconfiguration.md) — The configuration for the primary content that the task downloads.
- [auxiliaryContentConfigurations](auxiliarycontentconfigurations.md) — The configuration for the auxiliary content that the task downloads.
- [AVAssetDownloadContentConfiguration](../avassetdownloadcontentconfiguration.md) — A configuration object that contains variant qualifiers and media options.
- [optimizesAuxiliaryContentConfigurations](optimizesauxiliarycontentconfigurations.md) — A Boolean value that indicates whether the task optimizes auxiliary content selection.
- [- setInterstitialMediaSelectionCriteria:forMediaCharacteristic:](<setinterstitialmediaselectioncriteria(__formediacharacteristic_).md>) — Sets media selection on interstitials for this asset
