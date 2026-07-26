---
title: 'init(asset:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/init(asset:)-87rjl'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/init(asset:)-87rjl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/init%28asset%3A%29-87rjl.json'
content_hash: 'sha256:ad313bfc48e5df95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# init(asset:)

<sub>Initializer</sub>

Creates a player item for a specified asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(asset: AVAsset)
```

## Parameters

- `asset` — The [AVAsset](../avasset.md) to be played.

## Return Value

A new player item, initialized to play `asset`.

## See Also

### Creating a player item

- [- initWithURL:](<init(url_)-1xrtk.md>) — Creates a player item with a specified URL.
- [init(asset:)](<init(asset_)-1nme9.md>)
- [init(asset:automaticallyLoadedAssetKeys:)](<init(asset_automaticallyloadedassetkeys_)-5czjh.md>) — Creates a player item for the asset, and automatically loads values for the specified properties.
- [init(asset:automaticallyLoadedAssetKeys:)](<init(asset_automaticallyloadedassetkeys_)-85hal.md>)
- [- initWithAsset:automaticallyLoadedAssetKeys:](<init(asset_automaticallyloadedassetkeys_)-8x4.md>) — Creates a player item with the specified asset and the asset keys to automatically load.
