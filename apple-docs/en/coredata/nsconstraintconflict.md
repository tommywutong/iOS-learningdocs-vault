---
title: NSConstraintConflict
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsconstraintconflict
source_url: 'https://developer.apple.com/documentation/coredata/nsconstraintconflict'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsconstraintconflict.json'
content_hash: 'sha256:2b1dbbc5b32ff822'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSConstraintConflict

<sub>Class</sub>

An encapsulation of conflicts that occur during an attempt to save a managed object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSConstraintConflict
```

## Overview

A constraint conflict occurs when your data model is using unique constraints and one or more managed objects are violating that constraint.

When this error occurs, the error instance can be interrogated to determine which instance of [NSManagedObject](nsmanagedobject.md) is violating the constraint and which property on the [NSManagedObject](nsmanagedobject.md) instance is in violation.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a Conflict

- [- initWithConstraint:databaseObject:databaseSnapshot:conflictingObjects:conflictingSnapshots:](<nsconstraintconflict/init(constraint_database_databasesnapshot_conflicting_conflictingsnapshots_).md>) — Initializes a constraint conflict.

### Inspecting a Conflict

- [conflictingObjects](nsconstraintconflict/conflictingobjects.md) — The managed objects that are in conflict.
- [conflictingSnapshots](nsconstraintconflict/conflictingsnapshots.md) — The original property values of objects in violation of the constraint.
- [constraint](nsconstraintconflict/constraint.md) — The constraint that has been violated.
- [constraintValues](nsconstraintconflict/constraintvalues.md) — The values that the conflicting objects had when the conflict was created.
- [databaseObject](nsconstraintconflict/databaseobject.md) — The object whose database row is using constraint values.
- [databaseSnapshot](nsconstraintconflict/databasesnapshot.md) — The values currently stored in the database.

### Initializers

- [init(constraint:databaseObject:databaseSnapshot:conflictingObjects:conflictingSnapshots:)](<nsconstraintconflict/init(constraint_databaseobject_databasesnapshot_conflictingobjects_conflictingsnapshots_).md>)

## See Also

### Conflict Management

- [NSMergeConflict](nsmergeconflict.md) — An encapsulation of conflicts that occur during an attempt to save changes in a managed object context.
- [NSMergePolicy](nsmergepolicy.md) — A policy object that you use to resolve conflicts between the persistent store and in-memory versions of managed objects.
- [NSQueryGenerationToken](nsquerygenerationtoken.md) — A token that indicates which generation of the persistent store is being accessed.
