---
title: isExportable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/isexportable
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/isexportable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/isexportable.json'
content_hash: 'sha256:236327a62e27010a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# isExportable

<sub>Instance Property</sub>

A Boolean value that indicates whether you can export this asset using an export session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var isExportable: Bool { get }
```

## Discussion

This property value is [true](../../swift/true.md) if you can export the composition using [AVAssetExportSession](../avassetexportsession.md).

## See Also

### Determining suitability

- [isPlayable](isplayable.md) — A Boolean value that indicates whether the asset has playable content.
- [isReadable](isreadable.md) — A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [isComposable](iscomposable.md) — A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [isCompatibleWithAirPlayVideo](iscompatiblewithairplayvideo.md) — A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [isCompatibleWithSavedPhotosAlbum](iscompatiblewithsavedphotosalbum.md) — A Boolean value that indicates whether you can write the composition to the Saved Photos album.
