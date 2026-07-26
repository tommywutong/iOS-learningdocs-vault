---
title: 'countOfAssets(with:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phfetchresult/countofassets(with:)'
source_url: 'https://developer.apple.com/documentation/photos/phfetchresult/countofassets(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresult/countofassets%28with%3A%29.json'
content_hash: 'sha256:52ce6fe814ff7871'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResult](../phfetchresult.md)

# countOfAssets(with:)

<sub>Instance Method</sub>

Returns the number of assets in the fetch result of a specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func countOfAssets(with mediaType: PHAssetMediaType) -> Int
```

## Parameters

- `mediaType` — The type of assets to count, such as image or video. See [PHAssetMediaType](../phassetmediatype.md).

## Return Value

The number of assets in the fetch result of the specified type.

## Discussion

The first time you call this method, Photos enumerates the contents of the fetch result to count those of the specified type, then caches the result. Subsequent calls with the same `mediaType` parameter return the cached value.

This method counts only the [PHAsset](../phasset.md) objects in a fetch result. If a fetch result contains only [PHAssetCollection](../phassetcollection.md) or [PHCollectionList](../phcollectionlist.md) objects, the return value is `0`.

## See Also

### Querying a Fetch Result

- [- containsObject:](<contains(__).md>) — Returns whether the specified object is present in the fetch result.
- [count](count.md) — The number of objects in the fetch result.
- [firstObject](firstobject.md) — The first object in the fetch result.
- [lastObject](lastobject.md) — The last object in the fetch result.
- [- objectAtIndex:](<object(at_).md>) — Returns the object located at the specified index.
- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the object located at the specified index.
- [- objectsAtIndexes:](<objects(at_).md>) — Returns an array containing the objects in the fetch result at the indexes in the specified index set.
