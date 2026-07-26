---
title: 'object(at:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phfetchresult/object(at:)'
source_url: 'https://developer.apple.com/documentation/photos/phfetchresult/object(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresult/object%28at%3A%29.json'
content_hash: 'sha256:7e21daf8e78ae3a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResult](../phfetchresult.md)

# object(at:)

<sub>Instance Method</sub>

Returns the object located at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func object(at index: Int) -> ObjectType
```

## Parameters

- `index` — An index within the bounds of the fetch result.

## Return Value

The object located at `index` in the fetch result.

## Discussion

Raises a range exception if `index` is beyond the end of the fetch result (that is, greater than or equal to the value of the [count](count.md) property).

## See Also

### Querying a Fetch Result

- [- containsObject:](<contains(__).md>) — Returns whether the specified object is present in the fetch result.
- [count](count.md) — The number of objects in the fetch result.
- [- countOfAssetsWithMediaType:](<countofassets(with_).md>) — Returns the number of assets in the fetch result of a specified type.
- [firstObject](firstobject.md) — The first object in the fetch result.
- [lastObject](lastobject.md) — The last object in the fetch result.
- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the object located at the specified index.
- [- objectsAtIndexes:](<objects(at_).md>) — Returns an array containing the objects in the fetch result at the indexes in the specified index set.
