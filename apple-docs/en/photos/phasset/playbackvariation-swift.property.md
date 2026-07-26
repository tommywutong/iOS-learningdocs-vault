---
title: playbackVariation
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phasset/playbackvariation-swift.property
source_url: 'https://developer.apple.com/documentation/photos/phasset/playbackvariation-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/playbackvariation-swift.property.json'
content_hash: 'sha256:de6ebaf4a0abc727'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# playbackVariation

<sub>Instance Property</sub>

The Live Photo playback variation for the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var playbackVariation: PHAsset.PlaybackVariation { get }
```

## Discussion

Use this value to determine whether a Live Photo plays back as a Long Exposure, Mirror (Bounce), or Autoloop (Loop):

- `PHAssetPlaybackVariationNone`: the asset is not a Live Photo, or uses the default Live Photo presentation.
- `PHAssetPlaybackVariationAutoloop`: the Live Photo plays back as a Loop.
- `PHAssetPlaybackVariationMirror`: the Live Photo plays back as a Bounce.
- `PHAssetPlaybackVariationLongExposure`: the Live Photo plays back as a Long Exposure.
