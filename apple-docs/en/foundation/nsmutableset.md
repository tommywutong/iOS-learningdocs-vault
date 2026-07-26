---
title: NSMutableSet
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutableset
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableset.json'
content_hash: 'sha256:69da5878b5ee78c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMutableSet

<sub>Class</sub>

A dynamic unordered collection of unique objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMutableSet
```

## Overview

You can use this type in Swift instead of a [Set](../swift/set.md) in cases that require reference semantics.

The `NSMutableSet` class declares the programmatic interface to a mutable, unordered collection of distinct objects.

The [NSCountedSet](nscountedset.md) class, which is a concrete subclass of `NSMutableSet`, supports mutable sets that can contain multiple instances of the same element. The [NSSet](nsset.md) class supports creating and managing immutable sets.

NSMutableSet is “toll-free bridged” with its Core Foundation counterpart, [CFMutableSet](../corefoundation/cfmutableset.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

### Subclassing Notes

There should be little need of subclassing. If you need to customize behavior, it is often better to consider composition instead of subclassing.

#### Methods to Override

In a subclass, you must override both of its primitive methods:

- [- addObject:](<nsmutableset/add(__).md>)
- [- removeObject:](<nsmutableset/remove(__).md>)

You must also override the primitive methods of the [NSSet](nsset.md) class.

## Relationships

- **Inherits From**: [NSSet](nsset.md)

- **Inherited By**: [NSCountedSet](nscountedset.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Creating a mutable set

- [- initWithCapacity:](<nsmutableset/init(capacity_).md>) — Returns an initialized mutable set with a given initial capacity.
- [- init](<nsmutableset/init().md>) — Initializes a newly allocated set.

### Adding and removing entries

- [- addObject:](<nsmutableset/add(__).md>) — Adds a given object to the set, if it is not already a member.
- [- filterUsingPredicate:](<nsmutableset/filter(using_).md>) — Evaluates a given predicate against the set’s content and removes from the set those objects for which the predicate returns false.
- [- removeObject:](<nsmutableset/remove(__).md>) — Removes a given object from the set.
- [- removeAllObjects](<nsmutableset/removeallobjects().md>) — Empties the set of all of its members.
- [- addObjectsFromArray:](<nsmutableset/addobjects(from_).md>) — Adds to the set each object contained in a given array that is not already a member.

### Combining and recombining sets

- [- unionSet:](<nsmutableset/union(__).md>) — Adds each object in another given set to the receiving set, if not present.
- [- minusSet:](<nsmutableset/minus(__).md>) — Removes each object in another given set from the receiving set, if present.
- [- intersectSet:](<nsmutableset/intersect(__).md>) — Removes from the receiving set each object that isn’t a member of another given set.
- [- setSet:](<nsmutableset/setset(__).md>) — Empties the receiving set, then adds each object contained in another given set.

### Initializers

- [- initWithCoder:](<nsmutableset/init(coder_).md>)
- [init(objects:count:)](<nsmutableset/init(objects_count_).md>)
