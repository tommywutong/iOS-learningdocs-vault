---
title: 'remove(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableorderedset/remove(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableorderedset/remove(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableorderedset/remove%28_%3A%29.json'
content_hash: 'sha256:1fcb85b5cb934ee8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableOrderedSet](../nsmutableorderedset.md)

# remove(_:)

<sub>Instance Method</sub>

Removes a given object from the mutable ordered set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remove(_ object: Any)
```

## Parameters

- `object` — The object to remove from the mutable ordered set.

## See Also

### Adding, Removing, and Reordering Entries

- [- addObject:](<add(__).md>) — Appends a given object to the end of the mutable ordered set, if it is not already a member.
- [- addObjects:count:](<add(__count_).md>) — Appends the given number of objects from a given C array to the end of the mutable ordered set.
- [- addObjectsFromArray:](<addobjects(from_).md>) — Appends to the end of the mutable ordered set each object contained in a given array that is not already a member.
- [- insertObject:atIndex:](<insert(__at_)-7qg51.md>) — Inserts the given object at the specified index of the mutable ordered set, if it is not already a member.
- [- insertObjects:atIndexes:](<insert(__at_)-3ncnm.md>) — Inserts the objects in the array at the specified indexes.
- [- removeObjectAtIndex:](<removeobject(at_).md>) — Removes a the object at the specified index from the mutable ordered set.
- [- removeObjectsAtIndexes:](<removeobjects(at_).md>) — Removes the objects at the specified indexes from the mutable ordered set.
- [- removeObjectsInArray:](<removeobjects(in_)-8h2kh.md>) — Removes the objects in the array from the mutable ordered set.
- [- removeObjectsInRange:](<removeobjects(in_)-9jkis.md>) — Removes from the mutable ordered set each of the objects within a given range.
- [- removeAllObjects](<removeallobjects().md>) — Removes all the objects from the mutable ordered set.
- [- replaceObjectAtIndex:withObject:](<replaceobject(at_with_).md>) — Replaces the object at the specified index with the new object.
- [- replaceObjectsAtIndexes:withObjects:](<replaceobjects(at_with_).md>) — Replaces the objects at the specified indexes with the new objects.
- [- replaceObjectsInRange:withObjects:count:](<replaceobjects(in_with_count_).md>) — Replaces the objects in the receiving mutable ordered set at the range with the specified number of objects from a given C array.
- [- setObject:atIndex:](<setobject(__at_).md>) — Appends or replaces the object at the specified index.
- [- moveObjectsAtIndexes:toIndex:](<moveobjects(at_to_).md>) — Moves the objects at the specified indexes to the new location.
