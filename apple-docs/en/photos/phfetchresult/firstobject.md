---
title: firstObject
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phfetchresult/firstobject
source_url: 'https://developer.apple.com/documentation/photos/phfetchresult/firstobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresult/firstobject.json'
content_hash: 'sha256:8074ca43966b64f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResult](../phfetchresult.md)

# firstObject

<sub>Instance Property</sub>

The first object in the fetch result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var firstObject: ObjectType? { get }
```

## Discussion

You specify the ordering of a fetch result in the [PHFetchOptions](../phfetchoptions.md) object you pass to a fetch method.

Returns `nil` if the fetch result is empty.

## See Also

### Querying a Fetch Result

- [- containsObject:](<contains(__).md>) — Returns whether the specified object is present in the fetch result.
- [count](count.md) — The number of objects in the fetch result.
- [- countOfAssetsWithMediaType:](<countofassets(with_).md>) — Returns the number of assets in the fetch result of a specified type.
- [lastObject](lastobject.md) — The last object in the fetch result.
- [- objectAtIndex:](<object(at_).md>) — Returns the object located at the specified index.
- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the object located at the specified index.
- [- objectsAtIndexes:](<objects(at_).md>) — Returns an array containing the objects in the fetch result at the indexes in the specified index set.
