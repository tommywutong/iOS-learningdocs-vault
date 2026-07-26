---
title: uniformTypeIdentifier
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 10.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phassetresource/uniformtypeidentifier
source_url: 'https://developer.apple.com/documentation/photos/phassetresource/uniformtypeidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresource/uniformtypeidentifier.json'
content_hash: 'sha256:f14d9adf044aac99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResource](../phassetresource.md)

# uniformTypeIdentifier

<sub>Instance Property</sub>

The uniform type identifier for the asset resource’s image or video data.

> [!warning] Deprecated
> Use contentType instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var uniformTypeIdentifier: String { get }
```

## Discussion

For more information, see [Uniform Type Identifiers Overview](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319).

## See Also

### Inspecting an Asset Resource

- [type](type.md) — The relationship of an asset resource to its owning asset.
- [PHAssetResourceType](../phassetresourcetype.md) — Describes the relationship of an asset resource to its owning asset.
- [contentType](contenttype.md) — The content type of the data associated with this asset resource (the data can be retrieved via `PHAssetResourceManager`)
- [assetLocalIdentifier](assetlocalidentifier.md) — The unique identifier the system associates for a local asset object.
- [originalFilename](originalfilename.md) — The original filename of the asset resource from when it was created or imported.
- [pixelHeight](pixelheight.md) — The height of the resource, in pixels.
- [pixelWidth](pixelwidth.md) — The width of the resource, in pixels.
