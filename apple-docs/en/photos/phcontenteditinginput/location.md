---
title: location
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginput/location
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginput/location'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginput/location.json'
content_hash: 'sha256:dbc032cc4fbfc6d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInput](../phcontenteditinginput.md)

# location

<sub>Instance Property</sub>

The location information that was saved with the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var location: CLLocation? { get }
```

## Discussion

Typically, an asset’s location metadata identifies the place where the asset was captured.

## See Also

### Getting Information About the Asset

- [mediaType](mediatype.md) — The type of the asset, such as video or audio.
- [PHAssetMediaType](../phassetmediatype.md) — Identifies the general type of an asset, such as image or video.
- [mediaSubtypes](mediasubtypes.md) — The subtypes of the asset, identifying special kinds of assets such as a panoramic photo or a high-frame-rate video.
- [PHAssetMediaSubtype](../phassetmediasubtype.md) — Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.
- [creationDate](creationdate.md) — The date and time when the asset was originally created.
- [uniformTypeIdentifier](uniformtypeidentifier.md) — The uniform type identifier for the asset’s image or video data. _(deprecated)_
