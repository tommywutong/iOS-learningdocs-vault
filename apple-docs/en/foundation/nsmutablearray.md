---
title: NSMutableArray
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutablearray
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray.json'
content_hash: 'sha256:fee5e1171c6781d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMutableArray

<sub>Class</sub>

A dynamic ordered collection of objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMutableArray
```

## Overview

You can use this type in Swift instead of an [Array](../swift/array.md) variable in cases that require reference semantics.

The `NSMutableArray` class declares the programmatic interface to objects that manage a modifiable array of objects. This class adds insertion and deletion operations to the basic array-handling behavior inherited from [NSArray](nsarray.md).

NSMutableArray is “toll-free bridged” with its Core Foundation counterpart, [CFMutableArray](../corefoundation/cfmutablearray.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

### Accessing Values Using Subscripting

In addition to the provided instance methods, such as [- replaceObjectAtIndex:withObject:](<nsmutablearray/replaceobject(at_with_).md>), you can access `NSArray` values by their indexes using _subscripting_.

**Swift**

```swift
mutableArray[3] = "someValue"
```

**Objective-C**

```objc
mutableArray[3] = @"someValue";
```

### Subclassing Notes

There is typically little reason to subclass `NSMutableArray`. The class does well what it is designed to do—maintain a mutable, ordered collection of objects. But there are situations where a custom `NSArray` object might come in handy. Here are a few possibilities:

- Changing how `NSMutableArray` stores the elements of its collection. You might do this for performance reasons or for better compatibility with legacy code.
- Acquiring more information about what is happening to the collection (for example, statistics gathering).

#### Methods to Override

`NSMutableArray` defines five primitive methods:

- [- insertObject:atIndex:](<nsmutablearray/insert(__at_)-5dbx5.md>)
- [- removeObjectAtIndex:](<nsmutablearray/removeobject(at_).md>)
- [- addObject:](<nsmutablearray/add(__).md>)
- [- removeLastObject](<nsmutablearray/removelastobject().md>)
- [- replaceObjectAtIndex:withObject:](<nsmutablearray/replaceobject(at_with_).md>)

In a subclass, you must override all these methods. You must also override the primitive methods of the [NSArray](nsarray.md) class.

## Relationships

- **Inherits From**: [NSArray](nsarray.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Creating and Initializing a Mutable Array

- [init(contentsOfURL:)](<nsmutablearray/init(contentsofurl_).md>) — Creates and returns a mutable array containing the contents specified by a given URL.
- [- init](<nsmutablearray/init().md>) — Initializes a newly allocated array.
- [- initWithCapacity:](<nsmutablearray/init(capacity_).md>) — Returns an array, initialized with enough memory to initially hold a given number of objects.

### Adding Objects

- [- addObject:](<nsmutablearray/add(__).md>) — Inserts a given object at the end of the array.
- [- addObjectsFromArray:](<nsmutablearray/addobjects(from_).md>) — Adds the objects contained in another given array to the end of the receiving array’s content.
- [- insertObject:atIndex:](<nsmutablearray/insert(__at_)-5dbx5.md>) — Inserts a given object into the array’s contents at a given index.
- [- insertObjects:atIndexes:](<nsmutablearray/insert(__at_)-73pln.md>) — Inserts the objects in the provided array into the receiving array at the specified indexes.

### Removing Objects

- [- removeAllObjects](<nsmutablearray/removeallobjects().md>) — Empties the array of all its elements.
- [- removeLastObject](<nsmutablearray/removelastobject().md>) — Removes the object with the highest-valued index in the array
- [- removeObject:](<nsmutablearray/remove(__).md>) — Removes all occurrences in the array of a given object.
- [- removeObject:inRange:](<nsmutablearray/remove(__in_).md>) — Removes all occurrences within a specified range in the array of a given object.
- [- removeObjectAtIndex:](<nsmutablearray/removeobject(at_).md>) — Removes the object at `index` .
- [- removeObjectsAtIndexes:](<nsmutablearray/removeobjects(at_).md>) — Removes the objects at the specified indexes from the array.
- [- removeObjectIdenticalTo:](<nsmutablearray/removeobject(identicalto_).md>) — Removes all occurrences of a given object in the array.
- [- removeObjectIdenticalTo:inRange:](<nsmutablearray/removeobject(identicalto_in_).md>) — Removes all occurrences of `anObject` within the specified range in the array.
- [- removeObjectsFromIndices:numIndices:](<nsmutablearray/removeobjects(fromindices_numindices_).md>) — Removes the specified number of objects from the array, beginning at the specified index. _(deprecated)_
- [- removeObjectsInArray:](<nsmutablearray/removeobjects(in_)-4yb26.md>) — Removes from the receiving array the objects in another given array.
- [- removeObjectsInRange:](<nsmutablearray/removeobjects(in_)-1udmn.md>) — Removes from the array each of the objects within a given range.

### Replacing Objects

- [- replaceObjectAtIndex:withObject:](<nsmutablearray/replaceobject(at_with_).md>) — Replaces the object at `index` with `anObject`.
- [- replaceObjectsAtIndexes:withObjects:](<nsmutablearray/replaceobjects(at_with_).md>) — Replaces the objects in the receiving array at locations specified with the objects from a given array.
- [- replaceObjectsInRange:withObjectsFromArray:range:](<nsmutablearray/replaceobjects(in_withobjectsfrom_range_).md>) — Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [- replaceObjectsInRange:withObjectsFromArray:](<nsmutablearray/replaceobjects(in_withobjectsfrom_).md>) — Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.
- [- setArray:](<nsmutablearray/setarray(__).md>) — Sets the receiving array’s elements to those in another given array.

### Filtering Content

- [- filterUsingPredicate:](<nsmutablearray/filter(using_).md>) — Evaluates a given predicate against the array’s content and leaves only objects that match.

### Rearranging Content

- [- exchangeObjectAtIndex:withObjectAtIndex:](<nsmutablearray/exchangeobject(at_withobjectat_).md>) — Exchanges the objects in the array at given indexes.
- [- sortUsingDescriptors:](<nsmutablearray/sort(using_)-4eh07.md>) — Sorts the receiver using a given array of sort descriptors.
- [- sortUsingComparator:](<nsmutablearray/sort(comparator_).md>) — Sorts the receiver in ascending order using the comparison method specified by a given [Comparator](comparator.md) block.
- [- sortWithOptions:usingComparator:](<nsmutablearray/sort(options_usingcomparator_).md>) — Sorts the receiver in ascending order using the specified options and the comparison method specified by a given [Comparator](comparator.md) block.
- [- sortUsingFunction:context:](<nsmutablearray/sort(__context_).md>) — Sorts the receiver in ascending order as defined by the comparison function `compare`.
- [- sortUsingSelector:](<nsmutablearray/sort(using_)-537vs.md>) — Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.

### Initializers

- [- initWithCoder:](<nsmutablearray/init(coder_).md>)
- [init(objects:count:)](<nsmutablearray/init(objects_count_).md>)

### Default Implementations

- [NSMutableArray Implementations](nsmutablearray/nsmutablearray-implementations.md)
