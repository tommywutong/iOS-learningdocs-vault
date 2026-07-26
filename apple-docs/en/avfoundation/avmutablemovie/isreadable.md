---
title: isReadable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/isreadable
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/isreadable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/isreadable.json'
content_hash: 'sha256:3d623050311031e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# isReadable

<sub>Instance Property</sub>

A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var isReadable: Bool { get }
```

## Discussion

This property value is [true](../../swift/true.md) if you can use [AVAssetReader](../avassetreader.md) to extract the composition’s media data.

## See Also

### Determining suitability

- [isPlayable](isplayable.md) — A Boolean value that indicates whether the asset has playable content.
- [isExportable](isexportable.md) — A Boolean value that indicates whether you can export this asset using an export session.
- [isComposable](iscomposable.md) — A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [isCompatibleWithAirPlayVideo](iscompatiblewithairplayvideo.md) — A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [isCompatibleWithSavedPhotosAlbum](iscompatiblewithsavedphotosalbum.md) — A Boolean value that indicates whether you can write the composition to the Saved Photos album.
