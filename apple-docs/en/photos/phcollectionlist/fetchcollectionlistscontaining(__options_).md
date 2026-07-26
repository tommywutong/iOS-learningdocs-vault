---
title: 'fetchCollectionListsContaining(_:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlist/fetchcollectionlistscontaining(_:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlist/fetchcollectionlistscontaining(_:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlist/fetchcollectionlistscontaining%28_%3Aoptions%3A%29.json'
content_hash: 'sha256:fe7dce674d1cd804'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionList](../phcollectionlist.md)

# fetchCollectionListsContaining(_:options:)

<sub>Type Method</sub>

Retrieves collection lists that contain the specified collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func fetchCollectionListsContaining(_ collection: PHCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>
```

## Parameters

- `collection` — An asset collection or another collection list.

- `options` — Options that specify a filter predicate and sort order for the fetched collection lists, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHCollectionList](../phcollectionlist.md) objects, or an empty fetch result if no objects match the request.

## Discussion

Different kinds of collections have different containment possibilities. For example, an asset collection whose type is [PHAssetCollectionTypeAlbum](../phassetcollectiontype/album.md) may be contained in a folder, or have no containing collection list. A folder, in turn, may be contained in another folder. An asset collection whose type is [PHAssetCollectionTypeMoment](../phassetcollectiontype/moment.md) is always contained by two collection lists: a moment cluster and a moment year.

## See Also

### Fetching Collection Lists

- [+ fetchCollectionListsWithLocalIdentifiers:options:](<fetchcollectionlists(withlocalidentifiers_options_).md>) — Retrieves collection lists with the specified local-device-specific unique identifiers.
- [+ fetchCollectionListsWithType:subtype:options:](<fetchcollectionlists(with_subtype_options_).md>) — Retrieves collection lists of the specified type.
- [+ fetchMomentListsWithSubtype:containingMoment:options:](<fetchmomentlists(with_containingmoment_options_).md>) — Retrieves collection lists of the specified moment list type containing the specified moment. _(deprecated)_
- [+ fetchMomentListsWithSubtype:options:](<fetchmomentlists(with_options_).md>) — Retrieves collection lists of the specified moment list type. _(deprecated)_
