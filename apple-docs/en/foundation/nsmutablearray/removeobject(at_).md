---
title: 'removeObject(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/removeobject(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/removeobject(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/removeobject%28at%3A%29.json'
content_hash: 'sha256:1b4113fc93bc1dee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# removeObject(at:)

<sub>Instance Method</sub>

Removes the object at `index` .

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObject(at index: Int)
```

## Parameters

- `index` — The index from which to remove the object in the array. The value must not exceed the bounds of the array. > [!important] Important > Raises an exception `NSRangeException` if `index` is beyond the end of the array.

## Discussion

To fill the gap, all elements beyond `index` are moved by subtracting 1 from their index.

## See Also

### Related Documentation

- [- insertObject:atIndex:](<insert(__at_)-5dbx5.md>) — Inserts a given object into the array’s contents at a given index.

### Removing Objects

- [- removeAllObjects](<removeallobjects().md>) — Empties the array of all its elements.
- [- removeLastObject](<removelastobject().md>) — Removes the object with the highest-valued index in the array
- [- removeObject:](<remove(__).md>) — Removes all occurrences in the array of a given object.
- [- removeObject:inRange:](<remove(__in_).md>) — Removes all occurrences within a specified range in the array of a given object.
- [- removeObjectsAtIndexes:](<removeobjects(at_).md>) — Removes the objects at the specified indexes from the array.
- [- removeObjectIdenticalTo:](<removeobject(identicalto_).md>) — Removes all occurrences of a given object in the array.
- [- removeObjectIdenticalTo:inRange:](<removeobject(identicalto_in_).md>) — Removes all occurrences of `anObject` within the specified range in the array.
- [- removeObjectsFromIndices:numIndices:](<removeobjects(fromindices_numindices_).md>) — Removes the specified number of objects from the array, beginning at the specified index. _(deprecated)_
- [- removeObjectsInArray:](<removeobjects(in_)-4yb26.md>) — Removes from the receiving array the objects in another given array.
- [- removeObjectsInRange:](<removeobjects(in_)-1udmn.md>) — Removes from the array each of the objects within a given range.
