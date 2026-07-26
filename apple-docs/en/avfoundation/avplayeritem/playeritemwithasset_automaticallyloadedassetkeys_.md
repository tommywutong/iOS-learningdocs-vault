---
title: 'playerItemWithAsset:automaticallyLoadedAssetKeys:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/playeritemwithasset:automaticallyloadedassetkeys:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/playeritemwithasset:automaticallyloadedassetkeys:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/playeritemwithasset%3Aautomaticallyloadedassetkeys%3A.json'
content_hash: 'sha256:528d2d12f1d0af53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# playerItemWithAsset:automaticallyLoadedAssetKeys:

<sub>Type Method</sub>

Creates a player item with the specified asset and the asset keys to automatically load.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) playerItemWithAsset:(AVAsset *) asset automaticallyLoadedAssetKeys:(NSArray<NSString *> *) automaticallyLoadedAssetKeys;
```

## Parameters

- `asset` — An instance of [AVAsset](../avasset.md).

- `automaticallyLoadedAssetKeys` — An array of strings, each representing a property key defined by [AVAsset](../avasset.md).

## Return Value

An initialized instance of `AVPlayerItem`.

## Discussion

The value of each key in `automaticallyLoadedAssetKeys` will automatically be loaded by the underlying [AVAsset](../avasset.md) before the player item achieves the status [AVPlayerItemStatusReadyToPlay](status-swift.enum/readytoplay.md); i.e. when the item is ready to play, the value returned by invoking the [asset](asset.md) property’s [- statusOfValueForKey:error:](<../avasynchronouskeyvalueloading/statusofvalue(forkey_error_).md>) method will be one of the terminal status values, either [AVKeyValueStatusLoaded](../avkeyvaluestatus/loaded.md), [AVKeyValueStatusFailed](../avkeyvaluestatus/failed.md), or [AVKeyValueStatusCancelled](../avkeyvaluestatus/cancelled.md).

## See Also

### Creating a player item

- [playerItemWithURL:](playeritemwithurl_.md) — Returns a new player item with a specified URL.
- [- initWithURL:](<init(url_)-1xrtk.md>) — Creates a player item with a specified URL.
- [playerItemWithAsset:](playeritemwithasset_.md) — Returns a new player item for a specified asset.
- [- initWithAsset:](<init(asset_)-87rjl.md>) — Creates a player item for a specified asset.
- [- initWithAsset:automaticallyLoadedAssetKeys:](<init(asset_automaticallyloadedassetkeys_)-8x4.md>) — Creates a player item with the specified asset and the asset keys to automatically load.
