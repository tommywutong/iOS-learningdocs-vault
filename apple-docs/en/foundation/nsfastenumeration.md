---
title: NSFastEnumeration
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfastenumeration
source_url: 'https://developer.apple.com/documentation/foundation/nsfastenumeration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfastenumeration.json'
content_hash: 'sha256:055822828028cbce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFastEnumeration

<sub>Protocol</sub>

A protocol that objects adopt to support fast enumeration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSFastEnumeration
```

## Overview

The abstract class [NSEnumerator](nsenumerator.md) provides a convenience implementation that uses [- nextObject](<nsenumerator/nextobject().md>) to return items one at a time.

## Relationships

- **Conforming Types**: [DirectoryEnumerator](filemanager/directoryenumerator.md), [NSArray](nsarray.md), [NSCountedSet](nscountedset.md), [NSDictionary](nsdictionary.md), [NSEnumerator](nsenumerator.md), [NSHashTable](nshashtable.md), [NSMapTable](nsmaptable.md), [NSMutableArray](nsmutablearray.md), [NSMutableDictionary](nsmutabledictionary.md), [NSMutableOrderedSet](nsmutableorderedset.md), [NSMutableSet](nsmutableset.md), [NSOrderedCollectionDifference](nsorderedcollectiondifference.md), [NSOrderedSet](nsorderedset.md), [NSPointerArray](nspointerarray.md), [NSSet](nsset.md)

## Topics

### Enumeration

- [- countByEnumeratingWithState:objects:count:](<nsfastenumeration/countbyenumerating(with_objects_count_).md>) — Returns by reference a C array of objects over which the sender should iterate, and as the return value the number of objects in the array.

### Constants

- [NSFastEnumerationState](nsfastenumerationstate.md) — This defines the structure used as contextual information in the [NSFastEnumeration](nsfastenumeration.md) protocol.

## See Also

### Iteration

- [NSEnumerator](nsenumerator.md) — An abstract class whose subclasses enumerate collections of objects, such as arrays and dictionaries.
- [NSFastEnumerationIterator](nsfastenumerationiterator.md)
- [NSIndexSetIterator](nsindexsetiterator.md) — An iterator suitable for enumerating the elements of an index set.
- [NSEnumerationOptions](nsenumerationoptions.md) — Options for block enumeration operations.
- [NSSortOptions](nssortoptions.md) — Options for block sorting operations.
