---
title: NSMergeConflict
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergeconflict
source_url: 'https://developer.apple.com/documentation/coredata/nsmergeconflict'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergeconflict.json'
content_hash: 'sha256:9b377946bb770403'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSMergeConflict

<sub>Class</sub>

An encapsulation of conflicts that occur during an attempt to save changes in a managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMergeConflict
```

## Overview

A conflict can occur in two situations:

- Between the managed object context and its in-memory cached state at the persistent store coordinator layer.
- Between the cached state at the persistent store coordinator layer and the external store (file, database, and so forth). In this case, the merge conflict has a cached snapshot and a persisted snapshot.  The source object is also provided as a convenience, but it is not directly involved in the conflict.

Snapshot dictionaries include values for all attributes and to-one relationships, but not to-many relationships. Relationship values are `NSManagedObjectID` references. To-many relationships must be pulled from the persistent store as needed.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a Merge Conflict

- [- initWithSource:newVersion:oldVersion:cachedSnapshot:persistedSnapshot:](<nsmergeconflict/init(source_newversion_oldversion_cachedsnapshot_persistedsnapshot_).md>) — Initializes a merge conflict.

### Accessing Merge Conflict Details

- [sourceObject](nsmergeconflict/sourceobject.md) — The source object for the conflict.
- [objectSnapshot](nsmergeconflict/objectsnapshot.md) — A dictionary containing the values of the source object.
- [cachedSnapshot](nsmergeconflict/cachedsnapshot.md) — A dictionary containing the values of the source object held in the persistent store coordinator layer.
- [persistedSnapshot](nsmergeconflict/persistedsnapshot.md) — A dictionary containing the values of the source object held in the persistent store.
- [newVersionNumber](nsmergeconflict/newversionnumber.md) — The new version number for the change.
- [oldVersionNumber](nsmergeconflict/oldversionnumber.md) — The old version number for the change.

## See Also

### Conflict Management

- [NSConstraintConflict](nsconstraintconflict.md) — An encapsulation of conflicts that occur during an attempt to save a managed object.
- [NSMergePolicy](nsmergepolicy.md) — A policy object that you use to resolve conflicts between the persistent store and in-memory versions of managed objects.
- [NSQueryGenerationToken](nsquerygenerationtoken.md) — A token that indicates which generation of the persistent store is being accessed.
