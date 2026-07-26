---
title: contentType
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresource/contenttype
source_url: 'https://developer.apple.com/documentation/photos/phassetresource/contenttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresource/contenttype.json'
content_hash: 'sha256:353b2d3ae5868dc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResource](../phassetresource.md)

# contentType

<sub>Instance Property</sub>

The content type of the data associated with this asset resource (the data can be retrieved via `PHAssetResourceManager`)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentType: UTType { get }
```

## See Also

### Inspecting an Asset Resource

- [type](type.md) — The relationship of an asset resource to its owning asset.
- [PHAssetResourceType](../phassetresourcetype.md) — Describes the relationship of an asset resource to its owning asset.
- [assetLocalIdentifier](assetlocalidentifier.md) — The unique identifier the system associates for a local asset object.
- [uniformTypeIdentifier](uniformtypeidentifier.md) — The uniform type identifier for the asset resource’s image or video data. _(deprecated)_
- [originalFilename](originalfilename.md) — The original filename of the asset resource from when it was created or imported.
- [pixelHeight](pixelheight.md) — The height of the resource, in pixels.
- [pixelWidth](pixelwidth.md) — The width of the resource, in pixels.
