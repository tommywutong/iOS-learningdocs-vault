---
title: 'playerItemWithAsset:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/playeritemwithasset:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/playeritemwithasset:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/playeritemwithasset%3A.json'
content_hash: 'sha256:8a26f607b971a3b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# playerItemWithAsset:

<sub>Type Method</sub>

Returns a new player item for a specified asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) playerItemWithAsset:(AVAsset *) asset;
```

## Parameters

- `asset` — The [AVAsset](../avasset.md) to be played.

## Return Value

A new player item, initialized to play `asset`.

## Discussion

This method is equivalent to invoking [playerItemWithAsset:automaticallyLoadedAssetKeys:](playeritemwithasset_automaticallyloadedassetkeys_.md), passing `["duration"]` as the value of `automaticallyLoadedAssetKeys`.

## See Also

### Creating a player item

- [playerItemWithURL:](playeritemwithurl_.md) — Returns a new player item with a specified URL.
- [- initWithURL:](<init(url_)-1xrtk.md>) — Creates a player item with a specified URL.
- [- initWithAsset:](<init(asset_)-87rjl.md>) — Creates a player item for a specified asset.
- [playerItemWithAsset:automaticallyLoadedAssetKeys:](playeritemwithasset_automaticallyloadedassetkeys_.md) — Creates a player item with the specified asset and the asset keys to automatically load.
- [- initWithAsset:automaticallyLoadedAssetKeys:](<init(asset_automaticallyloadedassetkeys_)-8x4.md>) — Creates a player item with the specified asset and the asset keys to automatically load.
