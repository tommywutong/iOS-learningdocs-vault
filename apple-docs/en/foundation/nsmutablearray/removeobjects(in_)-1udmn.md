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
doc_path: '/documentation/foundation/nsmutablearray/removeobjects(in:)-1udmn'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/removeobjects(in:)-1udmn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/removeobjects%28in%3A%29-1udmn.json'
content_hash: 'sha256:dd7a175ad36389b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# removeObjects(in:)

<sub>Instance Method</sub>

Removes from the array each of the objects within a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObjects(in range: NSRange)
```

## Parameters

- `range` — The range of the objects to be removed from the array.

## Discussion

The objects are removed using [- removeObjectAtIndex:](<removeobject(at_).md>).

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
- [- removeObjectsInArray:](<removeobjects(in_)-4yb26.md>) — Removes from the receiving array the objects in another given array.
