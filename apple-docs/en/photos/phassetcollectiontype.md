---
title: PHAssetCollectionType
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetcollectiontype
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectiontype.json'
content_hash: 'sha256:3cb1414e4ad80dad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetCollectionType

<sub>Enumeration</sub>

Major distinctions between kinds of asset collections, used by the [assetCollectionType](phassetcollection/assetcollectiontype.md) property and the [+ fetchAssetCollectionsContainingAsset:withType:options:](<phassetcollection/fetchassetcollectionscontaining(__with_options_).md>) and [+ fetchAssetCollectionsWithType:subtype:options:](<phassetcollection/fetchassetcollections(with_subtype_options_).md>) methods.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHAssetCollectionType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHAssetCollectionTypeAlbum](phassetcollectiontype/album.md) — An album in the Photos app.
- [PHAssetCollectionTypeSmartAlbum](phassetcollectiontype/smartalbum.md) — A smart album whose contents update dynamically.
- [PHAssetCollectionTypeMoment](phassetcollectiontype/moment.md) — A moment in the Photos app. _(deprecated)_

### Initializers

- [init(rawValue:)](<phassetcollectiontype/init(rawvalue_).md>)

## See Also

### Reading Asset Collection Metadata

- [assetCollectionType](phassetcollection/assetcollectiontype.md) — The type of the asset collection, such as an album or a moment.
- [assetCollectionSubtype](phassetcollection/assetcollectionsubtype.md) — The subtype of the asset collection.
- [PHAssetCollectionSubtype](phassetcollectionsubtype.md) — Minor distinctions between kinds of asset collections, used by the [assetCollectionSubtype](phassetcollection/assetcollectionsubtype.md) property and the [+ fetchAssetCollectionsWithType:subtype:options:](<phassetcollection/fetchassetcollections(with_subtype_options_).md>) method.
- [estimatedAssetCount](phassetcollection/estimatedassetcount.md) — The estimated number of assets in the asset collection.
- [startDate](phassetcollection/startdate.md) — The earliest creation date among all assets in the asset collection.
- [endDate](phassetcollection/enddate.md) — The latest creation date among all assets in the asset collection.
- [approximateLocation](phassetcollection/approximatelocation.md) — A location representing those of all assets in the collection.
- [localizedLocationNames](phassetcollection/localizedlocationnames.md) — The names of locations grouped by the collection (an array of `NSString` objects).
