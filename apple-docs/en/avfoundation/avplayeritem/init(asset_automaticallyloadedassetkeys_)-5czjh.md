---
title: 'init(asset:automaticallyLoadedAssetKeys:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/init(asset:automaticallyloadedassetkeys:)-5czjh'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/init(asset:automaticallyloadedassetkeys:)-5czjh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/init%28asset%3Aautomaticallyloadedassetkeys%3A%29-5czjh.json'
content_hash: 'sha256:6895959431cdf0ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# init(asset:automaticallyLoadedAssetKeys:)

<sub>Initializer</sub>

Creates a player item for the asset, and automatically loads values for the specified properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency convenience init(asset: AVAsset, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>] = [])
```

## Parameters

- `asset` — The asset to play.

- `automaticallyLoadedAssetKeys` — An array of property identifiers for which the system automatically loads a value.

## Discussion

The system automatically loads values for the specified property identifiers before the player item reaches an [AVPlayerItemStatusReadyToPlay](status-swift.enum/readytoplay.md) state. In this state, calling [status(of:)](<../avasynchronouskeyvalueloading/status(of_).md>) on a specified property identifier returns a value of [AVAsyncProperty.Status.loaded(_:)](<../avasyncproperty/status/loaded(__).md>) or [AVAsyncProperty.Status.failed(_:)](<../avasyncproperty/status/failed(__).md>).

## See Also

### Creating a player item

- [- initWithURL:](<init(url_)-1xrtk.md>) — Creates a player item with a specified URL.
- [- initWithAsset:](<init(asset_)-87rjl.md>) — Creates a player item for a specified asset.
- [init(asset:)](<init(asset_)-1nme9.md>)
- [init(asset:automaticallyLoadedAssetKeys:)](<init(asset_automaticallyloadedassetkeys_)-85hal.md>)
- [- initWithAsset:automaticallyLoadedAssetKeys:](<init(asset_automaticallyloadedassetkeys_)-8x4.md>) — Creates a player item with the specified asset and the asset keys to automatically load.
