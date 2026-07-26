---
title: localizedLocationNames
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetcollection/localizedlocationnames
source_url: 'https://developer.apple.com/documentation/photos/phassetcollection/localizedlocationnames'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollection/localizedlocationnames.json'
content_hash: 'sha256:45e6329b65b4178c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollection](../phassetcollection.md)

# localizedLocationNames

<sub>Instance Property</sub>

The names of locations grouped by the collection (an array of `NSString` objects).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var localizedLocationNames: [String] { get }
```

## Discussion

This property applies only to asset collections whose type is [PHAssetCollectionTypeMoment](../phassetcollectiontype/moment.md). The Photos app automatically creates moments to group assets by time and location. A moment might group assets captured in multiple locations, so this array can contain multiple names. For other asset collection types, this property’s value is `nil`.

## See Also

### Reading Asset Collection Metadata

- [assetCollectionType](assetcollectiontype.md) — The type of the asset collection, such as an album or a moment.
- [PHAssetCollectionType](../phassetcollectiontype.md) — Major distinctions between kinds of asset collections, used by the [assetCollectionType](assetcollectiontype.md) property and the [+ fetchAssetCollectionsContainingAsset:withType:options:](<fetchassetcollectionscontaining(__with_options_).md>) and [+ fetchAssetCollectionsWithType:subtype:options:](<fetchassetcollections(with_subtype_options_).md>) methods.
- [assetCollectionSubtype](assetcollectionsubtype.md) — The subtype of the asset collection.
- [PHAssetCollectionSubtype](../phassetcollectionsubtype.md) — Minor distinctions between kinds of asset collections, used by the [assetCollectionSubtype](assetcollectionsubtype.md) property and the [+ fetchAssetCollectionsWithType:subtype:options:](<fetchassetcollections(with_subtype_options_).md>) method.
- [estimatedAssetCount](estimatedassetcount.md) — The estimated number of assets in the asset collection.
- [startDate](startdate.md) — The earliest creation date among all assets in the asset collection.
- [endDate](enddate.md) — The latest creation date among all assets in the asset collection.
- [approximateLocation](approximatelocation.md) — A location representing those of all assets in the collection.
