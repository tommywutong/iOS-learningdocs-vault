---
title: playbackStyle
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phasset/playbackstyle-swift.property
source_url: 'https://developer.apple.com/documentation/photos/phasset/playbackstyle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/playbackstyle-swift.property.json'
content_hash: 'sha256:a3e224be9a648c58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# playbackStyle

<sub>Instance Property</sub>

An enumerated value that describes how to present an asset to the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var playbackStyle: PHAsset.PlaybackStyle { get }
```

## Discussion

Use this value to choose how your app displays the asset in [PHImageManager](../phimagemanager.md) regardless of the media type backing the asset.

## See Also

### Displaying an Asset

- [PlaybackStyle](playbackstyle-swift.enum.md) — An enumeration of asset playback styles that dictate how to present an asset to the user.
