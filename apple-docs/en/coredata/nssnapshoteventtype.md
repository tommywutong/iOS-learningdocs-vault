---
title: NSSnapshotEventType
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nssnapshoteventtype
source_url: 'https://developer.apple.com/documentation/coredata/nssnapshoteventtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nssnapshoteventtype.json'
content_hash: 'sha256:b69b0f49ad2d77a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSSnapshotEventType

<sub>Structure</sub>

Constants that specify the reason the managed object may need to reinitialize its values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSSnapshotEventType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Event Types

- [NSSnapshotEventUndoInsertion](nssnapshoteventtype/undoinsertion.md) — Specifies a change due to undo from insertion.
- [NSSnapshotEventUndoDeletion](nssnapshoteventtype/undodeletion.md) — Specifies a change due to undo from deletion.
- [NSSnapshotEventUndoUpdate](nssnapshoteventtype/undoupdate.md) — Specifies a change due to a property-level undo.
- [NSSnapshotEventRollback](nssnapshoteventtype/rollback.md) — Specifies a change due to the managed object context being rolled back.
- [NSSnapshotEventRefresh](nssnapshoteventtype/refresh.md) — Specifies a change due to the managed object being refreshed.
- [NSSnapshotEventMergePolicy](nssnapshoteventtype/mergepolicy.md) — Specifies a change due to conflict resolution during a save operation.

### Initializers

- [init(rawValue:)](<nssnapshoteventtype/init(rawvalue_).md>) — Creates a snapshot event using a raw value.
