---
title: isComposable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/iscomposable
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/iscomposable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/iscomposable.json'
content_hash: 'sha256:4fce8f21cba39216'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# isComposable

<sub>Instance Property</sub>

A Boolean value that indicates whether you can use the asset as a segment of a composition track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isComposable: Bool { get }
```

## Discussion

This property value is [true](../../swift/true.md) if you can use the composition as a segment within an [AVCompositionTrack](../avcompositiontrack.md) object.

## See Also

### Determining suitability

- [isPlayable](isplayable.md) — A Boolean value that indicates whether the asset has playable content.
- [isReadable](isreadable.md) — A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [isExportable](isexportable.md) — A Boolean value that indicates whether you can export this asset using an export session.
- [isCompatibleWithAirPlayVideo](iscompatiblewithairplayvideo.md) — A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [isCompatibleWithSavedPhotosAlbum](iscompatiblewithsavedphotosalbum.md) — A Boolean value that indicates whether you can write the composition to the Saved Photos album.
