---
title: uniformTypeIdentifier
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）, tvOS 10.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phcontenteditinginput/uniformtypeidentifier
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginput/uniformtypeidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginput/uniformtypeidentifier.json'
content_hash: 'sha256:0df53a8cb555276d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInput](../phcontenteditinginput.md)

# uniformTypeIdentifier

<sub>Instance Property</sub>

The uniform type identifier for the asset’s image or video data.

> [!warning] Deprecated
> Use contentType instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var uniformTypeIdentifier: String? { get }
```

## Discussion

For more information, see [Uniform Type Identifiers Overview](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319).

## See Also

### Getting Information About the Asset

- [mediaType](mediatype.md) — The type of the asset, such as video or audio.
- [PHAssetMediaType](../phassetmediatype.md) — Identifies the general type of an asset, such as image or video.
- [mediaSubtypes](mediasubtypes.md) — The subtypes of the asset, identifying special kinds of assets such as a panoramic photo or a high-frame-rate video.
- [PHAssetMediaSubtype](../phassetmediasubtype.md) — Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.
- [creationDate](creationdate.md) — The date and time when the asset was originally created.
- [location](location.md) — The location information that was saved with the asset.
