---
title: conflictingObjects
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsconstraintconflict/conflictingobjects
source_url: 'https://developer.apple.com/documentation/coredata/nsconstraintconflict/conflictingobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsconstraintconflict/conflictingobjects.json'
content_hash: 'sha256:4ac820715a2f0194'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSConstraintConflict](../nsconstraintconflict.md)

# conflictingObjects

<sub>Instance Property</sub>

The managed objects that are in conflict.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var conflictingObjects: [NSManagedObject] { get }
```

## See Also

### Inspecting a Conflict

- [conflictingSnapshots](conflictingsnapshots.md) — The original property values of objects in violation of the constraint.
- [constraint](constraint.md) — The constraint that has been violated.
- [constraintValues](constraintvalues.md) — The values that the conflicting objects had when the conflict was created.
- [databaseObject](databaseobject.md) — The object whose database row is using constraint values.
- [databaseSnapshot](databasesnapshot.md) — The values currently stored in the database.
