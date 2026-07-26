---
title: 'addResource(with:data:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcreationrequest/addresource(with:data:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcreationrequest/addresource(with:data:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcreationrequest/addresource%28with%3Adata%3Aoptions%3A%29.json'
content_hash: 'sha256:21f89f76de8bd663'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCreationRequest](../phassetcreationrequest.md)

# addResource(with:data:options:)

<sub>Instance Method</sub>

Adds a data resource to the asset being created, using the specified data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addResource(with type: PHAssetResourceType, data: Data, options: PHAssetResourceCreationOptions?)
```

## Parameters

- `type` — The role of this data resource in constructing an asset. For details, see [PHAssetResourceType](../phassetresourcetype.md).

- `data` — The data for the asset resource.

- `options` — Options affecting how Photos constructs the asset resource and incorporates its data into the Photos library. For details, see [PHAssetResourceCreationOptions](../phassetresourcecreationoptions.md).

## Discussion

Photos imports the asset resource data only when it executes the [PHPhotoLibrary](../phphotolibrary.md) change block in which you create a [PHAssetCreationRequest](../phassetcreationrequest.md) object and call this method. If you attempt to create an asset with invalid data or an invalid combination of resources, Photos reports an error in the completion handler of your [PHPhotoLibrary](../phphotolibrary.md) call.

## See Also

### Providing Data Resources for the New Asset

- [- addResourceWithType:fileURL:options:](<addresource(with_fileurl_options_).md>) — Adds a data resource to the asset being created, using the file at the specified URL.
