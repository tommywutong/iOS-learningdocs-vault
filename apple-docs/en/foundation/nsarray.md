---
title: NSArray
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsarray
source_url: 'https://developer.apple.com/documentation/foundation/nsarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray.json'
content_hash: 'sha256:d94fc683ce71e588'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSArray

<sub>Class</sub>

A static ordered collection of objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSArray
```

## Overview

You can use this type in Swift instead of an [Array](../swift/array.md) constant in cases that require reference semantics.

`NSArray` and its subclass [NSMutableArray](nsmutablearray.md) manage ordered collections of objects called **arrays**. `NSArray` creates static arrays, and `NSMutableArray` creates dynamic arrays. You can use arrays when you need an ordered collection of objects.

`NSArray` is “toll-free bridged” with its Core Foundation counterpart, [CFArray](../corefoundation/cfarray.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

### Creating NSArray Objects Using Array Literals

In addition to the provided initializers, such as [initWithObjects:](nsarray/initwithobjects_.md), you can create an `NSArray` object using an _array literal_.

**Swift**

```swift
let array: NSArray = [someObject, "Hello, World!", 42]
```

**Objective-C**

```objc
NSArray *array = @[someObject, @"Hello, World!", @42];
```

In Objective-C, the compiler generates code that makes an underlying call to the [+ arrayWithObjects:count:](<nsarray/init(objects_count_)-7dct1.md>) method.

```objc
id objects[] = { someObject, @"Hello, World!", @42 };
NSUInteger count = sizeof(objects) / sizeof(id);
NSArray *array = [NSArray arrayWithObjects:objects
                                     count:count];
```

You should not terminate the list of objects with `nil` when using this literal syntax, and in fact `nil` is an invalid value. For more information about object literals in Objective-C, see [Working with Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithObjects/WorkingwithObjects.html#//apple_ref/doc/uid/TP40011210-CH4) in [Programming with Objective-C](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011210).

In Swift, the `NSArray` class conforms to the `ArrayLiteralConvertible` protocol, which allows it to be initialized with array literals. For more information about object literals in Swift, see [Literal Expression](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/Expressions.html#//apple_ref/doc/uid/TP40014097-CH32-ID390) in [The Swift Programming Language (Swift 4.1)](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/index.html#//apple_ref/doc/uid/TP40014097).

### Accessing Values Using Subscripting

In addition to the provided instance methods, such as [- objectAtIndex:](<nsarray/object(at_).md>), you can access `NSArray` values by their indexes using _subscripting_.

**Swift**

```swift
let value = array[3]
```

**Objective-C**

```objc
id value = array[3];
```

### Subclassing Notes

There is typically little reason to subclass `NSArray`. The class does well what it is designed to do—maintain an ordered collection of objects. But there are situations where a custom `NSArray` object might come in handy. Here are a few possibilities:

- Changing how `NSArray` stores the elements of its collection. You might do this for performance reasons or for better compatibility with legacy code.
- Acquiring more information about what is happening to the collection (for example, statistics gathering).

#### Methods to Override

Any subclass of `NSArray`    _must_ override the primitive instance methods [count](nsarray/count.md) and [- objectAtIndex:](<nsarray/object(at_).md>). These methods must operate on the backing store that you provide for the elements of the collection. For this backing store you can use a static array, a standard `NSArray` object, or some other data type or mechanism. You may also choose to override, partially or fully, any other `NSArray` method for which you want to provide an alternative implementation.

You might want to implement an initializer for your subclass that is suited to the backing store that the subclass is managing. If you do, your initializer must invoke one of the designated initializers of the `NSArray` class, either [- init](<nsarray/init().md>) or [- initWithObjects:count:](<nsarray/init(objects_count_)-5odxv.md>). The `NSArray` class adopts the [NSCopying](nscopying.md), [NSMutableCopying](nsmutablecopying.md), and [NSCoding](nscoding.md) protocols; custom subclasses of `NSArray` should override the methods in these protocols as necessary.

Remember that `NSArray` is the public interface for a class cluster and what this entails for your subclass. You must provide the storage for your subclass and implement the primitive methods that directly act on that storage.

#### Alternatives to Subclassing

Before making a custom subclass of `NSArray`, investigate [NSPointerArray](nspointerarray.md) and the corresponding Core Foundation type, [CFArray](../corefoundation/cfarray.md). Because `NSArray` and `CFArray` are “toll-free bridged,” you can substitute a `CFArray` object for a `NSArray` object in your code (with appropriate casting). Although they are corresponding types, `CFArray` and `NSArray` do not have identical interfaces or implementations, and you can sometimes do things with `CFArray` that you cannot easily do with `NSArray`. For example, `CFArray` provides a set of callbacks, some of which are for implementing custom retain-release behavior. If you specify `NULL` implementations for these callbacks, you can easily get a non-retaining array.

If the behavior you want to add supplements that of the existing class, you could write a category on `NSArray`. Keep in mind, however, that this category will be in effect for all instances of `NSArray` that you use, and this might have unintended consequences. Alternatively, you could use composition to achieve the desired behavior.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSMutableArray](nsmutablearray.md)

- **Conforms To**: [CKRecordValue](../cloudkit/ckrecordvalue-c.protocol.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sequence](../swift/sequence.md)

## Topics

### Creating an Array

- [+ arrayWithObject:](<nsarray/init(object_).md>) — Creates and returns an array containing a given object.
- [+ arrayWithObjects:count:](<nsarray/init(objects_count_)-7dct1.md>) — Creates and returns an array that includes a given number of objects from a given C array.

### Initializing an Array

- [- init](<nsarray/init().md>) — Initializes a newly allocated array.
- [- initWithArray:](<nsarray/init(array_)-o72h.md>) — Initializes a newly allocated array by placing in it the objects contained in a given array.
- [- initWithArray:copyItems:](<nsarray/init(array_copyitems_).md>) — Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [- initWithContentsOfFile:](<nsarray/init(contentsoffile_).md>) — Initializes a newly allocated array with the contents of the file specified by a given path. _(deprecated)_
- [- initWithObjects:count:](<nsarray/init(objects_count_)-5odxv.md>) — Initializes a newly allocated array to include a given number of objects from a given C array.

### Querying an Array

- [- containsObject:](<nsarray/contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the array.
- [count](nsarray/count.md) — The number of objects in the array.
- [firstObject](nsarray/firstobject.md) — The first object in the array.
- [lastObject](nsarray/lastobject.md) — The last object in the array.
- [- objectAtIndex:](<nsarray/object(at_).md>) — Returns the object located at the specified index.
- [- objectAtIndexedSubscript:](<nsarray/subscript(__).md>) — Returns the object at the specified index.
- [- objectsAtIndexes:](<nsarray/objects(at_).md>) — Returns an array containing the objects in the array at the indexes specified by a given index set.
- [- objectEnumerator](<nsarray/objectenumerator().md>) — Returns an enumerator object that lets you access each object in the array.
- [- reverseObjectEnumerator](<nsarray/reverseobjectenumerator().md>) — Returns an enumerator object that lets you access each object in the array, in reverse order.

### Finding Objects in an Array

- [- indexOfObject:](<nsarray/index(of_).md>) — Returns the lowest index whose corresponding array value is equal to a given object.
- [- indexOfObject:inRange:](<nsarray/index(of_in_).md>) — Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [- indexOfObjectIdenticalTo:](<nsarray/indexofobjectidentical(to_).md>) — Returns the lowest index whose corresponding array value is identical to a given object.
- [- indexOfObjectIdenticalTo:inRange:](<nsarray/indexofobjectidentical(to_in_).md>) — Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [- indexOfObjectPassingTest:](<nsarray/indexofobject(passingtest_).md>) — Returns the index of the first object in the array that passes a test in a given block.
- [- indexOfObjectWithOptions:passingTest:](<nsarray/indexofobject(options_passingtest_).md>) — Returns the index of an object in the array that passes a test in a given block for a given set of enumeration options.
- [- indexOfObjectAtIndexes:options:passingTest:](<nsarray/indexofobject(at_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the first object in the array that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsPassingTest:](<nsarray/indexesofobjects(passingtest_).md>) — Returns the indexes of objects in the array that pass a test in a given block.
- [- indexesOfObjectsWithOptions:passingTest:](<nsarray/indexesofobjects(options_passingtest_).md>) — Returns the indexes of objects in the array that pass a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsAtIndexes:options:passingTest:](<nsarray/indexesofobjects(at_options_passingtest_).md>) — Returns the indexes, from a given set of indexes, of objects in the array that pass a test in a given block for a given set of enumeration options.
- [- indexOfObject:inSortedRange:options:usingComparator:](<nsarray/index(of_insortedrange_options_usingcomparator_).md>) — Returns the index, within a specified range, of an object compared with elements in the array using a given `NSComparator` block.

### Sending Messages to Elements

- [- enumerateObjectsUsingBlock:](<nsarray/enumerateobjects(__).md>) — Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object.
- [- enumerateObjectsWithOptions:usingBlock:](<nsarray/enumerateobjects(options_using_).md>) — Executes a given closure or block using each object in the array with the specified options.
- [- enumerateObjectsAtIndexes:options:usingBlock:](<nsarray/enumerateobjects(at_options_using_).md>) — Executes a given block using the objects in the array at the specified indexes.

### Comparing Arrays

- [- firstObjectCommonWithArray:](<nsarray/firstobjectcommon(with_).md>) — Returns the first object contained in the receiving array that’s equal to an object in another given array.
- [- isEqualToArray:](<nsarray/isequal(to_).md>) — Compares the receiving array to another array.

### Deriving New Arrays

- [- arrayByAddingObject:](<nsarray/adding(__).md>) — Returns a new array that is a copy of the receiving array with a given object added to the end.
- [- arrayByAddingObjectsFromArray:](<nsarray/addingobjects(from_).md>) — Returns a new array that is a copy of the receiving array with the objects contained in another array added to the end.
- [- filteredArrayUsingPredicate:](<nsarray/filtered(using_).md>) — Evaluates a given predicate against each object in the receiving array and returns a new array containing the objects for which the predicate returns true.
- [- subarrayWithRange:](<nsarray/subarray(with_).md>) — Returns a new array containing the receiving array’s elements that fall within the limits specified by a given range.

### Sorting

- [sortedArrayHint](nsarray/sortedarrayhint.md) — Analyzes the array and returns a “hint” that speeds the sorting of the array when the hint is supplied to [- sortedArrayUsingFunction:context:hint:](<nsarray/sortedarray(__context_hint_).md>).
- [- sortedArrayUsingFunction:context:](<nsarray/sortedarray(__context_).md>) — Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [- sortedArrayUsingFunction:context:hint:](<nsarray/sortedarray(__context_hint_).md>) — Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [- sortedArrayUsingDescriptors:](<nsarray/sortedarray(using_)-82wi1.md>) — Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.
- [- sortedArrayUsingSelector:](<nsarray/sortedarray(using_)-9nhh9.md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.
- [- sortedArrayUsingComparator:](<nsarray/sortedarray(comparator_).md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [- sortedArrayWithOptions:usingComparator:](<nsarray/sortedarray(options_usingcomparator_).md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [Comparator](comparator.md) — Defines the signature for a block object used for comparison operations.

### Working with String Elements

- [- componentsJoinedByString:](<nsarray/componentsjoined(by_).md>) — Constructs and returns an `NSString` object that is the result of interposing a given separator between the elements of the array.

### Creating a Description

- [description](nsarray/description.md) — A string that represents the contents of the array, formatted as a property list.
- [- descriptionWithLocale:](<nsarray/description(withlocale_).md>) — Returns a string that represents the contents of the array, formatted as a property list.
- [- descriptionWithLocale:indent:](<nsarray/description(withlocale_indent_).md>) — Returns a string that represents the contents of the array, formatted as a property list.

### Storing Arrays

- [- writeToFile:atomically:](<nsarray/write(tofile_atomically_).md>) — Writes the contents of the array to a file at a given path. _(deprecated)_
- [- writeToURL:atomically:](<nsarray/write(to_atomically_).md>) — Writes the contents of the array to the location specified by a given URL. _(deprecated)_

### Collecting Paths

- [- pathsMatchingExtensions:](<nsarray/pathsmatchingextensions(__).md>) — Returns an array containing all the pathname elements in the receiving array that have filename extensions from a given array.

### Key-Value Observing

- [- addObserver:forKeyPath:options:context:](<nsarray/addobserver(__forkeypath_options_context_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:](<nsarray/removeobserver(__forkeypath_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:context:](<nsarray/removeobserver(__forkeypath_context_).md>) — Raises an exception.
- [- removeObserver:fromObjectsAtIndexes:forKeyPath:context:](<nsarray/removeobserver(__fromobjectsat_forkeypath_context_).md>) — Raises an exception.
- [- addObserver:toObjectsAtIndexes:forKeyPath:options:context:](<nsarray/addobserver(__toobjectsat_forkeypath_options_context_).md>) — Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.
- [- removeObserver:fromObjectsAtIndexes:forKeyPath:](<nsarray/removeobserver(__fromobjectsat_forkeypath_).md>) — Removes `anObserver` from all key value observer notifications associated with the specified `keyPath` relative to the array’s objects at `indexes`.

### Key-Value Coding

- [- setValue:forKey:](<nsarray/setvalue(__forkey_).md>) — Invokes [- setValue:forKey:](<nsarray/setvalue(__forkey_).md>) on each of the array’s items using the specified `value` and `key`.
- [- valueForKey:](<nsarray/value(forkey_).md>) — Returns an array containing the results of invoking [- valueForKey:](<nsarray/value(forkey_).md>) using `key` on each of the array’s objects.

### Randomly Shuffling an Array

- [- shuffledArray](<nsarray/shuffled().md>) — Returns a new array that lists this array’s elements in a random order.
- [- shuffledArrayWithRandomSource:](<nsarray/shuffled(using_).md>) — Returns a new array that lists this array’s elements in a random order, using the specified random source.

### Comparing with Another Array

- [NSOrderedCollectionDifference](nsorderedcollectiondifference.md) — An object representing the difference between two ordered collections.
- [NSOrderedCollectionDifferenceCalculationOptions](nsorderedcollectiondifferencecalculationoptions.md) — Constants that specify the options to use when creating an ordered collection difference.

### New Methods

- [- initWithCoder:](<nsarray/init(coder_).md>)

### Constants

- [NSBinarySearchingOptions](nsbinarysearchingoptions.md) — Options for searches and insertions using [- indexOfObject:inSortedRange:options:usingComparator:](<nsarray/index(of_insortedrange_options_usingcomparator_).md>).

### Initializers

- [init(array:)](<nsarray/init(array_)-9rh7.md>) — Initializes a newly allocated array by placing in it the objects contained in a given array.
- [- initWithContentsOfURL:](<nsarray/init(contentsof_).md>) — Initializes a newly allocated array with the contents of the location specified by a given URL. _(deprecated)_
- [- initWithContentsOfURL:error:](<nsarray/init(contentsof_error_).md>)
- [init(objects:)](<nsarray/init(objects_).md>)

### Instance Methods

- [- writeToURL:error:](<nsarray/write(to_).md>)

### Default Implementations

- [ExpressibleByArrayLiteral Implementations](nsarray/expressiblebyarrayliteral-implementations.md)
- [NSArray Implementations](nsarray/nsarray-implementations.md)
- [Sequence Implementations](nsarray/sequence-implementations.md)
