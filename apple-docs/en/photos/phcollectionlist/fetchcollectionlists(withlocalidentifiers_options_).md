---
title: 'fetchCollectionLists(withLocalIdentifiers:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlist/fetchcollectionlists(withlocalidentifiers:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlist/fetchcollectionlists(withlocalidentifiers:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlist/fetchcollectionlists%28withlocalidentifiers%3Aoptions%3A%29.json'
content_hash: 'sha256:beb0e8e3f07c74ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionList](../phcollectionlist.md)

# fetchCollectionLists(withLocalIdentifiers:options:)

<sub>Type Method</sub>

Retrieves collection lists with the specified local-device-specific unique identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func fetchCollectionLists(withLocalIdentifiers identifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>
```

## Parameters

- `identifiers` — An array of `NSString` objects, each the [localIdentifier](../phobject/localidentifier.md) string of a collection list.

- `options` — Options that specify a filter predicate and sort order for the fetched collection lists, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHCollectionList](../phcollectionlist.md) objects, or an empty fetch result if no objects match the request.

## See Also

### Fetching Collection Lists

- [+ fetchCollectionListsContainingCollection:options:](<fetchcollectionlistscontaining(__options_).md>) — Retrieves collection lists that contain the specified collection.
- [+ fetchCollectionListsWithType:subtype:options:](<fetchcollectionlists(with_subtype_options_).md>) — Retrieves collection lists of the specified type.
- [+ fetchMomentListsWithSubtype:containingMoment:options:](<fetchmomentlists(with_containingmoment_options_).md>) — Retrieves collection lists of the specified moment list type containing the specified moment. _(deprecated)_
- [+ fetchMomentListsWithSubtype:options:](<fetchmomentlists(with_options_).md>) — Retrieves collection lists of the specified moment list type. _(deprecated)_
