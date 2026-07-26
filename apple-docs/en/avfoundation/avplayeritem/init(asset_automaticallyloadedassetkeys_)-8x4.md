---
title: 'init(asset:automaticallyLoadedAssetKeys:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/init(asset:automaticallyloadedassetkeys:)-8x4'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/init(asset:automaticallyloadedassetkeys:)-8x4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/init%28asset%3Aautomaticallyloadedassetkeys%3A%29-8x4.json'
content_hash: 'sha256:108ea38765176b86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# init(asset:automaticallyLoadedAssetKeys:)

<sub>Initializer</sub>

Creates a player item with the specified asset and the asset keys to automatically load.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(asset: AVAsset, automaticallyLoadedAssetKeys: [String]?)
```

## Parameters

- `asset` — An instance of [AVAsset](../avasset.md).

- `automaticallyLoadedAssetKeys` — An array of strings, each representing a property defined by [AVAsset](../avasset.md).

## Return Value

An initialized instance of `AVPlayerItem`.

## Discussion

The value of each key in `automaticallyLoadedAssetKeys` will automatically be loaded by the underlying [AVAsset](../avasset.md) before the player item achieves the status [AVPlayerItemStatusReadyToPlay](status-swift.enum/readytoplay.md); i.e. when the item is ready to play, the value returned by invoking the [asset](asset.md) property’s [- statusOfValueForKey:error:](<../avasynchronouskeyvalueloading/statusofvalue(forkey_error_).md>) method will be one of the terminal status values, either [AVKeyValueStatusLoaded](../avkeyvaluestatus/loaded.md), [AVKeyValueStatusFailed](../avkeyvaluestatus/failed.md), or [AVKeyValueStatusCancelled](../avkeyvaluestatus/cancelled.md).

## See Also

### Creating a player item

- [- initWithURL:](<init(url_)-1xrtk.md>) — Creates a player item with a specified URL.
- [- initWithAsset:](<init(asset_)-87rjl.md>) — Creates a player item for a specified asset.
- [init(asset:)](<init(asset_)-1nme9.md>)
- [init(asset:automaticallyLoadedAssetKeys:)](<init(asset_automaticallyloadedassetkeys_)-5czjh.md>) — Creates a player item for the asset, and automatically loads values for the specified properties.
- [init(asset:automaticallyLoadedAssetKeys:)](<init(asset_automaticallyloadedassetkeys_)-85hal.md>)
