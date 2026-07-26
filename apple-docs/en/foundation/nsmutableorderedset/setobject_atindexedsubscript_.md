---
title: 'setObject:atIndexedSubscript:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableorderedset/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableorderedset/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableorderedset/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:2fe3d33d50ad5ebb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableOrderedSet](../nsmutableorderedset.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Replaces the given object at the specified index of the mutable ordered set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) setObject:(ObjectType) obj atIndexedSubscript:(NSUInteger) idx;
```

## Parameters

- `obj` — The object to replace the set’s content.

- `idx` — The index in the mutable ordered set at which to insert `obj`. This value must not be greater than the count of elements in the array. > [!important] Important > Important: Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if `idx` is greater than the number of elements in the mutable ordered set.

## Discussion

If the index is already occupied, the objects at index and beyond are shifted by adding `1` to their indices to make room.

This method is identical to [- insertObject:atIndex:](<insert(__at_)-7qg51.md>).

## See Also

### Adding, Removing, and Reordering Entries

- [- addObject:](<add(__).md>) — Appends a given object to the end of the mutable ordered set, if it is not already a member.
- [- addObjects:count:](<add(__count_).md>) — Appends the given number of objects from a given C array to the end of the mutable ordered set.
- [- addObjectsFromArray:](<addobjects(from_).md>) — Appends to the end of the mutable ordered set each object contained in a given array that is not already a member.
- [- insertObject:atIndex:](<insert(__at_)-7qg51.md>) — Inserts the given object at the specified index of the mutable ordered set, if it is not already a member.
- [- insertObjects:atIndexes:](<insert(__at_)-3ncnm.md>) — Inserts the objects in the array at the specified indexes.
- [- removeObject:](<remove(__).md>) — Removes a given object from the mutable ordered set.
- [- removeObjectAtIndex:](<removeobject(at_).md>) — Removes a the object at the specified index from the mutable ordered set.
- [- removeObjectsAtIndexes:](<removeobjects(at_).md>) — Removes the objects at the specified indexes from the mutable ordered set.
- [- removeObjectsInArray:](<removeobjects(in_)-8h2kh.md>) — Removes the objects in the array from the mutable ordered set.
- [- removeObjectsInRange:](<removeobjects(in_)-9jkis.md>) — Removes from the mutable ordered set each of the objects within a given range.
- [- removeAllObjects](<removeallobjects().md>) — Removes all the objects from the mutable ordered set.
- [- replaceObjectAtIndex:withObject:](<replaceobject(at_with_).md>) — Replaces the object at the specified index with the new object.
- [- replaceObjectsAtIndexes:withObjects:](<replaceobjects(at_with_).md>) — Replaces the objects at the specified indexes with the new objects.
- [- replaceObjectsInRange:withObjects:count:](<replaceobjects(in_with_count_).md>) — Replaces the objects in the receiving mutable ordered set at the range with the specified number of objects from a given C array.
- [- setObject:atIndex:](<setobject(__at_).md>) — Appends or replaces the object at the specified index.
