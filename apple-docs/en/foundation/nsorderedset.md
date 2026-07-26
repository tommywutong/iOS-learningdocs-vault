---
title: NSOrderedSet
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorderedset
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset.json'
content_hash: 'sha256:8346d4f652486e78'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSOrderedSet

<sub>Class</sub>

A static, ordered collection of unique objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSOrderedSet
```

## Overview

[NSOrderedSet](nsorderedset.md) declares the programmatic interface for static sets of distinct objects. You establish a static set’s entries when it’s created, and thereafter the entries can’t be modified. [NSMutableOrderedSet](nsmutableorderedset.md), on the other hand, declares a programmatic interface for dynamic sets of distinct objects. A dynamic—or mutable—set allows the addition and deletion of entries at any time, automatically allocating memory as needed.

You can use ordered sets as an alternative to arrays when the order of elements is important and performance in testing whether an object is contained in the set is a consideration—testing for membership of an array is slower than testing for membership of a set.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSMutableOrderedSet](nsmutableorderedset.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sequence](../swift/sequence.md)

## Topics

### Creating an Ordered Set

- [+ orderedSetWithObjects:count:](<nsorderedset/init(objects_count_)-3ny0m.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.

### Initializing an Ordered Set

- [- initWithArray:](<nsorderedset/init(array_).md>) — Initializes a newly allocated set with the objects that are contained in a given array.
- [- initWithArray:copyItems:](<nsorderedset/init(array_copyitems_).md>) — Initializes a newly allocated set with the objects that are contained in a given array, optionally copying the items.
- [- initWithArray:range:copyItems:](<nsorderedset/init(array_range_copyitems_).md>) — Initializes a newly allocated set with the objects that are contained in the specified range of an array, optionally copying the items.
- [- initWithObject:](<nsorderedset/init(object_).md>) — Initializes a new ordered set with the object.
- [- initWithObjects:count:](<nsorderedset/init(objects_count_)-2ai32.md>) — Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [- initWithOrderedSet:](<nsorderedset/init(orderedset_).md>) — Initializes a new ordered set with the contents of a set.
- [- initWithOrderedSet:copyItems:](<nsorderedset/init(orderedset_copyitems_).md>) — Initializes a new ordered set with the contents of a set, optionally copying the items.
- [- initWithOrderedSet:range:copyItems:](<nsorderedset/init(orderedset_range_copyitems_).md>) — Initializes a new ordered set with the contents of an ordered set, optionally copying the items.
- [- initWithSet:](<nsorderedset/init(set_).md>) — Initializes a new ordered set with the contents of a set.
- [- initWithSet:copyItems:](<nsorderedset/init(set_copyitems_).md>) — Initializes a new ordered set with the contents of a set, optionally copying the objects in the set.
- [- init](<nsorderedset/init().md>) — Initializes a newly allocated ordered set.

### Counting Entries

- [count](nsorderedset/count.md) — The number of members in the set.

### Accessing Set Members

- [- containsObject:](<nsorderedset/contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the ordered set.
- [- enumerateObjectsAtIndexes:options:usingBlock:](<nsorderedset/enumerateobjects(at_options_using_).md>) — Executes a given block using the objects in the ordered set at the specified indexes.
- [- enumerateObjectsUsingBlock:](<nsorderedset/enumerateobjects(__).md>) — Executes a given block using each object in the ordered set.
- [- enumerateObjectsWithOptions:usingBlock:](<nsorderedset/enumerateobjects(options_using_).md>) — Executes a given block using each object in the set, using the specified enumeration options.
- [firstObject](nsorderedset/firstobject.md) — The first object in the ordered set.
- [lastObject](nsorderedset/lastobject.md) — The last object in the ordered set.
- [- objectAtIndex:](<nsorderedset/object(at_).md>) — Returns the object at the specified index of the set.
- [- objectAtIndexedSubscript:](<nsorderedset/subscript(__).md>) — Returns the object at the specified index of the set.
- [- objectsAtIndexes:](<nsorderedset/objects(at_).md>) — Returns the objects in the ordered set at the specified indexes.
- [- indexOfObject:](<nsorderedset/index(of_).md>) — Returns the index of the specified object.
- [- indexOfObject:inSortedRange:options:usingComparator:](<nsorderedset/index(of_insortedrange_options_usingcomparator_).md>) — Returns the index, within a specified range, of an object compared with elements in the ordered set using a given NSComparator block.
- [- indexOfObjectAtIndexes:options:passingTest:](<nsorderedset/index(ofobjectat_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexOfObjectPassingTest:](<nsorderedset/index(ofobjectpassingtest_).md>) — Returns the index of the object in the ordered set that passes a test in a given block.
- [- indexOfObjectWithOptions:passingTest:](<nsorderedset/index(__ofobjectpassingtest_).md>) — Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsAtIndexes:options:passingTest:](<nsorderedset/indexes(ofobjectsat_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsPassingTest:](<nsorderedset/indexes(ofobjectspassingtest_).md>) — Returns the index of the object in the ordered set that passes a test in a given block.
- [- indexesOfObjectsWithOptions:passingTest:](<nsorderedset/indexes(options_ofobjectspassingtest_).md>) — Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- objectEnumerator](<nsorderedset/objectenumerator().md>) — Returns an enumerator object that lets you access each object in the ordered set.
- [- reverseObjectEnumerator](<nsorderedset/reverseobjectenumerator().md>) — Returns an enumerator object that lets you access each object in the ordered set.
- [reversedOrderedSet](nsorderedset/reversed.md) — An ordered set in the reverse order.

### Key-Value Coding Support

- [- setValue:forKey:](<nsorderedset/setvalue(__forkey_).md>) — Invokes `setValue:forKey:` on each of the receiver’s members using the specified value and key
- [- valueForKey:](<nsorderedset/value(forkey_).md>) — Returns an ordered set containing the results of invoking `valueForKey:` using key on each of the ordered set’s objects.

### Key-Value Observing Support

- [- addObserver:forKeyPath:options:context:](<nsorderedset/addobserver(__forkeypath_options_context_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:](<nsorderedset/removeobserver(__forkeypath_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:context:](<nsorderedset/removeobserver(__forkeypath_context_).md>) — Raises an exception.

### Comparing Sets

- [- isEqualToOrderedSet:](<nsorderedset/isequal(to_).md>) — Compares the receiving ordered set to another ordered set.
- [- intersectsOrderedSet:](<nsorderedset/intersects(__).md>) — Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given ordered set.
- [- intersectsSet:](<nsorderedset/intersectsset(__).md>) — Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given set.
- [- isSubsetOfOrderedSet:](<nsorderedset/issubset(of_)-7brc.md>) — Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given ordered set.
- [- isSubsetOfSet:](<nsorderedset/issubset(of_)-8zx9x.md>) — Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given set.

### Creating a Sorted Array

- [- sortedArrayUsingDescriptors:](<nsorderedset/sortedarray(using_).md>) — Returns an array of the ordered set’s elements sorted as specified by a given array of sort descriptors.
- [- sortedArrayUsingComparator:](<nsorderedset/sortedarray(comparator_).md>) — Returns an array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block
- [- sortedArrayWithOptions:usingComparator:](<nsorderedset/sortedarray(options_usingcomparator_).md>) — Returns an array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.

### Filtering Ordered Sets

- [- filteredOrderedSetUsingPredicate:](<nsorderedset/filtered(using_).md>) — Evaluates a given predicate against each object in the receiving ordered set and returns a new ordered set containing the objects for which the predicate returns true.

### Describing a Set

- [description](nsorderedset/description.md) — A string that represents the contents of the ordered set, formatted as a property list.
- [- descriptionWithLocale:](<nsorderedset/description(withlocale_).md>) — Returns a string that represents the contents of the ordered set, formatted as a property list.
- [- descriptionWithLocale:indent:](<nsorderedset/description(withlocale_indent_).md>) — Returns a string that represents the contents of the ordered set, formatted as a property list.

### Converting Other Collections

- [array](nsorderedset/array.md) — A representation of the ordered set as an array.
- [set](nsorderedset/set.md) — A representation of the set containing the contents of the ordered set.

### Comparing with Another Set

- [NSOrderedCollectionDifference](nsorderedcollectiondifference.md) — An object representing the difference between two ordered collections.
- [NSOrderedCollectionDifferenceCalculationOptions](nsorderedcollectiondifferencecalculationoptions.md) — Constants that specify the options to use when creating an ordered collection difference.

### Initializers

- [- initWithCoder:](<nsorderedset/init(coder_).md>)
- [init(objects:)](<nsorderedset/init(objects_).md>)

### Default Implementations

- [ExpressibleByArrayLiteral Implementations](nsorderedset/expressiblebyarrayliteral-implementations.md)
- [Sequence Implementations](nsorderedset/sequence-implementations.md)

## See Also

### Specialized Sets

- [NSCountedSet](nscountedset.md) — A mutable, unordered collection of distinct objects that may appear more than once in the collection.
- [NSMutableOrderedSet](nsmutableorderedset.md) — A dynamic, ordered collection of unique objects.
