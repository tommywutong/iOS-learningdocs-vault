---
title: 'objects(at:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phfetchresult/objects(at:)'
source_url: 'https://developer.apple.com/documentation/photos/phfetchresult/objects(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresult/objects%28at%3A%29.json'
content_hash: 'sha256:e74c6c0e90d5124e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResult](../phfetchresult.md)

# objects(at:)

<sub>Instance Method</sub>

Returns an array containing the objects in the fetch result at the indexes in the specified index set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func objects(at indexes: IndexSet) -> [ObjectType]
```

## Parameters

- `indexes` — An index set containing indexes within the bounds of the fetch result.

## Return Value

An array containing the objects in the fetch result at the indexes specified by `indexes`.

## Discussion

The ordering of the returned array follows the index set. That is, in the returned array, an object with a higher index in the index set comes after any object with a smaller index in the index set.

Raises a range exception if any index in the index set is beyond the end of the fetch result (that is, greater than or equal to the value of the [count](count.md) property).

## See Also

### Querying a Fetch Result

- [- containsObject:](<contains(__).md>) — Returns whether the specified object is present in the fetch result.
- [count](count.md) — The number of objects in the fetch result.
- [- countOfAssetsWithMediaType:](<countofassets(with_).md>) — Returns the number of assets in the fetch result of a specified type.
- [firstObject](firstobject.md) — The first object in the fetch result.
- [lastObject](lastobject.md) — The last object in the fetch result.
- [- objectAtIndex:](<object(at_).md>) — Returns the object located at the specified index.
- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the object located at the specified index.
