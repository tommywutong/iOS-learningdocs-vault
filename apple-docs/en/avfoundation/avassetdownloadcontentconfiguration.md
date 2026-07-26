---
title: AVAssetDownloadContentConfiguration
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetdownloadcontentconfiguration
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadcontentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadcontentconfiguration.json'
content_hash: 'sha256:bf98c5fa0a204ae4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadContentConfiguration

<sub>Class</sub>

A configuration object that contains variant qualifiers and media options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAssetDownloadContentConfiguration
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing configuration details

- [variantQualifiers](avassetdownloadcontentconfiguration/variantqualifiers.md) — The variant qualifiers for this configuration.
- [AVAssetVariantQualifier](avassetvariantqualifier.md) — An object that represents an HTTP Live Streaming asset variant.
- [mediaSelections](avassetdownloadcontentconfiguration/mediaselections.md) — The media selections of an asset that a task downloads.

## See Also

### Accessing configuration details

- [artworkData](avassetdownloadconfiguration/artworkdata.md) — A data value that represents the asset’s artwork.
- [primaryContentConfiguration](avassetdownloadconfiguration/primarycontentconfiguration.md) — The configuration for the primary content that the task downloads.
- [auxiliaryContentConfigurations](avassetdownloadconfiguration/auxiliarycontentconfigurations.md) — The configuration for the auxiliary content that the task downloads.
- [optimizesAuxiliaryContentConfigurations](avassetdownloadconfiguration/optimizesauxiliarycontentconfigurations.md) — A Boolean value that indicates whether the task optimizes auxiliary content selection.
- [downloadsInterstitialAssets](avassetdownloadconfiguration/downloadsinterstitialassets.md) — Download interstitial assets as listed in the index file. False by default.
- [- setInterstitialMediaSelectionCriteria:forMediaCharacteristic:](<avassetdownloadconfiguration/setinterstitialmediaselectioncriteria(__formediacharacteristic_).md>) — Sets media selection on interstitials for this asset
