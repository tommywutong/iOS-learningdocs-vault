---
title: NSSet
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsset
source_url: 'https://developer.apple.com/documentation/foundation/nsset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset.json'
content_hash: 'sha256:ba6b6bd5741f636b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSet

<sub>Class</sub>

A static, unordered collection of unique objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSSet
```

## Overview

The [NSSet](nsset.md), [NSMutableSet](nsmutableset.md), and [NSCountedSet](nscountedset.md) classes declare the programmatic interface to an unordered collection of objects.

[NSSet](nsset.md) declares the programmatic interface for static sets of distinct objects. You establish a static set’s entries when it’s created, and can’t modify the entries after that. [NSMutableSet](nsmutableset.md), on the other hand, declares a programmatic interface for dynamic sets of distinct objects. A dynamic — or mutable — set allows the addition and deletion of entries at any time, automatically allocating memory as needed.

Use sets as an alternative to arrays when the order of elements isn’t important and you need to consider performance in testing whether the set contains an object. With an array, testing for membership is slower than with sets.

[NSSet](nsset.md) is “toll-free bridged” with its Core Foundation counterpart, [CFSet](../corefoundation/cfset.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

In Swift, use this class instead of a [Set](../swift/set.md) constant in cases where you require reference semantics.

### Subclassing Notes

There should be little need of subclassing. If you need to customize behavior, it’s often better to consider composition instead of subclassing.

#### Methods to Override

In a subclass, you must override all of its primitive methods:

- [count](nsset/count.md)
- [- member:](<nsset/member(__).md>)
- [- objectEnumerator](<nsset/objectenumerator().md>)

#### Alternatives to Subclassing

Before making a custom class of [NSSet](nsset.md), investigate [NSHashTable](nshashtable.md) and the corresponding Core Foundation type, [CFSet](../corefoundation/cfset.md). Because [NSSet](nsset.md) and [CFSet](../corefoundation/cfset.md) are “toll-free bridged,” you can substitute a [CFSet](../corefoundation/cfset.md) object for a [NSSet](nsset.md) object in your code (with appropriate casting). Although they’re corresponding types, [CFSet](../corefoundation/cfset.md) and [NSSet](nsset.md) don’t have identical interfaces or implementations, and you can sometimes do things with [CFSet](../corefoundation/cfset.md) that you can’t easily do with [NSSet](nsset.md).

If the behavior you want to add supplements that of the existing class, you could write a category on [NSSet](nsset.md). Keep in mind, however, that this category affects all instances of [NSSet](nsset.md) that you use, and this might have unintended consequences. Alternatively, you could use composition to achieve the desired behavior.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSMutableSet](nsmutableset.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sequence](../swift/sequence.md)

## Topics

### Creating a Set

- [+ setWithObject:](<nsset/init(object_).md>) — Creates and returns a set that contains a single given object.
- [+ setWithObjects:count:](<nsset/init(objects_count_)-65ni4.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.
- [- setByAddingObject:](<nsset/adding(__).md>) — Returns a new set formed by adding a given object to the receiving set.
- [- setByAddingObjectsFromSet:](<nsset/addingobjects(from_)-2i31h.md>) — Returns a new set formed by adding the objects in a given set to the receiving set.
- [- setByAddingObjectsFromArray:](<nsset/addingobjects(from_)-544m9.md>) — Returns a new set formed by adding the objects in a given array to the receiving set.

### Initializing a Set

- [- initWithArray:](<nsset/init(array_).md>) — Initializes a newly allocated set with the objects that are contained in a given array.
- [- initWithObjects:count:](<nsset/init(objects_count_)-7kift.md>) — Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [- initWithSet:](<nsset/init(set_)-1xovx.md>) — Initializes a newly allocated set and adds to it objects from another given set.
- [- initWithSet:copyItems:](<nsset/init(set_copyitems_).md>) — Initializes a newly allocated set and adds to it members of another given set.
- [- init](<nsset/init().md>) — Initializes a newly allocated set.

### Counting Entries

- [count](nsset/count.md) — The number of members in the set.

### Accessing Set Members

- [allObjects](nsset/allobjects.md) — An array containing the set’s members, or an empty array if the set has no members.
- [- anyObject](<nsset/anyobject().md>) — Returns one of the objects in the set, or `nil` if the set contains no objects.
- [- containsObject:](<nsset/contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the set.
- [- filteredSetUsingPredicate:](<nsset/filtered(using_).md>) — Evaluates a given predicate against each object in the receiving set and returns a new set containing the objects for which the predicate returns true.
- [- member:](<nsset/member(__).md>) — Determines whether a given object is present in the set, and returns that object if it is.
- [- objectEnumerator](<nsset/objectenumerator().md>) — Returns an enumerator object that lets you access each object in the set.
- [- enumerateObjectsUsingBlock:](<nsset/enumerateobjects(__).md>) — Executes a given block using each object in the set.
- [- enumerateObjectsWithOptions:usingBlock:](<nsset/enumerateobjects(options_using_).md>) — Executes a given block using each object in the set, using the specified enumeration options.
- [- objectsPassingTest:](<nsset/objects(passingtest_).md>) — Returns a set of objects that pass a test in a given block.
- [- objectsWithOptions:passingTest:](<nsset/objects(options_passingtest_).md>) — Returns a set of objects that pass a test in a given block, using the specified enumeration options.

### Comparing Sets

- [- isSubsetOfSet:](<nsset/issubset(of_).md>) — Returns a Boolean value that indicates whether every object in the receiving set is also present in another given set.
- [- intersectsSet:](<nsset/intersects(__).md>) — Returns a Boolean value that indicates whether at least one object in the receiving set is also present in another given set.
- [- isEqualToSet:](<nsset/isequal(to_).md>) — Compares the receiving set to another set.
- [- valueForKey:](<nsset/value(forkey_).md>) — Return a set containing the results of invoking `valueForKey:` on each of the receiving set’s members.
- [- setValue:forKey:](<nsset/setvalue(__forkey_).md>) — Invokes `setValue:forKey:` on each of the set’s members.

### Creating a Sorted Array

- [- sortedArrayUsingDescriptors:](<nsset/sortedarray(using_).md>) — Returns an array of the set’s content sorted as specified by a given array of sort descriptors.

### Key-Value Observing

- [- addObserver:forKeyPath:options:context:](<nsset/addobserver(__forkeypath_options_context_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:context:](<nsset/removeobserver(__forkeypath_context_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:](<nsset/removeobserver(__forkeypath_).md>) — Raises an exception.

### Describing a Set

- [description](nsset/description.md) — A string that represents the contents of the set, formatted as a property list.
- [- descriptionWithLocale:](<nsset/description(withlocale_).md>) — Returns a string that represents the contents of the set, formatted as a property list.

### Initializers

- [- initWithCoder:](<nsset/init(coder_).md>)
- [+ setWithCollectionViewIndexPath:](<nsset/init(collectionviewindexpath_).md>)
- [+ setWithCollectionViewIndexPaths:](<nsset/init(collectionviewindexpaths_).md>)
- [init(objects:)](<nsset/init(objects_).md>)
- [init(set:)](<nsset/init(set_)-7a7ws.md>) — Initializes a newly allocated set and adds to it objects from another given set.

### Instance Methods

- [- enumerateIndexPathsWithOptions:usingBlock:](<nsset/enumerateindexpaths(options_using_).md>)

### Default Implementations

- [Sequence Implementations](nsset/sequence-implementations.md)
