---
title: isCompatibleWithAirPlayVideo
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/iscompatiblewithairplayvideo
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/iscompatiblewithairplayvideo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/iscompatiblewithairplayvideo.json'
content_hash: 'sha256:bbe1a28d9b612348'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# isCompatibleWithAirPlayVideo

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset is compatible with AirPlay Video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isCompatibleWithAirPlayVideo: Bool { get }
```

## Discussion

This property value is [true](../../swift/true.md) if you can play this composition’s content to an external AirPlay device, like an Apple TV.

## See Also

### Determining suitability

- [isPlayable](isplayable.md) — A Boolean value that indicates whether the asset has playable content.
- [isReadable](isreadable.md) — A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [isExportable](isexportable.md) — A Boolean value that indicates whether you can export this asset using an export session.
- [isComposable](iscomposable.md) — A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [isCompatibleWithSavedPhotosAlbum](iscompatiblewithsavedphotosalbum.md) — A Boolean value that indicates whether you can write the composition to the Saved Photos album.
