---
title: automaticallyLoadedAssetKeys
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/automaticallyloadedassetkeys
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/automaticallyloadedassetkeys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/automaticallyloadedassetkeys.json'
content_hash: 'sha256:3fdd1010f727f0e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# automaticallyLoadedAssetKeys

<sub>Instance Property</sub>

The array of asset keys to be automatically loaded before the player item is ready to play.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var automaticallyLoadedAssetKeys: [String] { get }
```

## Discussion

The value of each key in `automaticallyLoadedAssetKeys` will automatically be loaded by the [asset](asset.md) prior to the player item reaching a status of [AVPlayerItemStatusReadyToPlay](status-swift.enum/readytoplay.md). When this status is reached, the asset’s [- statusOfValueForKey:error:](<../avasynchronouskeyvalueloading/statusofvalue(forkey_error_).md>) method returns [AVKeyValueStatusLoaded](../avkeyvaluestatus/loaded.md) for the status of all keys in the array. If loading of any of the asset’s key values fails, the player item’s [status](status-swift.property.md) will change to [AVPlayerItemStatusFailed](status-swift.enum/failed.md).

## See Also

### Accessing initialization parameters

- [asset](asset.md) — The asset provided during initialization.
