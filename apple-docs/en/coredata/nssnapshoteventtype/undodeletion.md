---
title: undoDeletion
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nssnapshoteventtype/undodeletion
source_url: 'https://developer.apple.com/documentation/coredata/nssnapshoteventtype/undodeletion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nssnapshoteventtype/undodeletion.json'
content_hash: 'sha256:71843b80732daa95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSSnapshotEventType](../nssnapshoteventtype.md)

# undoDeletion

<sub>Type Property</sub>

Specifies a change due to undo from deletion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var undoDeletion: NSSnapshotEventType { get }
```

## See Also

### Event Types

- [NSSnapshotEventUndoInsertion](undoinsertion.md) — Specifies a change due to undo from insertion.
- [NSSnapshotEventUndoUpdate](undoupdate.md) — Specifies a change due to a property-level undo.
- [NSSnapshotEventRollback](rollback.md) — Specifies a change due to the managed object context being rolled back.
- [NSSnapshotEventRefresh](refresh.md) — Specifies a change due to the managed object being refreshed.
- [NSSnapshotEventMergePolicy](mergepolicy.md) — Specifies a change due to conflict resolution during a save operation.
