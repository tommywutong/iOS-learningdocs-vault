---
title: isPlayable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/isplayable-45h5v
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/isplayable-45h5v'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/isplayable-45h5v.json'
content_hash: 'sha256:50be10c3522f7c6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# isPlayable

<sub>Type Property</sub>

A Boolean value that indicates whether an asset contains playable content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var isPlayable: AVAsyncProperty<Root, Bool> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

> [!note] Note
> You can attempt playback when value is [false](../../swift/false.md), but this may result in a substandard playback experience.

## See Also

### Loading suitability

- [isExportable](isexportable.md) — A Boolean value that indicates whether you can export an asset using an export session.
- [isReadable](isreadable.md) — A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [isComposable](iscomposable.md) — A Boolean value that indicates whether you can use the asset in a media composition.
- [isCompatibleWithAirPlayVideo](iscompatiblewithairplayvideo.md) — A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [isCompatibleWithSavedPhotosAlbum](iscompatiblewithsavedphotosalbum.md) — A Boolean value that indicates whether you can write the asset to the Saved Photos album.
