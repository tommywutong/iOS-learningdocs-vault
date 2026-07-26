---
title: firstObject
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsarray/firstobject
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/firstobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/firstobject.json'
content_hash: 'sha256:ecbc06132ae6b03d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# firstObject

<sub>Instance Property</sub>

The first object in the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var firstObject: Any? { get }
```

## Discussion

If the array is empty, returns `nil`.

## See Also

### Querying an Array

- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the array.
- [count](count.md) — The number of objects in the array.
- [lastObject](lastobject.md) — The last object in the array.
- [- objectAtIndex:](<object(at_).md>) — Returns the object located at the specified index.
- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the object at the specified index.
- [- objectsAtIndexes:](<objects(at_).md>) — Returns an array containing the objects in the array at the indexes specified by a given index set.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the array.
- [- reverseObjectEnumerator](<reverseobjectenumerator().md>) — Returns an enumerator object that lets you access each object in the array, in reverse order.
