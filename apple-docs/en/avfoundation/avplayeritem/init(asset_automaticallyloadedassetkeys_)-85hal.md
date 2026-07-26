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
doc_path: '/documentation/avfoundation/avplayeritem/init(asset:automaticallyloadedassetkeys:)-85hal'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/init(asset:automaticallyloadedassetkeys:)-85hal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/init%28asset%3Aautomaticallyloadedassetkeys%3A%29-85hal.json'
content_hash: 'sha256:1fafdd0f60099387'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# init(asset:automaticallyLoadedAssetKeys:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated convenience init(asset: any AVAsset & Sendable, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>])
```

## See Also

### Creating a player item

- [- initWithURL:](<init(url_)-1xrtk.md>) — Creates a player item with a specified URL.
- [- initWithAsset:](<init(asset_)-87rjl.md>) — Creates a player item for a specified asset.
- [init(asset:)](<init(asset_)-1nme9.md>)
- [init(asset:automaticallyLoadedAssetKeys:)](<init(asset_automaticallyloadedassetkeys_)-5czjh.md>) — Creates a player item for the asset, and automatically loads values for the specified properties.
- [- initWithAsset:automaticallyLoadedAssetKeys:](<init(asset_automaticallyloadedassetkeys_)-8x4.md>) — Creates a player item with the specified asset and the asset keys to automatically load.
