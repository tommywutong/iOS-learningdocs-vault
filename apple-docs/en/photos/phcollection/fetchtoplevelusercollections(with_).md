---
title: 'fetchTopLevelUserCollections(with:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollection/fetchtoplevelusercollections(with:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollection/fetchtoplevelusercollections(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollection/fetchtoplevelusercollections%28with%3A%29.json'
content_hash: 'sha256:2e8af5fefdc7013b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollection](../phcollection.md)

# fetchTopLevelUserCollections(with:)

<sub>Type Method</sub>

Retrieves collections from the root of the photo library’s hierarchy of user-created albums and folders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func fetchTopLevelUserCollections(with options: PHFetchOptions?) -> PHFetchResult<PHCollection>
```

## Parameters

- `options` — Options that specify a filter predicate and sort order for the fetched collections, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHCollection](../phcollection.md) objects, or an empty fetch result if no objects match the request.

## See Also

### Fetching Collections

- [+ fetchCollectionsInCollectionList:options:](<fetchcollections(in_options_).md>) — Retrieves collections from the specified collection list.
