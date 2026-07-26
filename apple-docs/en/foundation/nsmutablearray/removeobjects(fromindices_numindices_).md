---
title: 'removeObjects(fromIndices:numIndices:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（4.0 起废弃）, iPadOS 2.0+（4.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsmutablearray/removeobjects(fromindices:numindices:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/removeobjects(fromindices:numindices:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/removeobjects%28fromindices%3Anumindices%3A%29.json'
content_hash: 'sha256:018f6aea98e13573'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# removeObjects(fromIndices:numIndices:)

<sub>Instance Method</sub>

Removes the specified number of objects from the array, beginning at the specified index.

> [!warning] Deprecated
> Do not use this method, use [- removeObjectsAtIndexes:](<removeobjects(at_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func removeObjects(fromIndices indices: UnsafeMutablePointer<Int>, numIndices cnt: Int)
```

## Parameters

- `indices` — A C array of the indices of the objects to remove from the receiving array.

- `cnt` — The number of objects to remove from the receiving array.

## Discussion

This method is similar to [- removeObjectAtIndex:](<removeobject(at_).md>), but it allows you to efficiently remove multiple objects with a single operation. If you sort the list of indexes in ascending order, you will improve the speed of this operation.

This method cannot be sent to a remote object with distributed objects.

### Special Considerations

This deprecated method uses a C array of indices. The [- removeObjectsAtIndexes:](<removeobjects(at_).md>) method uses an [NSIndexSet](../nsindexset.md) which provides a more efficient way of indexing into an array.

## See Also

### Related Documentation

- [- initWithCapacity:](<init(capacity_).md>) — Returns an array, initialized with enough memory to initially hold a given number of objects.

### Removing Objects

- [- removeAllObjects](<removeallobjects().md>) — Empties the array of all its elements.
- [- removeLastObject](<removelastobject().md>) — Removes the object with the highest-valued index in the array
- [- removeObject:](<remove(__).md>) — Removes all occurrences in the array of a given object.
- [- removeObject:inRange:](<remove(__in_).md>) — Removes all occurrences within a specified range in the array of a given object.
- [- removeObjectAtIndex:](<removeobject(at_).md>) — Removes the object at `index` .
- [- removeObjectsAtIndexes:](<removeobjects(at_).md>) — Removes the objects at the specified indexes from the array.
- [- removeObjectIdenticalTo:](<removeobject(identicalto_).md>) — Removes all occurrences of a given object in the array.
- [- removeObjectIdenticalTo:inRange:](<removeobject(identicalto_in_).md>) — Removes all occurrences of `anObject` within the specified range in the array.
- [- removeObjectsInArray:](<removeobjects(in_)-4yb26.md>) — Removes from the receiving array the objects in another given array.
- [- removeObjectsInRange:](<removeobjects(in_)-1udmn.md>) — Removes from the array each of the objects within a given range.
