---
title: 'init(object:type:index:associatedIndex:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedcollectionchange/init(object:type:index:associatedindex:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectionchange/init(object:type:index:associatedindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectionchange/init%28object%3Atype%3Aindex%3Aassociatedindex%3A%29.json'
content_hash: 'sha256:93b637de7548baad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedCollectionChange](../nsorderedcollectionchange.md)

# init(object:type:index:associatedIndex:)

<sub>Initializer</sub>

Creates a change object that represents inserting, removing, or moving an object from an ordered collection at a specific index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(object anObject: Any?, type: NSCollectionChangeType, index: Int, associatedIndex: Int)
```

## Parameters

- `anObject` — An optional object the change will remove or insert.

- `type` — The type of change.

- `index` — The index location within an ordered collection where the change applies.

- `associatedIndex` — The index of the change’s counterpart of the opposite type in the diff.

## Discussion

Pairs of changes with opposite types that refer to each other represent the index location of their counterpart with the [associatedIndex](associatedindex.md) property. Initializing an [NSOrderedCollectionDifference](../nsorderedcollectiondifference.md) with broken associations (or associations that aren’t reflexive) generates an exception. The following example creates a diff where the object `@”Red”` moves from index `8` to index `3`:

```objc
NSOrderedCollectionDifference *diff = [[NSOrderedCollectionDifference alloc] initWithChanges:@[
    [NSOrderedCollectionChange changeWithObject:@"Red" type:NSCollectionChangeRemove index:8 associatedIndex:3],
    [NSOrderedCollectionChange changeWithObject:@"Red" type:NSCollectionChangeInsert index:3 associatedIndex:8]
]];
```

A move pair can have a different `object` in its removal and insertion changes, which can imply that the change represents moving and changing or replacing an element. Diffs that [controller(_:didChangeContentWith:)](<../../coredata/nsfetchedresultscontrollerdelegate/controller(__didchangecontentwith_)-5ullb.md>) passes to delegates of [NSFetchedResultsController](../../coredata/nsfetchedresultscontroller.md) communicate that an object changed even when its position in the results is unaffected.

> [!note] Note
> Don’t ignore a move when the indexes of its changes are the same. The calculated difference from `@[@”A”, @”B”, @”C”]` to `@[@”C”, @”B”]` may legitimately produce a diff where the change removes the object at index 0 and the object at index 1 moves to index 1. Ignoring the move produces the incorrect result `@[@”B”, @”C”]`.

## See Also

### Creating a Change

- [- initWithObject:type:index:](<init(object_type_index_).md>) — Creates a change object that represents inserting or removing an object from an ordered collection at a specific index.
