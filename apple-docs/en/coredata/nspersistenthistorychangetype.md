---
title: NSPersistentHistoryChangeType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistorychangetype
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychangetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychangetype.json'
content_hash: 'sha256:fad9da2c493b3e91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentHistoryChangeType

<sub>Enumeration</sub>

The types of changes to managed objects reflected in persistent history.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSPersistentHistoryChangeType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Change Types

- [NSPersistentHistoryChangeTypeDelete](nspersistenthistorychangetype/delete.md) — The deletion of a managed object from the persistent store.
- [NSPersistentHistoryChangeTypeInsert](nspersistenthistorychangetype/insert.md) — The insertion of a managed object into the persistent store.
- [NSPersistentHistoryChangeTypeUpdate](nspersistenthistorychangetype/update.md) — An update to a managed object’s properties in the persistent store.

### Initializers

- [init(rawValue:)](<nspersistenthistorychangetype/init(rawvalue_).md>)

## See Also

### Inspecting Change Details

- [changeID](nspersistenthistorychange/changeid.md) — The change’s numeric identifier.
- [changeType](nspersistenthistorychange/changetype.md) — The type of change to the managed object in the persistent store.
- [changedObjectID](nspersistenthistorychange/changedobjectid.md) — The identifier of the managed object that changed. (swift) Declaration: @property(readonly, copy) NSManagedObjectID *changedObjectID; (objc) Availability: iOS: 11.0 — iPadOS: 11.0 — Mac Catalyst: 13.1 — macOS: 10.13 — tvOS: 11.0 — visionOS: 1.0 — watchOS: 4.0 (objc,swift) }
- [tombstone](nspersistenthistorychange/tombstone.md) — A dictionary of attributes marked for preservation after deletion, and their values when deleted.
- [transaction](nspersistenthistorychange/transaction.md) — The persistent history transaction containing this change.
- [updatedProperties](nspersistenthistorychange/updatedproperties.md) — The set of properties that were updated on the managed object.
