---
title: 'transientCollectionList(with:title:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlist/transientcollectionlist(with:title:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlist/transientcollectionlist(with:title:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlist/transientcollectionlist%28with%3Atitle%3A%29.json'
content_hash: 'sha256:309fd89982135ea5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionList](../phcollectionlist.md)

# transientCollectionList(with:title:)

<sub>Type Method</sub>

Creates a temporary collection list that contains the specified asset collections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func transientCollectionList(with collections: [PHCollection], title: String?) -> PHCollectionList
```

## Parameters

- `collections` — An array of [PHAssetCollection](../phassetcollection.md) objects.

- `title` — A name for the new temporary collection list.

## Return Value

A new collection list.

## Discussion

Transient collection lists are not saved to local storage or iCloud and do not appear in the Photos application or other apps using the Photos framework. A transient collection can be useful if you’ve designed a UI for displaying the contents of a collection list and want to display an arbitrary set of collections.

## See Also

### Creating Temporary Collection Lists

- [+ transientCollectionListWithCollectionsFetchResult:title:](<transientcollectionlist(withcollectionsfetchresult_title_).md>) — Creates a temporary collection list containing the asset collections in the specified fetch result.
