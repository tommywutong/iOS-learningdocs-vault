---
title: artworkData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetdownloadconfiguration/artworkdata
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadconfiguration/artworkdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadconfiguration/artworkdata.json'
content_hash: 'sha256:6ddd8ddecde855dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadConfiguration](../avassetdownloadconfiguration.md)

# artworkData

<sub>Instance Property</sub>

A data value that represents the asset’s artwork.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var artworkData: Data? { get set }
```

## Discussion

The system displays this image in the usage pane of the Settings app.

## See Also

### Accessing configuration details

- [primaryContentConfiguration](primarycontentconfiguration.md) — The configuration for the primary content that the task downloads.
- [auxiliaryContentConfigurations](auxiliarycontentconfigurations.md) — The configuration for the auxiliary content that the task downloads.
- [AVAssetDownloadContentConfiguration](../avassetdownloadcontentconfiguration.md) — A configuration object that contains variant qualifiers and media options.
- [optimizesAuxiliaryContentConfigurations](optimizesauxiliarycontentconfigurations.md) — A Boolean value that indicates whether the task optimizes auxiliary content selection.
- [downloadsInterstitialAssets](downloadsinterstitialassets.md) — Download interstitial assets as listed in the index file. False by default.
- [- setInterstitialMediaSelectionCriteria:forMediaCharacteristic:](<setinterstitialmediaselectioncriteria(__formediacharacteristic_).md>) — Sets media selection on interstitials for this asset
