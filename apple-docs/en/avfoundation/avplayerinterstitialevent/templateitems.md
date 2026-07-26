---
title: templateItems
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/templateitems
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/templateitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/templateitems.json'
content_hash: 'sha256:88eee2e750e4032a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# templateItems

<sub>Instance Property</sub>

An array of player item configurations to use as templates for player items that play interstitial content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var templateItems: [AVPlayerItem] { get set }
```

## Discussion

If you require the system to create new player items using the same asset instance as the template item, create the asset with an [AVURLAssetPrimarySessionIdentifierKey](../avurlassetprimarysessionidentifierkey.md) value equal to [httpSessionIdentifier](../avurlasset/httpsessionidentifier.md) of the primary item’s [asset](../avplayeritem/asset.md). Creating assets this way simplifies cases where you require loading their data with a custom [AVAssetResourceLoader](../avassetresourceloader.md) delegate.

> [!important] Important
> The system raises an exception if template items contain assets that aren’t URL based, such as [AVComposition](../avcomposition.md).

## See Also

### Accessing player items

- [primaryItem](primaryitem.md) — The player item that represents the primary content.
