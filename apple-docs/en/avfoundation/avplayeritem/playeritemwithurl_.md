---
title: 'playerItemWithURL:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/playeritemwithurl:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/playeritemwithurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/playeritemwithurl%3A.json'
content_hash: 'sha256:295dccc7504ea7ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# playerItemWithURL:

<sub>Type Method</sub>

Returns a new player item with a specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) playerItemWithURL:(NSURL *) URL;
```

## Parameters

- `URL` — A URL identifying the media resource to be played.

## Return Value

A new player item, prepared to use `URL`.

## Discussion

This method immediately returns the item, but with the status [AVPlayerItemStatusUnknown](status-swift.enum/unknown.md).

Associating the player item with an [AVPlayer](../avplayer.md) immediately begins enqueuing its media and preparing it for playback. If the URL contains valid data that can be used by the player item, its status later changes to [AVPlayerItemStatusReadyToPlay](status-swift.enum/readytoplay.md). If the URL contains no valid data or otherwise can’t be used by the player item, its status later changes to [AVPlayerItemStatusFailed](status-swift.enum/failed.md). You can determine the nature of the failure by querying the player item’s [error](error.md) property.

## See Also

### Creating a player item

- [- initWithURL:](<init(url_)-1xrtk.md>) — Creates a player item with a specified URL.
- [playerItemWithAsset:](playeritemwithasset_.md) — Returns a new player item for a specified asset.
- [- initWithAsset:](<init(asset_)-87rjl.md>) — Creates a player item for a specified asset.
- [playerItemWithAsset:automaticallyLoadedAssetKeys:](playeritemwithasset_automaticallyloadedassetkeys_.md) — Creates a player item with the specified asset and the asset keys to automatically load.
- [- initWithAsset:automaticallyLoadedAssetKeys:](<init(asset_automaticallyloadedassetkeys_)-8x4.md>) — Creates a player item with the specified asset and the asset keys to automatically load.
