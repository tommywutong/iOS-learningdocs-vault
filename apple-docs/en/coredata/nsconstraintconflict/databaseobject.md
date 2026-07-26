---
title: databaseObject
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsconstraintconflict/databaseobject
source_url: 'https://developer.apple.com/documentation/coredata/nsconstraintconflict/databaseobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsconstraintconflict/databaseobject.json'
content_hash: 'sha256:fa30b839a4e1667a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSConstraintConflict](../nsconstraintconflict.md)

# databaseObject

<sub>Instance Property</sub>

The object whose database row is using constraint values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var databaseObject: NSManagedObject? { get }
```

## See Also

### Inspecting a Conflict

- [conflictingObjects](conflictingobjects.md) — The managed objects that are in conflict.
- [conflictingSnapshots](conflictingsnapshots.md) — The original property values of objects in violation of the constraint.
- [constraint](constraint.md) — The constraint that has been violated.
- [constraintValues](constraintvalues.md) — The values that the conflicting objects had when the conflict was created.
- [databaseSnapshot](databasesnapshot.md) — The values currently stored in the database.
