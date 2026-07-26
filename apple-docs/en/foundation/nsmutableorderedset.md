---
title: NSMutableOrderedSet
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutableorderedset
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableorderedset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableorderedset.json'
content_hash: 'sha256:f8544c154c393e0e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMutableOrderedSet

<sub>Class</sub>

A dynamic, ordered collection of unique objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMutableOrderedSet
```

## Overview

[NSMutableOrderedSet](nsmutableorderedset.md) objects are not like C arrays. That is, even though you may specify a size when you create a mutable ordered set, the specified size is regarded as a “hint”; the actual size of the set is still 0. This means that you cannot insert an object at an index greater than the current count of an set. For example, if a set contains two objects, its size is 2, so you can add objects at indices 0, 1, or 2. Index 3 is illegal and out of bounds; if you try to add an object at index 3 (when the size of the array is 2), `NSMutableOrderedSet` raises an exception.

## Relationships

- **Inherits From**: [NSOrderedSet](nsorderedset.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Creating a Mutable Ordered Set

- [- initWithCapacity:](<nsmutableorderedset/init(capacity_).md>) — Returns an initialized mutable ordered set with a given initial capacity.
- [- init](<nsmutableorderedset/init().md>) — Initializes a newly allocated mutable ordered set.

### Adding, Removing, and Reordering Entries

- [- addObject:](<nsmutableorderedset/add(__).md>) — Appends a given object to the end of the mutable ordered set, if it is not already a member.
- [- addObjects:count:](<nsmutableorderedset/add(__count_).md>) — Appends the given number of objects from a given C array to the end of the mutable ordered set.
- [- addObjectsFromArray:](<nsmutableorderedset/addobjects(from_).md>) — Appends to the end of the mutable ordered set each object contained in a given array that is not already a member.
- [- insertObject:atIndex:](<nsmutableorderedset/insert(__at_)-7qg51.md>) — Inserts the given object at the specified index of the mutable ordered set, if it is not already a member.
- [- insertObjects:atIndexes:](<nsmutableorderedset/insert(__at_)-3ncnm.md>) — Inserts the objects in the array at the specified indexes.
- [- removeObject:](<nsmutableorderedset/remove(__).md>) — Removes a given object from the mutable ordered set.
- [- removeObjectAtIndex:](<nsmutableorderedset/removeobject(at_).md>) — Removes a the object at the specified index from the mutable ordered set.
- [- removeObjectsAtIndexes:](<nsmutableorderedset/removeobjects(at_).md>) — Removes the objects at the specified indexes from the mutable ordered set.
- [- removeObjectsInArray:](<nsmutableorderedset/removeobjects(in_)-8h2kh.md>) — Removes the objects in the array from the mutable ordered set.
- [- removeObjectsInRange:](<nsmutableorderedset/removeobjects(in_)-9jkis.md>) — Removes from the mutable ordered set each of the objects within a given range.
- [- removeAllObjects](<nsmutableorderedset/removeallobjects().md>) — Removes all the objects from the mutable ordered set.
- [- replaceObjectAtIndex:withObject:](<nsmutableorderedset/replaceobject(at_with_).md>) — Replaces the object at the specified index with the new object.
- [- replaceObjectsAtIndexes:withObjects:](<nsmutableorderedset/replaceobjects(at_with_).md>) — Replaces the objects at the specified indexes with the new objects.
- [- replaceObjectsInRange:withObjects:count:](<nsmutableorderedset/replaceobjects(in_with_count_).md>) — Replaces the objects in the receiving mutable ordered set at the range with the specified number of objects from a given C array.
- [- setObject:atIndex:](<nsmutableorderedset/setobject(__at_).md>) — Appends or replaces the object at the specified index.
- [- moveObjectsAtIndexes:toIndex:](<nsmutableorderedset/moveobjects(at_to_).md>) — Moves the objects at the specified indexes to the new location.
- [- exchangeObjectAtIndex:withObjectAtIndex:](<nsmutableorderedset/exchangeobject(at_withobjectat_).md>) — Exchanges the object at the specified index with the object at the other index.
- [- filterUsingPredicate:](<nsmutableorderedset/filter(using_).md>) — Evaluates a given predicate against the mutable ordered set’s content and leaves only objects that match.

### Sorting Entries

- [- sortUsingDescriptors:](<nsmutableorderedset/sort(using_).md>) — Sorts the receiving ordered set using a given array of sort descriptors.
- [- sortUsingComparator:](<nsmutableorderedset/sort(comparator_).md>) — Sorts the mutable ordered set using the comparison method specified by the comparator block.
- [- sortWithOptions:usingComparator:](<nsmutableorderedset/sort(options_usingcomparator_).md>) — Sorts the mutable ordered set using the specified options and the comparison method specified by a given comparator block.
- [- sortRange:options:usingComparator:](<nsmutableorderedset/sortrange(__options_usingcomparator_).md>) — Sorts the specified range of the mutable ordered set using the specified options and the comparison method specified by a given comparator block.

### Combining and Recombining Entries

- [- intersectOrderedSet:](<nsmutableorderedset/intersect(__).md>) — Removes from the receiving ordered set each object that isn’t a member of another ordered set.
- [- intersectSet:](<nsmutableorderedset/intersectset(__).md>) — Removes from the receiving ordered set each object that isn’t a member of another set.
- [- minusOrderedSet:](<nsmutableorderedset/minus(__).md>) — Removes each object in another given ordered set from the receiving mutable ordered set, if present.
- [- minusSet:](<nsmutableorderedset/minusset(__).md>) — Removes each object in another given set from the receiving mutable ordered set, if present.
- [- unionOrderedSet:](<nsmutableorderedset/union(__).md>) — Adds each object in another given ordered set to the receiving mutable ordered set, if not present.
- [- unionSet:](<nsmutableorderedset/unionset(__).md>) — Adds each object in another given set to the receiving mutable ordered set, if not present.

### Initializers

- [- initWithCoder:](<nsmutableorderedset/init(coder_).md>)
- [init(objects:count:)](<nsmutableorderedset/init(objects_count_).md>)

## See Also

### Specialized Sets

- [NSCountedSet](nscountedset.md) — A mutable, unordered collection of distinct objects that may appear more than once in the collection.
- [NSOrderedSet](nsorderedset.md) — A static, ordered collection of unique objects.
