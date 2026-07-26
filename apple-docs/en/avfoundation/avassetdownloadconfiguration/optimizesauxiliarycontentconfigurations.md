---
title: optimizesAuxiliaryContentConfigurations
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetdownloadconfiguration/optimizesauxiliarycontentconfigurations
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadconfiguration/optimizesauxiliarycontentconfigurations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadconfiguration/optimizesauxiliarycontentconfigurations.json'
content_hash: 'sha256:f9d53f7fad92f1d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadConfiguration](../avassetdownloadconfiguration.md)

# optimizesAuxiliaryContentConfigurations

<sub>Instance Property</sub>

A Boolean value that indicates whether the task optimizes auxiliary content selection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var optimizesAuxiliaryContentConfigurations: Bool { get set }
```

## Discussion

By default, a download task optimizes its selection of auxiliary content based on its primary download content. For example, if the primary content configuration represents stereo renditions, and auxiliary content configuration represents multichannel audio renditions, the task choses the auxiliary multichannel variant to avoid downloading duplicate video renditions.

## See Also

### Accessing configuration details

- [artworkData](artworkdata.md) — A data value that represents the asset’s artwork.
- [primaryContentConfiguration](primarycontentconfiguration.md) — The configuration for the primary content that the task downloads.
- [auxiliaryContentConfigurations](auxiliarycontentconfigurations.md) — The configuration for the auxiliary content that the task downloads.
- [AVAssetDownloadContentConfiguration](../avassetdownloadcontentconfiguration.md) — A configuration object that contains variant qualifiers and media options.
- [downloadsInterstitialAssets](downloadsinterstitialassets.md) — Download interstitial assets as listed in the index file. False by default.
- [- setInterstitialMediaSelectionCriteria:forMediaCharacteristic:](<setinterstitialmediaselectioncriteria(__formediacharacteristic_).md>) — Sets media selection on interstitials for this asset
