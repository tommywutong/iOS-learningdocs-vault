---
title: assetLocalIdentifier
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresource/assetlocalidentifier
source_url: 'https://developer.apple.com/documentation/photos/phassetresource/assetlocalidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresource/assetlocalidentifier.json'
content_hash: 'sha256:475e6061e289c979'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResource](../phassetresource.md)

# assetLocalIdentifier

<sub>Instance Property</sub>

The unique identifier the system associates for a local asset object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var assetLocalIdentifier: String { get }
```

## Discussion

This property’s value corresponds to the [localIdentifier](../phobject/localidentifier.md) property of the [PHAsset](../phasset.md) object that owns this asset resource. If you’ve obtained an asset resource without a reference to its owning asset, use the [+ fetchAssetsWithLocalIdentifiers:options:](<../phasset/fetchassets(withlocalidentifiers_options_).md>) method with this identifier to retrieve the correct [PHAsset](../phasset.md) object.

## See Also

### Inspecting an Asset Resource

- [type](type.md) — The relationship of an asset resource to its owning asset.
- [PHAssetResourceType](../phassetresourcetype.md) — Describes the relationship of an asset resource to its owning asset.
- [contentType](contenttype.md) — The content type of the data associated with this asset resource (the data can be retrieved via `PHAssetResourceManager`)
- [uniformTypeIdentifier](uniformtypeidentifier.md) — The uniform type identifier for the asset resource’s image or video data. _(deprecated)_
- [originalFilename](originalfilename.md) — The original filename of the asset resource from when it was created or imported.
- [pixelHeight](pixelheight.md) — The height of the resource, in pixels.
- [pixelWidth](pixelwidth.md) — The width of the resource, in pixels.
