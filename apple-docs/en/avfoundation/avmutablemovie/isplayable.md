---
title: isPlayable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, visionOS 1.0+, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/isplayable
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/isplayable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/isplayable.json'
content_hash: 'sha256:934bc82fcba0bb67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# isPlayable

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset has playable content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var isPlayable: Bool { get }
```

## Discussion

This property value is [true](../../swift/true.md) if you can use the movie to create an [AVPlayerItem](../avplayeritem.md).

## See Also

### Determining suitability

- [isReadable](isreadable.md) — A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [isExportable](isexportable.md) — A Boolean value that indicates whether you can export this asset using an export session.
- [isComposable](iscomposable.md) — A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [isCompatibleWithAirPlayVideo](iscompatiblewithairplayvideo.md) — A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [isCompatibleWithSavedPhotosAlbum](iscompatiblewithsavedphotosalbum.md) — A Boolean value that indicates whether you can write the composition to the Saved Photos album.
