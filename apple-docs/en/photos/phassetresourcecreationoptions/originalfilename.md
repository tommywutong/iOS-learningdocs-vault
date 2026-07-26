---
title: originalFilename
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcecreationoptions/originalfilename
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcecreationoptions/originalfilename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcecreationoptions/originalfilename.json'
content_hash: 'sha256:3eb0d3a9568dcfd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceCreationOptions](../phassetresourcecreationoptions.md)

# originalFilename

<sub>Instance Property</sub>

The filename for the asset resource being created.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var originalFilename: String? { get set }
```

## Discussion

You can use this property to track the original name of the file from which you import an asset resource even if you use the [- addResourceWithType:data:options:](<../phassetcreationrequest/addresource(with_data_options_).md>) method to create a resource from data instead of from a file. After creating the asset, this information is available in the [originalFilename](../phassetresource/originalfilename.md) property of the corresponding [PHAssetResource](../phassetresource.md) object.

If you do not specify a value for this property and are using the [- addResourceWithType:fileURL:options:](<../phassetcreationrequest/addresource(with_fileurl_options_).md>) method to create a resource, Photos infers the filename from that method’s `fileURL` parameter. Otherwise, Photos automatically generates a filename.

## See Also

### Describing a New Asset Resource

- [uniformTypeIdentifier](uniformtypeidentifier.md) — The uniform type identifier for the resource. _(deprecated)_
- [contentType](contenttype.md) — The type of data being provided for this asset resource. If not specified, one will be inferred from the PHAssetResourceType or file URL extension (if provided).
