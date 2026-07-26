---
title: reverseObjectEnumerator()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsarray/reverseobjectenumerator()
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/reverseobjectenumerator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/reverseobjectenumerator%28%29.json'
content_hash: 'sha256:8d880d37663579f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# reverseObjectEnumerator()

<sub>Instance Method</sub>

Returns an enumerator object that lets you access each object in the array, in reverse order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func reverseObjectEnumerator() -> NSEnumerator
```

## Return Value

An enumerator object that lets you access each object in the array, in order, from the element at the highest index down to the element at index `0`.

## Discussion

When you use this method with mutable subclasses of `NSArray`, you must not modify the array during enumeration.

It is more efficient to use the fast enumeration protocol (see [NSFastEnumeration](../nsfastenumeration.md)). Fast enumeration is available in macOS 10.5 and later and iOS 2.0 and later.

## See Also

### Related Documentation

- [- nextObject](<../nsenumerator/nextobject().md>) — Returns the next object from the collection being enumerated.

### Querying an Array

- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the array.
- [count](count.md) — The number of objects in the array.
- [firstObject](firstobject.md) — The first object in the array.
- [lastObject](lastobject.md) — The last object in the array.
- [- objectAtIndex:](<object(at_).md>) — Returns the object located at the specified index.
- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the object at the specified index.
- [- objectsAtIndexes:](<objects(at_).md>) — Returns an array containing the objects in the array at the indexes specified by a given index set.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the array.
