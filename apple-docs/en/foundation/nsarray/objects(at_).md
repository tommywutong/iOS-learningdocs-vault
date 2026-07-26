---
title: 'objects(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/objects(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/objects(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/objects%28at%3A%29.json'
content_hash: 'sha256:3b2f464554ab05a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# objects(at:)

<sub>Instance Method</sub>

Returns an array containing the objects in the array at the indexes specified by a given index set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objects(at indexes: IndexSet) -> [Any]
```

## Return Value

An array containing the objects in the array at the indexes specified by `indexes`.

## Discussion

The returned objects are in the ascending order of their indexes in `indexes`, so that object in returned array with higher index in indexes will follow the object with smaller index in `indexes`.

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any location in `indexes` exceeds the bounds of the array, `indexes` is `nil`.

## See Also

### Querying an Array

- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the array.
- [count](count.md) — The number of objects in the array.
- [firstObject](firstobject.md) — The first object in the array.
- [lastObject](lastobject.md) — The last object in the array.
- [- objectAtIndex:](<object(at_).md>) — Returns the object located at the specified index.
- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the object at the specified index.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the array.
- [- reverseObjectEnumerator](<reverseobjectenumerator().md>) — Returns an enumerator object that lets you access each object in the array, in reverse order.
