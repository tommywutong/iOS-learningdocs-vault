---
title: NSEnumerator
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsenumerator
source_url: 'https://developer.apple.com/documentation/foundation/nsenumerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsenumerator.json'
content_hash: 'sha256:04e5e160ac92de17'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSEnumerator

<sub>Class</sub>

An abstract class whose subclasses enumerate collections of objects, such as arrays and dictionaries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSEnumerator
```

## Overview

All creation methods are defined in the collection classes—such as [NSArray](nsarray.md), [NSSet](nsset.md), and [NSDictionary](nsdictionary.md)—which provide special [NSEnumerator](nsenumerator.md) objects with which to enumerate their contents. For example, `NSArray` has two methods that return an [NSEnumerator](nsenumerator.md) object: [- objectEnumerator](<nsset/objectenumerator().md>) and [- reverseObjectEnumerator](<nsarray/reverseobjectenumerator().md>). `NSDictionary` also has two methods that return an [NSEnumerator](nsenumerator.md) object: [- keyEnumerator](<nsdictionary/keyenumerator().md>) and [- objectEnumerator](<nsdictionary/objectenumerator().md>). These methods let you enumerate the contents of a dictionary by key or by value, respectively.

You send [- nextObject](<nsenumerator/nextobject().md>) repeatedly to a newly created [NSEnumerator](nsenumerator.md) object to have it return the next object in the original collection. When the collection is exhausted, `nil` is returned. You cannot “reset” an enumerator after it has exhausted its collection. To enumerate a collection again, you need a new enumerator.

The enumerator subclasses used by `NSArray`, `NSDictionary`, and `NSSet` retain the collection during enumeration. When the enumeration is exhausted, the collection is released.

> [!note] Note
> In Objective-C, it is not safe to modify a mutable collection while enumerating through it. Some enumerators may currently allow enumeration of a collection that is modified, but this behavior is not guaranteed to be supported in the future.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [DirectoryEnumerator](filemanager/directoryenumerator.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSFastEnumeration](nsfastenumeration.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sequence](../swift/sequence.md)

## Topics

### Getting the Enumerated Objects

- [allObjects](nsenumerator/allobjects.md) — The array of unenumerated objects.
- [- nextObject](<nsenumerator/nextobject().md>) — Returns the next object from the collection being enumerated.

### Default Implementations

- [Sequence Implementations](nsenumerator/sequence-implementations.md)

## See Also

### Iteration

- [NSFastEnumeration](nsfastenumeration.md) — A protocol that objects adopt to support fast enumeration.
- [NSFastEnumerationIterator](nsfastenumerationiterator.md)
- [NSIndexSetIterator](nsindexsetiterator.md) — An iterator suitable for enumerating the elements of an index set.
- [NSEnumerationOptions](nsenumerationoptions.md) — Options for block enumeration operations.
- [NSSortOptions](nssortoptions.md) — Options for block sorting operations.
