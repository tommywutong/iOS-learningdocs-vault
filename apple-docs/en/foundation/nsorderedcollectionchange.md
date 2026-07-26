---
title: NSOrderedCollectionChange
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorderedcollectionchange
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectionchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectionchange.json'
content_hash: 'sha256:f48a55f85c73c5f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSOrderedCollectionChange

<sub>Class</sub>

An object that represents an indexed change within an ordered collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSOrderedCollectionChange
```

## Overview

An ordered collection change represents changes by adding, removing, or moving objects within an ordered collection. Changes with an associated index indicate a move within the collection.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Change

- [- initWithObject:type:index:](<nsorderedcollectionchange/init(object_type_index_).md>) — Creates a change object that represents inserting or removing an object from an ordered collection at a specific index.
- [- initWithObject:type:index:associatedIndex:](<nsorderedcollectionchange/init(object_type_index_associatedindex_).md>) — Creates a change object that represents inserting, removing, or moving an object from an ordered collection at a specific index.

### Accessing the Change

- [changeType](nsorderedcollectionchange/changetype.md) — The type of change.
- [index](nsorderedcollectionchange/index.md) — The index location of the change.
- [object](nsorderedcollectionchange/object.md) — An object the change inserts or removes.
- [associatedIndex](nsorderedcollectionchange/associatedindex.md) — When this property is set to a value other than [NSNotFound](nsnotfound-9t5v2.md), the receiver is one half of a move, and this value is the index of the change’s counterpart of the opposite type in the diff.

## See Also

### Accessing Changes

- [hasChanges](nsorderedcollectiondifference/haschanges.md) — A Boolean value that indicates if the difference has changes.
- [insertions](nsorderedcollectiondifference/insertions.md) — A collection of insertion change objects.
- [removals](nsorderedcollectiondifference/removals.md) — A collection of removal change objects.
- [NSCollectionChangeType](nscollectionchangetype.md) — The type of change represented in computing the difference of an ordered collection.
