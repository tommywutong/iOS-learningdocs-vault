---
title: 'fetchCollections(in:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollection/fetchcollections(in:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollection/fetchcollections(in:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollection/fetchcollections%28in%3Aoptions%3A%29.json'
content_hash: 'sha256:fd26d521a06756c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollection](../phcollection.md)

# fetchCollections(in:options:)

<sub>Type Method</sub>

Retrieves collections from the specified collection list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func fetchCollections(in collectionList: PHCollectionList, options: PHFetchOptions?) -> PHFetchResult<PHCollection>
```

## Parameters

- `collectionList` — The collection list from which to fetch collections.

- `options` — Options that specify a filter predicate and sort order for the fetched collections, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHCollection](../phcollection.md) objects, or an empty fetch result if no objects match the request.

## Discussion

By default, the returned [PHFetchResult](../phfetchresult.md) object contains all collections in the specified collection list. To retrieve a more specific set of assets, provide a [PHFetchOptions](../phfetchoptions.md) object that contains a filter predicate.

## See Also

### Fetching Collections

- [+ fetchTopLevelUserCollectionsWithOptions:](<fetchtoplevelusercollections(with_).md>) — Retrieves collections from the root of the photo library’s hierarchy of user-created albums and folders.
