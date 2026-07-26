---
title: estimatedAssetCount
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetcollection/estimatedassetcount
source_url: 'https://developer.apple.com/documentation/photos/phassetcollection/estimatedassetcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollection/estimatedassetcount.json'
content_hash: 'sha256:44061205c5c35228'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollection](../phassetcollection.md)

# estimatedAssetCount

<sub>Instance Property</sub>

The estimated number of assets in the asset collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var estimatedAssetCount: Int { get }
```

## Discussion

This count may not match the current number of assets in the collection. To get the most recent count, fetch the collection’s assets with the [+ fetchAssetsInAssetCollection:options:](<../phasset/fetchassets(in_options_).md>) method and read the [count](../phfetchresult/count.md) property of the fetch result.

If asset count information is not available for the collection, this property’s value is `NSNotFound`.

## See Also

### Reading Asset Collection Metadata

- [assetCollectionType](assetcollectiontype.md) — The type of the asset collection, such as an album or a moment.
- [PHAssetCollectionType](../phassetcollectiontype.md) — Major distinctions between kinds of asset collections, used by the [assetCollectionType](assetcollectiontype.md) property and the [+ fetchAssetCollectionsContainingAsset:withType:options:](<fetchassetcollectionscontaining(__with_options_).md>) and [+ fetchAssetCollectionsWithType:subtype:options:](<fetchassetcollections(with_subtype_options_).md>) methods.
- [assetCollectionSubtype](assetcollectionsubtype.md) — The subtype of the asset collection.
- [PHAssetCollectionSubtype](../phassetcollectionsubtype.md) — Minor distinctions between kinds of asset collections, used by the [assetCollectionSubtype](assetcollectionsubtype.md) property and the [+ fetchAssetCollectionsWithType:subtype:options:](<fetchassetcollections(with_subtype_options_).md>) method.
- [startDate](startdate.md) — The earliest creation date among all assets in the asset collection.
- [endDate](enddate.md) — The latest creation date among all assets in the asset collection.
- [approximateLocation](approximatelocation.md) — A location representing those of all assets in the collection.
- [localizedLocationNames](localizedlocationnames.md) — The names of locations grouped by the collection (an array of `NSString` objects).
