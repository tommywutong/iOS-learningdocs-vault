---
title: 'removeObjects(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/removeobjects(in:)-4yb26'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/removeobjects(in:)-4yb26'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/removeobjects%28in%3A%29-4yb26.json'
content_hash: 'sha256:51e73b08a0142ea8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# removeObjects(in:)

<sub>Instance Method</sub>

Removes from the receiving array the objects in another given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObjects(in otherArray: [Any])
```

## Parameters

- `otherArray` — An array containing the objects to be removed from the receiving array.

## Discussion

This method is similar to [- removeObject:](<remove(__).md>), but it allows you to efficiently remove large sets of objects with a single operation. If the receiving array does not contain objects in `otherArray`, the method has no effect (although it does incur the overhead of searching the contents).

This method assumes that all elements in `otherArray` respond to `hash` and `isEqual:`.

## See Also

### Removing Objects

- [- removeAllObjects](<removeallobjects().md>) — Empties the array of all its elements.
- [- removeLastObject](<removelastobject().md>) — Removes the object with the highest-valued index in the array
- [- removeObject:](<remove(__).md>) — Removes all occurrences in the array of a given object.
- [- removeObject:inRange:](<remove(__in_).md>) — Removes all occurrences within a specified range in the array of a given object.
- [- removeObjectAtIndex:](<removeobject(at_).md>) — Removes the object at `index` .
- [- removeObjectsAtIndexes:](<removeobjects(at_).md>) — Removes the objects at the specified indexes from the array.
- [- removeObjectIdenticalTo:](<removeobject(identicalto_).md>) — Removes all occurrences of a given object in the array.
- [- removeObjectIdenticalTo:inRange:](<removeobject(identicalto_in_).md>) — Removes all occurrences of `anObject` within the specified range in the array.
- [- removeObjectsFromIndices:numIndices:](<removeobjects(fromindices_numindices_).md>) — Removes the specified number of objects from the array, beginning at the specified index. _(deprecated)_
- [- removeObjectsInRange:](<removeobjects(in_)-1udmn.md>) — Removes from the array each of the objects within a given range.
