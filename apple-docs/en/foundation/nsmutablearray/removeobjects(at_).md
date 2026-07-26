---
title: 'removeObjects(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/removeobjects(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/removeobjects(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/removeobjects%28at%3A%29.json'
content_hash: 'sha256:4b2831f3856ebb26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# removeObjects(at:)

<sub>Instance Method</sub>

Removes the objects at the specified indexes from the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObjects(at indexes: IndexSet)
```

## Parameters

- `indexes` — The indexes of the objects to remove from the array. The locations specified by `indexes` must lie within the bounds of the array.

## Discussion

This method is similar to [- removeObjectAtIndex:](<removeobject(at_).md>), but allows you to efficiently remove multiple objects with a single operation. `indexes` specifies the locations of objects to be removed given the state of the array when the method is invoked, as illustrated in the following example:

```objc
NSMutableArray *array = [NSMutableArray arrayWithObjects: @"one", @"a", @"two", @"b", @"three", @"four", nil];
NSMutableIndexSet *indexes = [NSMutableIndexSet indexSetWithIndex:1];
[indexes addIndex:3];
[array removeObjectsAtIndexes:indexes];
NSLog(@"array: %@", array);
 
// Output: array: (one, two, three, four)
```

If `indexes` is `nil`, this method raises an exception.

## See Also

### Related Documentation

- [- initWithCapacity:](<init(capacity_).md>) — Returns an array, initialized with enough memory to initially hold a given number of objects.

### Removing Objects

- [- removeAllObjects](<removeallobjects().md>) — Empties the array of all its elements.
- [- removeLastObject](<removelastobject().md>) — Removes the object with the highest-valued index in the array
- [- removeObject:](<remove(__).md>) — Removes all occurrences in the array of a given object.
- [- removeObject:inRange:](<remove(__in_).md>) — Removes all occurrences within a specified range in the array of a given object.
- [- removeObjectAtIndex:](<removeobject(at_).md>) — Removes the object at `index` .
- [- removeObjectIdenticalTo:](<removeobject(identicalto_).md>) — Removes all occurrences of a given object in the array.
- [- removeObjectIdenticalTo:inRange:](<removeobject(identicalto_in_).md>) — Removes all occurrences of `anObject` within the specified range in the array.
- [- removeObjectsFromIndices:numIndices:](<removeobjects(fromindices_numindices_).md>) — Removes the specified number of objects from the array, beginning at the specified index. _(deprecated)_
- [- removeObjectsInArray:](<removeobjects(in_)-4yb26.md>) — Removes from the receiving array the objects in another given array.
- [- removeObjectsInRange:](<removeobjects(in_)-1udmn.md>) — Removes from the array each of the objects within a given range.
