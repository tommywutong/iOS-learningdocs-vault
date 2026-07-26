---
title: 'contains(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/contains(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/contains%28_%3A%29.json'
content_hash: 'sha256:6495ee21a7dbff2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a given object is present in the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ anObject: Any) -> Bool
```

## Parameters

- `anObject` — An object to look for in the array.

## Return Value

[true](../../swift/true.md) if `anObject` is present in the array, otherwise [false](../../swift/false.md).

## Discussion

Starting at index `0`, each element of the array is checked for equality with `anObject` until a match is found or the end of the array is reached.  Objects are considered equal if [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) returns [true](../../swift/true.md).

To determine if the array contains a particular instance of an object, you can test for identity rather than equality by calling the [- indexOfObjectIdenticalTo:](<indexofobjectidentical(to_).md>) method and comparing the return value to [NSNotFound](../nsnotfound-9t5v2.md).

## See Also

### Related Documentation

- [- indexOfObjectIdenticalTo:](<indexofobjectidentical(to_).md>) — Returns the lowest index whose corresponding array value is identical to a given object.
- [- indexOfObject:](<index(of_).md>) — Returns the lowest index whose corresponding array value is equal to a given object.

### Querying an Array

- [count](count.md) — The number of objects in the array.
- [firstObject](firstobject.md) — The first object in the array.
- [lastObject](lastobject.md) — The last object in the array.
- [- objectAtIndex:](<object(at_).md>) — Returns the object located at the specified index.
- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the object at the specified index.
- [- objectsAtIndexes:](<objects(at_).md>) — Returns an array containing the objects in the array at the indexes specified by a given index set.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the array.
- [- reverseObjectEnumerator](<reverseobjectenumerator().md>) — Returns an enumerator object that lets you access each object in the array, in reverse order.
