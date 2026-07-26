---
title: NSOrderedCollectionDifference
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorderedcollectiondifference
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectiondifference.json'
content_hash: 'sha256:3d2e915de60fd816'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSOrderedCollectionDifference

<sub>Class</sub>

An object representing the difference between two ordered collections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSOrderedCollectionDifference
```

## Overview

Use [differenceFromArray:](nsarray/differencefromarray_.md) or one of its variations to get an instance of [NSOrderedCollectionDifference](nsorderedcollectiondifference.md), which represents the difference between two ordered collections.

For example, the following sample compares two arrays of strings to create a difference that represents the changes:

```objc
NSArray *original = @[@"Red", @"Green", @"Blue"];
NSArray *modified = @[@"Red", @"Blue", @"Green"];

NSOrderedCollectionDifference *diff = [original differenceFromArray:modified];

// diff.hasChanges == TRUE
// diff.insertions.count == 1
// diff.removals.count == 1

```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSFastEnumeration](nsfastenumeration.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing Changes

- [hasChanges](nsorderedcollectiondifference/haschanges.md) — A Boolean value that indicates if the difference has changes.
- [insertions](nsorderedcollectiondifference/insertions.md) — A collection of insertion change objects.
- [removals](nsorderedcollectiondifference/removals.md) — A collection of removal change objects.
- [NSOrderedCollectionChange](nsorderedcollectionchange.md) — An object that represents an indexed change within an ordered collection.
- [NSCollectionChangeType](nscollectionchangetype.md) — The type of change represented in computing the difference of an ordered collection.

### Inverting a Difference Object

- [- inverseDifference](<nsorderedcollectiondifference/inverse().md>) — Calculate the difference between two objects in the reverse direction of comparison.

### Creating a Collection Difference Object

- [- initWithChanges:](<nsorderedcollectiondifference/init(changes_).md>) — Creates an ordered collection difference using an array of ordered collection changes.
- [- initWithInsertIndexes:insertedObjects:removeIndexes:removedObjects:](<nsorderedcollectiondifference/init(insert_insertedobjects_remove_removedobjects_).md>) — Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices.
- [- initWithInsertIndexes:insertedObjects:removeIndexes:removedObjects:additionalChanges:](<nsorderedcollectiondifference/init(insert_insertedobjects_remove_removedobjects_additionalchanges_).md>) — Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices, in addition to an array of ordered collection changes.

### Updating Changes from a Difference Object

- [- differenceByTransformingChangesWithBlock:](<nsorderedcollectiondifference/transformingchanges(__).md>) — Create a new ordered collection difference by mapping over this difference’s members, processing the change objects with the block provided.

### Initializers

- [init(insertIndexes:insertedObjects:removeIndexes:removedObjects:)](<nsorderedcollectiondifference/init(insertindexes_insertedobjects_removeindexes_removedobjects_).md>)
- [init(insertIndexes:insertedObjects:removeIndexes:removedObjects:additionalChanges:)](<nsorderedcollectiondifference/init(insertindexes_insertedobjects_removeindexes_removedobjects_additionalchanges_).md>)

## See Also

### Comparing with Another Array

- [NSOrderedCollectionDifferenceCalculationOptions](nsorderedcollectiondifferencecalculationoptions.md) — Constants that specify the options to use when creating an ordered collection difference.
