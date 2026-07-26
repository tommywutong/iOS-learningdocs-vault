---
title: NSCountedSet
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscountedset
source_url: 'https://developer.apple.com/documentation/foundation/nscountedset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscountedset.json'
content_hash: 'sha256:015e174b63643af8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCountedSet

<sub>Class</sub>

A mutable, unordered collection of distinct objects that may appear more than once in the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSCountedSet
```

## Overview

Each distinct object inserted into an [NSCountedSet](nscountedset.md) object has a counter associated with it. [NSCountedSet](nscountedset.md) keeps track of the number of times objects are inserted and requires that objects be removed the same number of times. Thus, there is only one instance of an object in an [NSSet](nsset.md) object even if the object has been added to the set multiple times. The [count](nsset/count.md) method defined by the superclass [NSSet](nsset.md) has special significance; it returns the number of distinct objects, not the total number of times objects are represented in the set. The [NSSet](nsset.md) and [NSMutableSet](nsmutableset.md) classes are provided for static and dynamic sets, respectively, whose elements are distinct.

While [NSCountedSet](nscountedset.md) and [CFBag](../corefoundation/cfbag.md) are not toll-free bridged, they provide similar functionality. For more information about `CFBag`, see the [CFBag](../corefoundation/cfbag.md).

### Subclassing Notes

Because [NSCountedSet](nscountedset.md) is not a class cluster, it does not have primitive methods that provide the basis for its implementation. In general, there should be little need for subclassing.

#### Methods to Override

If you subclass [NSCountedSet](nscountedset.md), you must override any method of which you want to change the behavior.

If you change the primitive behavior of an [NSCountedSet](nscountedset.md), for instance if you change how objects are stored, you must override all of the affected methods. These include:

- [- addObject:](<nscountedset/add(__).md>)
- [- removeObject:](<nscountedset/remove(__).md>)
- [- objectEnumerator](<nscountedset/objectenumerator().md>)
- [- countForObject:](<nscountedset/count(for_).md>)

If you change the primitive behavior, you must also override the primitive methods of [NSSet](nsset.md) and [NSMutableSet](nsmutableset.md).

## Relationships

- **Inherits From**: [NSMutableSet](nsmutableset.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Initializing a Counted Set

- [- initWithArray:](<nscountedset/init(array_).md>) — Returns a counted set object initialized with the contents of a given array.
- [- initWithSet:](<nscountedset/init(set_).md>) — Returns a counted set object initialized with the contents of a given set.
- [- initWithCapacity:](<nscountedset/init(capacity_).md>) — Returns a counted set object initialized with enough memory to hold a given number of objects.

### Adding and Removing Entries

- [- addObject:](<nscountedset/add(__).md>) — Adds a given object to the set.
- [- removeObject:](<nscountedset/remove(__).md>) — Removes a given object from the set.

### Examining a Counted Set

- [- countForObject:](<nscountedset/count(for_).md>) — Returns the count associated with a given object in the set.
- [- objectEnumerator](<nscountedset/objectenumerator().md>) — Returns an enumerator object that lets you access each object in the set once, independent of its count.

## See Also

### Specialized Sets

- [NSOrderedSet](nsorderedset.md) — A static, ordered collection of unique objects.
- [NSMutableOrderedSet](nsmutableorderedset.md) — A dynamic, ordered collection of unique objects.
