---
title: collectionListType
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollectionlist/collectionlisttype
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlist/collectionlisttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlist/collectionlisttype.json'
content_hash: 'sha256:7d49b46065bdc5ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionList](../phcollectionlist.md)

# collectionListType

<sub>Instance Property</sub>

The type of asset collection group that the collection list represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var collectionListType: PHCollectionListType { get }
```

## Discussion

A collection list may represent an upper level of the Moments hierarchy shown in the Photos app, a folder that contains albums, or a smart folder synced from iPhoto. See [PHCollectionListType](../phcollectionlisttype.md).

## See Also

### Reading Collection List Metadata

- [PHCollectionListType](../phcollectionlisttype.md) — Major distinctions between kinds of collection list, used by the [collectionListType](collectionlisttype.md) property and [+ fetchCollectionListsWithType:subtype:options:](<fetchcollectionlists(with_subtype_options_).md>) method.
- [collectionListSubtype](collectionlistsubtype.md) — The type of asset collection grouping the collection list represents.
- [PHCollectionListSubtype](../phcollectionlistsubtype.md) — Major distinctions between kinds of collection list, used by the [collectionListSubtype](collectionlistsubtype.md) property and [+ fetchCollectionListsWithType:subtype:options:](<fetchcollectionlists(with_subtype_options_).md>), [+ fetchMomentListsWithSubtype:containingMoment:options:](<fetchmomentlists(with_containingmoment_options_).md>), and [+ fetchMomentListsWithSubtype:options:](<fetchmomentlists(with_options_).md>) methods.
- [startDate](startdate.md) — The earliest creation date among all assets in the collection list.
- [endDate](enddate.md) — The latest creation date among all assets in the collection list.
- [localizedLocationNames](localizedlocationnames.md) — The names of locations grouped by the collection (an array of `NSString` objects).
