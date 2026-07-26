---
title: databaseSnapshot
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsconstraintconflict/databasesnapshot
source_url: 'https://developer.apple.com/documentation/coredata/nsconstraintconflict/databasesnapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsconstraintconflict/databasesnapshot.json'
content_hash: 'sha256:69052d55185ed0fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSConstraintConflict](../nsconstraintconflict.md)

# databaseSnapshot

<sub>Instance Property</sub>

The values currently stored in the database.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var databaseSnapshot: [String : Any]? { get }
```

## See Also

### Inspecting a Conflict

- [conflictingObjects](conflictingobjects.md) — The managed objects that are in conflict.
- [conflictingSnapshots](conflictingsnapshots.md) — The original property values of objects in violation of the constraint.
- [constraint](constraint.md) — The constraint that has been violated.
- [constraintValues](constraintvalues.md) — The values that the conflicting objects had when the conflict was created.
- [databaseObject](databaseobject.md) — The object whose database row is using constraint values.
