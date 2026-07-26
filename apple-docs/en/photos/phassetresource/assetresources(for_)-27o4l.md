---
title: 'assetResources(for:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetresource/assetresources(for:)-27o4l'
source_url: 'https://developer.apple.com/documentation/photos/phassetresource/assetresources(for:)-27o4l'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresource/assetresources%28for%3A%29-27o4l.json'
content_hash: 'sha256:c54443d88a9abb06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResource](../phassetresource.md)

# assetResources(for:)

<sub>Type Method</sub>

Returns the list of data resources associated with an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func assetResources(for asset: PHAsset) -> [PHAssetResource]
```

## Parameters

- `asset` — A photo or video asset in the Photos library.

## Return Value

The asset’s resources.

## Discussion

Asset resource objects describe the data files that an asset represents. An asset can contain multiple resources—for example, an edited photo asset contains resources for both the original and edited images, as well as for the [PHAdjustmentData](../phadjustmentdata.md) object describing the edit. To work with one of these files, fetch the underlying data using the [PHAssetResourceManager](../phassetresourcemanager.md) class.

## See Also

### Retrieving an Asset’s Data Resources

- [+ assetResourcesForLivePhoto:](<assetresources(for_)-2fedw.md>) — Returns the list of data resources associated with a Live Photo object.
