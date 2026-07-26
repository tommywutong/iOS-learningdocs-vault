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
doc_path: /documentation/photos/phassetresourcecreationoptions/contenttype
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcecreationoptions/contenttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcecreationoptions/contenttype.json'
content_hash: 'sha256:aa627d68eb6d8e3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceCreationOptions](../phassetresourcecreationoptions.md)

# contentType

<sub>Instance Property</sub>

The type of data being provided for this asset resource. If not specified, one will be inferred from the PHAssetResourceType or file URL extension (if provided).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentType: UTType? { get set }
```

## See Also

### Describing a New Asset Resource

- [originalFilename](originalfilename.md) — The filename for the asset resource being created.
- [uniformTypeIdentifier](uniformtypeidentifier.md) — The uniform type identifier for the resource. _(deprecated)_
