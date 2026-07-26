---
title: mediaType
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginput/mediatype
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginput/mediatype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginput/mediatype.json'
content_hash: 'sha256:b9b0ea2c75c8d8bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInput](../phcontenteditinginput.md)

# mediaType

<sub>Instance Property</sub>

The type of the asset, such as video or audio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mediaType: PHAssetMediaType { get }
```

## Discussion

See [PHAssetMediaType](../phassetmediatype.md) for possible values.

## See Also

### Getting Information About the Asset

- [PHAssetMediaType](../phassetmediatype.md) — Identifies the general type of an asset, such as image or video.
- [mediaSubtypes](mediasubtypes.md) — The subtypes of the asset, identifying special kinds of assets such as a panoramic photo or a high-frame-rate video.
- [PHAssetMediaSubtype](../phassetmediasubtype.md) — Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.
- [creationDate](creationdate.md) — The date and time when the asset was originally created.
- [location](location.md) — The location information that was saved with the asset.
- [uniformTypeIdentifier](uniformtypeidentifier.md) — The uniform type identifier for the asset’s image or video data. _(deprecated)_
