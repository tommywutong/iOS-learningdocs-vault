---
title: collectionListSubtype
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollectionlist/collectionlistsubtype
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlist/collectionlistsubtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlist/collectionlistsubtype.json'
content_hash: 'sha256:67b5128d29e3b350'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionList](../phcollectionlist.md)

# collectionListSubtype

<sub>Instance Property</sub>

The type of asset collection grouping the collection list represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var collectionListSubtype: PHCollectionListSubtype { get }
```

## Discussion

Use subtypes to make minor distinctions between collection lists of the same type, such as moment clusters and moment years. See [PHCollectionListSubtype](../phcollectionlistsubtype.md).

## See Also

### Reading Collection List Metadata

- [collectionListType](collectionlisttype.md) — The type of asset collection group that the collection list represents.
- [PHCollectionListType](../phcollectionlisttype.md) — Major distinctions between kinds of collection list, used by the [collectionListType](collectionlisttype.md) property and [+ fetchCollectionListsWithType:subtype:options:](<fetchcollectionlists(with_subtype_options_).md>) method.
- [PHCollectionListSubtype](../phcollectionlistsubtype.md) — Major distinctions between kinds of collection list, used by the [collectionListSubtype](collectionlistsubtype.md) property and [+ fetchCollectionListsWithType:subtype:options:](<fetchcollectionlists(with_subtype_options_).md>), [+ fetchMomentListsWithSubtype:containingMoment:options:](<fetchmomentlists(with_containingmoment_options_).md>), and [+ fetchMomentListsWithSubtype:options:](<fetchmomentlists(with_options_).md>) methods.
- [startDate](startdate.md) — The earliest creation date among all assets in the collection list.
- [endDate](enddate.md) — The latest creation date among all assets in the collection list.
- [localizedLocationNames](localizedlocationnames.md) — The names of locations grouped by the collection (an array of `NSString` objects).
