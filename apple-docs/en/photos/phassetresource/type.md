---
title: type
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresource/type
source_url: 'https://developer.apple.com/documentation/photos/phassetresource/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresource/type.json'
content_hash: 'sha256:3de03b2e4b3ad9d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResource](../phassetresource.md)

# type

<sub>Instance Property</sub>

The relationship of an asset resource to its owning asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var type: PHAssetResourceType { get }
```

## Discussion

An asset can contain multiple resources, and different resources contribute to the asset in different ways. For details and examples, see [PHAssetResourceType](../phassetresourcetype.md).

## See Also

### Inspecting an Asset Resource

- [PHAssetResourceType](../phassetresourcetype.md) — Describes the relationship of an asset resource to its owning asset.
- [contentType](contenttype.md) — The content type of the data associated with this asset resource (the data can be retrieved via `PHAssetResourceManager`)
- [assetLocalIdentifier](assetlocalidentifier.md) — The unique identifier the system associates for a local asset object.
- [uniformTypeIdentifier](uniformtypeidentifier.md) — The uniform type identifier for the asset resource’s image or video data. _(deprecated)_
- [originalFilename](originalfilename.md) — The original filename of the asset resource from when it was created or imported.
- [pixelHeight](pixelheight.md) — The height of the resource, in pixels.
- [pixelWidth](pixelwidth.md) — The width of the resource, in pixels.
