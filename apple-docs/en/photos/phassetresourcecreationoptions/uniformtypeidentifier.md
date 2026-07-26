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
doc_path: /documentation/photos/phassetresourcecreationoptions/uniformtypeidentifier
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcecreationoptions/uniformtypeidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcecreationoptions/uniformtypeidentifier.json'
content_hash: 'sha256:b941ce3a904ace4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceCreationOptions](../phassetresourcecreationoptions.md)

# uniformTypeIdentifier

<sub>Instance Property</sub>

The uniform type identifier for the resource.

> [!warning] Deprecated
> Use contentType instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var uniformTypeIdentifier: String? { get set }
```

## Discussion

If you do not specify a value for this property, Photos infers the data type from the [PHAssetResourceType](../phassetresourcetype.md) value you specify when adding the resource to a creation request.

For details in uniform type identifiers, see [Uniform Type Identifiers Overview](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319).

## See Also

### Describing a New Asset Resource

- [originalFilename](originalfilename.md) — The filename for the asset resource being created.
- [contentType](contenttype.md) — The type of data being provided for this asset resource. If not specified, one will be inferred from the PHAssetResourceType or file URL extension (if provided).
