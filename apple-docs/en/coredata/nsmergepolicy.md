---
title: NSMergePolicy
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergepolicy
source_url: 'https://developer.apple.com/documentation/coredata/nsmergepolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergepolicy.json'
content_hash: 'sha256:73db175951213461'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSMergePolicy

<sub>Class</sub>

A policy object that you use to resolve conflicts between the persistent store and in-memory versions of managed objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMergePolicy
```

## Overview

A conflict is a mismatch between state held at two different layers in the Core Data stack. A conflict can arise when you save a managed object context and you have stale data at another layer. There are two places in which a conflict may occur:

- Between the managed object context layer and its in-memory cached state at the persistent store coordinator layer.
- Between the cached state at the persistent store coordinator and the external store (file, database, and so forth).

Conflicts are represented by instances of [NSMergeConflict](nsmergeconflict.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting a Merge Policy

- [- initWithMergeType:](<nsmergepolicy/init(merge_).md>) — Returns a merge policy initialized with a given policy type.
- [mergeType](nsmergepolicy/mergetype.md) — The merge type.

### Resolving a Conflict

- [- resolveConflicts:error:](<nsmergepolicy/resolve(mergeconflicts_).md>) — Resolves the conflicts in a given list.
- [- resolveConstraintConflicts:error:](<nsmergepolicy/resolve(constraintconflicts_).md>) — Resolves the conflicts in a given list.
- [- resolveOptimisticLockingVersionConflicts:error:](<nsmergepolicy/resolve(optimisticlockingconflicts_).md>) — Resolves the conflicts in a given list.

### Defining Merge Policies

- [errorMergePolicy](nsmergepolicy/error.md) — The default merge policy for all managed object contexts.
- [mergeByPropertyStoreTrumpMergePolicy](nsmergepolicy/mergebypropertystoretrump.md) — A property-based merge policy that applies external changes.
- [mergeByPropertyObjectTrumpMergePolicy](nsmergepolicy/mergebypropertyobjecttrump.md) — A property-based merge policy that applies in-memory changes.
- [overwriteMergePolicy](nsmergepolicy/overwrite.md) — A merge policy that overwrites the entire stored object.
- [rollbackMergePolicy](nsmergepolicy/rollback.md) — A merge policy that discards unsaved changes.
- [Merge Policies](merge-policies.md) — Define standard ways to handle conflicts during a save operation.

### Initializers

- [init(mergeType:)](<nsmergepolicy/init(mergetype_).md>)

## See Also

### Conflict Management

- [NSConstraintConflict](nsconstraintconflict.md) — An encapsulation of conflicts that occur during an attempt to save a managed object.
- [NSMergeConflict](nsmergeconflict.md) — An encapsulation of conflicts that occur during an attempt to save changes in a managed object context.
- [NSQueryGenerationToken](nsquerygenerationtoken.md) — A token that indicates which generation of the persistent store is being accessed.
