---
title: isCompatibleWithSavedPhotosAlbum
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/iscompatiblewithsavedphotosalbum
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/iscompatiblewithsavedphotosalbum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/iscompatiblewithsavedphotosalbum.json'
content_hash: 'sha256:5e7a088623a3eb00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# isCompatibleWithSavedPhotosAlbum

<sub>Type Property</sub>

A Boolean value that indicates whether you can write the asset to the Saved Photos album.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var isCompatibleWithSavedPhotosAlbum: AVAsyncProperty<Root, Bool> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

## See Also

### Loading suitability

- [isPlayable](isplayable-45h5v.md) — A Boolean value that indicates whether an asset contains playable content.
- [isExportable](isexportable.md) — A Boolean value that indicates whether you can export an asset using an export session.
- [isReadable](isreadable.md) — A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [isComposable](iscomposable.md) — A Boolean value that indicates whether you can use the asset in a media composition.
- [isCompatibleWithAirPlayVideo](iscompatiblewithairplayvideo.md) — A Boolean value that indicates whether the asset is compatible with AirPlay Video.
