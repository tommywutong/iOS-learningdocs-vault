---
title: 'fetchCollectionLists(with:subtype:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlist/fetchcollectionlists(with:subtype:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlist/fetchcollectionlists(with:subtype:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlist/fetchcollectionlists%28with%3Asubtype%3Aoptions%3A%29.json'
content_hash: 'sha256:d61ce74a4faeda80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionList](../phcollectionlist.md)

# fetchCollectionLists(with:subtype:options:)

<sub>Type Method</sub>

Retrieves collection lists of the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func fetchCollectionLists(with collectionListType: PHCollectionListType, subtype: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>
```

## Parameters

- `collectionListType` — A type of collection list. See [PHCollectionListType](../phcollectionlisttype.md).

- `subtype` — A subtype of collection list. See [PHCollectionListSubtype](../phcollectionlistsubtype.md).

- `options` — Options that specify a filter predicate and sort order for the fetched collection lists, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHCollectionList](../phcollectionlist.md) objects, or an empty fetch result if no objects match the request.

## Discussion

By default, the returned [PHFetchResult](../phfetchresult.md) object contains all collection lists with the specified type and subtype. To retrieve a more specific set of collection lists, provide a [PHFetchOptions](../phfetchoptions.md) object containing a filter predicate.

## See Also

### Fetching Collection Lists

- [+ fetchCollectionListsContainingCollection:options:](<fetchcollectionlistscontaining(__options_).md>) — Retrieves collection lists that contain the specified collection.
- [+ fetchCollectionListsWithLocalIdentifiers:options:](<fetchcollectionlists(withlocalidentifiers_options_).md>) — Retrieves collection lists with the specified local-device-specific unique identifiers.
- [+ fetchMomentListsWithSubtype:containingMoment:options:](<fetchmomentlists(with_containingmoment_options_).md>) — Retrieves collection lists of the specified moment list type containing the specified moment. _(deprecated)_
- [+ fetchMomentListsWithSubtype:options:](<fetchmomentlists(with_options_).md>) — Retrieves collection lists of the specified moment list type. _(deprecated)_
