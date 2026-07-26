---
title: 'contains(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phfetchresult/contains(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phfetchresult/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresult/contains%28_%3A%29.json'
content_hash: 'sha256:2c89a2d04095c27e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResult](../phfetchresult.md)

# contains(_:)

<sub>Instance Method</sub>

Returns whether the specified object is present in the fetch result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func contains(_ anObject: ObjectType) -> Bool
```

## Parameters

- `anObject` — An object.

## Return Value

`true` if `anObject` is present in the fetch result, otherwise `false`.

## Discussion

This method determines whether `anObject` is present in the fetch result by sending an `==` message to each of the fetch result’s objects (and passing `anObject` as the parameter to each `==` message).

## See Also

### Querying a Fetch Result

- [count](count.md) — The number of objects in the fetch result.
- [- countOfAssetsWithMediaType:](<countofassets(with_).md>) — Returns the number of assets in the fetch result of a specified type.
- [firstObject](firstobject.md) — The first object in the fetch result.
- [lastObject](lastobject.md) — The last object in the fetch result.
- [- objectAtIndex:](<object(at_).md>) — Returns the object located at the specified index.
- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the object located at the specified index.
- [- objectsAtIndexes:](<objects(at_).md>) — Returns an array containing the objects in the fetch result at the indexes in the specified index set.
