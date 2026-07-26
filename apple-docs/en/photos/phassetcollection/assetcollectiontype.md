---
title: assetCollectionType
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetcollection/assetcollectiontype
source_url: 'https://developer.apple.com/documentation/photos/phassetcollection/assetcollectiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollection/assetcollectiontype.json'
content_hash: 'sha256:0e63251ce08b2079'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollection](../phassetcollection.md)

# assetCollectionType

<sub>Instance Property</sub>

The type of the asset collection, such as an album or a moment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var assetCollectionType: PHAssetCollectionType { get }
```

## Discussion

See [PHAssetCollectionType](../phassetcollectiontype.md) for possible values.

## See Also

### Reading Asset Collection Metadata

- [PHAssetCollectionType](../phassetcollectiontype.md) — Major distinctions between kinds of asset collections, used by the [assetCollectionType](assetcollectiontype.md) property and the [+ fetchAssetCollectionsContainingAsset:withType:options:](<fetchassetcollectionscontaining(__with_options_).md>) and [+ fetchAssetCollectionsWithType:subtype:options:](<fetchassetcollections(with_subtype_options_).md>) methods.
- [assetCollectionSubtype](assetcollectionsubtype.md) — The subtype of the asset collection.
- [PHAssetCollectionSubtype](../phassetcollectionsubtype.md) — Minor distinctions between kinds of asset collections, used by the [assetCollectionSubtype](assetcollectionsubtype.md) property and the [+ fetchAssetCollectionsWithType:subtype:options:](<fetchassetcollections(with_subtype_options_).md>) method.
- [estimatedAssetCount](estimatedassetcount.md) — The estimated number of assets in the asset collection.
- [startDate](startdate.md) — The earliest creation date among all assets in the asset collection.
- [endDate](enddate.md) — The latest creation date among all assets in the asset collection.
- [approximateLocation](approximatelocation.md) — A location representing those of all assets in the collection.
- [localizedLocationNames](localizedlocationnames.md) — The names of locations grouped by the collection (an array of `NSString` objects).
