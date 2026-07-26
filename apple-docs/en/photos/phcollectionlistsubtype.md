---
title: PHCollectionListSubtype
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollectionlistsubtype
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistsubtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistsubtype.json'
content_hash: 'sha256:ce6594fce688cd7a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHCollectionListSubtype

<sub>Enumeration</sub>

Major distinctions between kinds of collection list, used by the [collectionListSubtype](phcollectionlist/collectionlistsubtype.md) property and [+ fetchCollectionListsWithType:subtype:options:](<phcollectionlist/fetchcollectionlists(with_subtype_options_).md>), [+ fetchMomentListsWithSubtype:containingMoment:options:](<phcollectionlist/fetchmomentlists(with_containingmoment_options_).md>), and [+ fetchMomentListsWithSubtype:options:](<phcollectionlist/fetchmomentlists(with_options_).md>) methods.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHCollectionListSubtype
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHCollectionListSubtypeMomentListCluster](phcollectionlistsubtype/momentlistcluster.md) — The collection list is a moment cluster, grouping several related moments. _(deprecated)_
- [PHCollectionListSubtypeMomentListYear](phcollectionlistsubtype/momentlistyear.md) — The collection list is a moment year, grouping all moments from one or more calendar years. _(deprecated)_
- [PHCollectionListSubtypeRegularFolder](phcollectionlistsubtype/regularfolder.md) — The collection list is a folder containing albums or other folders.
- [PHCollectionListSubtypeRootFolder](phcollectionlistsubtype/rootfolder.md) — The collection list that contains the top-level user collections, there is always one root folder in the library and does not allow `PHCollectionEditOperationRename` or `PHCollectionEditOperationDelete` _(beta)_
- [PHCollectionListSubtypeSmartFolderEvents](phcollectionlistsubtype/smartfolderevents.md) — The collection list is a smart folder containing one or more Events synced from iPhoto.
- [PHCollectionListSubtypeSmartFolderFaces](phcollectionlistsubtype/smartfolderfaces.md) — The collection list is a smart folder containing one or more Faces synced from iPhoto.
- [PHCollectionListSubtypeAny](phcollectionlistsubtype/any.md) — Use this value to fetch collection lists of all possible subtypes.

### Initializers

- [init(rawValue:)](<phcollectionlistsubtype/init(rawvalue_).md>)

## See Also

### Reading Collection List Metadata

- [collectionListType](phcollectionlist/collectionlisttype.md) — The type of asset collection group that the collection list represents.
- [PHCollectionListType](phcollectionlisttype.md) — Major distinctions between kinds of collection list, used by the [collectionListType](phcollectionlist/collectionlisttype.md) property and [+ fetchCollectionListsWithType:subtype:options:](<phcollectionlist/fetchcollectionlists(with_subtype_options_).md>) method.
- [collectionListSubtype](phcollectionlist/collectionlistsubtype.md) — The type of asset collection grouping the collection list represents.
- [startDate](phcollectionlist/startdate.md) — The earliest creation date among all assets in the collection list.
- [endDate](phcollectionlist/enddate.md) — The latest creation date among all assets in the collection list.
- [localizedLocationNames](phcollectionlist/localizedlocationnames.md) — The names of locations grouped by the collection (an array of `NSString` objects).
