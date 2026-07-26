---
title: PHCollectionListType
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollectionlisttype
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlisttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlisttype.json'
content_hash: 'sha256:e2b9b18dedc3fd10'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHCollectionListType

<sub>Enumeration</sub>

Major distinctions between kinds of collection list, used by the [collectionListType](phcollectionlist/collectionlisttype.md) property and [+ fetchCollectionListsWithType:subtype:options:](<phcollectionlist/fetchcollectionlists(with_subtype_options_).md>) method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHCollectionListType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHCollectionListTypeMomentList](phcollectionlisttype/momentlist.md) — A group of asset collections of type [PHAssetCollectionTypeMoment](phassetcollectiontype/moment.md). _(deprecated)_
- [PHCollectionListTypeFolder](phcollectionlisttype/folder.md) — A folder containing asset collections of type [PHAssetCollectionTypeAlbum](phassetcollectiontype/album.md) or [PHAssetCollectionTypeSmartAlbum](phassetcollectiontype/smartalbum.md).
- [PHCollectionListTypeSmartFolder](phcollectionlisttype/smartfolder.md) — A smart folder synced to the device from .

### Initializers

- [init(rawValue:)](<phcollectionlisttype/init(rawvalue_).md>)

## See Also

### Reading Collection List Metadata

- [collectionListType](phcollectionlist/collectionlisttype.md) — The type of asset collection group that the collection list represents.
- [collectionListSubtype](phcollectionlist/collectionlistsubtype.md) — The type of asset collection grouping the collection list represents.
- [PHCollectionListSubtype](phcollectionlistsubtype.md) — Major distinctions between kinds of collection list, used by the [collectionListSubtype](phcollectionlist/collectionlistsubtype.md) property and [+ fetchCollectionListsWithType:subtype:options:](<phcollectionlist/fetchcollectionlists(with_subtype_options_).md>), [+ fetchMomentListsWithSubtype:containingMoment:options:](<phcollectionlist/fetchmomentlists(with_containingmoment_options_).md>), and [+ fetchMomentListsWithSubtype:options:](<phcollectionlist/fetchmomentlists(with_options_).md>) methods.
- [startDate](phcollectionlist/startdate.md) — The earliest creation date among all assets in the collection list.
- [endDate](phcollectionlist/enddate.md) — The latest creation date among all assets in the collection list.
- [localizedLocationNames](phcollectionlist/localizedlocationnames.md) — The names of locations grouped by the collection (an array of `NSString` objects).
