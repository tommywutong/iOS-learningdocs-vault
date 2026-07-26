---
title: 'moveObjects(at:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableorderedset/moveobjects(at:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableorderedset/moveobjects(at:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableorderedset/moveobjects%28at%3Ato%3A%29.json'
content_hash: 'sha256:e43b83c9b09b3768'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableOrderedSet](../nsmutableorderedset.md)

# moveObjects(at:to:)

<sub>Instance Method</sub>

Moves the objects at the specified indexes to the new location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func moveObjects(at indexes: IndexSet, to idx: Int)
```

## Parameters

- `indexes` — The indexes of the objects to move.

- `idx` — The index in the mutable ordered set at which to insert the objects. The objects being moved are first removed from the set, then this index is used to find the location at which to insert the moved objects.

## Discussion

For example, the following code results in the contents of `mySet` being equal to `["a", "c", "b", "d", "e"]:`

**Swift**

```swift
let movedObjectIndexes = NSMutableIndexSet()
movedObjectIndexes.addIndex(1)
movedObjectIndexes.addIndex(3)
 
let mySet = NSMutableOrderedSet(capacity: 5)
mySet.addObject("a")
mySet.addObject("b")
mySet.addObject("c")
mySet.addObject("d")
mySet.addObject("e")
 
mySet.moveObjectsAtIndexes(movedObjectIndexes, toIndex: 2)
```

**Objective-C**

```objc
NSMutableIndexSet *movedObjectIndexes = [NSMutableIndexSet indexSet];
[movedObjectIndexes addIndex: 1];
[movedObjectIndexes addIndex: 3];
 
NSMutableOrderedSet *mySet = [NSMutableOrderedSet orderedSetWithCapacity:5];
[mySet addObject:@"a"];
[mySet addObject:@"b"];
[mySet addObject:@"c"];
[mySet addObject:@"d"];
[mySet addObject:@"e"];
 
[mySet moveObjectsAtIndexes:movedObjectIndexes toIndex:2];
```

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
