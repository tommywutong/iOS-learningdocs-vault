---
title: rollback
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nssnapshoteventtype/rollback
source_url: 'https://developer.apple.com/documentation/coredata/nssnapshoteventtype/rollback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nssnapshoteventtype/rollback.json'
content_hash: 'sha256:27ca83535d466d35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSSnapshotEventType](../nssnapshoteventtype.md)

# rollback

<sub>Type Property</sub>

Specifies a change due to the managed object context being rolled back.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var rollback: NSSnapshotEventType { get }
```

## See Also

### Event Types

- [NSSnapshotEventUndoInsertion](undoinsertion.md) — Specifies a change due to undo from insertion.
- [NSSnapshotEventUndoDeletion](undodeletion.md) — Specifies a change due to undo from deletion.
- [NSSnapshotEventUndoUpdate](undoupdate.md) — Specifies a change due to a property-level undo.
- [NSSnapshotEventRefresh](refresh.md) — Specifies a change due to the managed object being refreshed.
- [NSSnapshotEventMergePolicy](mergepolicy.md) — Specifies a change due to conflict resolution during a save operation.
