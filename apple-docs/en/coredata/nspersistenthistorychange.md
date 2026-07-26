---
title: NSPersistentHistoryChange
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistorychange
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychange.json'
content_hash: 'sha256:230b77243077aaba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentHistoryChange

<sub>Class</sub>

A change representing the insertion, update, or deletion of a managed object in the persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPersistentHistoryChange
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting Change Metadata

- [fetchRequest](nspersistenthistorychange/fetchrequest.md) — A fetch request that has the persistent history change as the entity.
- [entityDescription](nspersistenthistorychange/entitydescription.md) — The entity description of the persistent history change entity.
- [+ entityDescriptionWithContext:](<nspersistenthistorychange/entitydescription(with_).md>) — Requests an entity description for the managed object type affected by the change using the provided context.

### Inspecting Change Details

- [changeID](nspersistenthistorychange/changeid.md) — The change’s numeric identifier.
- [changeType](nspersistenthistorychange/changetype.md) — The type of change to the managed object in the persistent store.
- [NSPersistentHistoryChangeType](nspersistenthistorychangetype.md) — The types of changes to managed objects reflected in persistent history.
- [changedObjectID](nspersistenthistorychange/changedobjectid.md) — The identifier of the managed object that changed. (swift) Declaration: @property(readonly, copy) NSManagedObjectID *changedObjectID; (objc) Availability: iOS: 11.0 — iPadOS: 11.0 — Mac Catalyst: 13.1 — macOS: 10.13 — tvOS: 11.0 — visionOS: 1.0 — watchOS: 4.0 (objc,swift) }
- [tombstone](nspersistenthistorychange/tombstone.md) — A dictionary of attributes marked for preservation after deletion, and their values when deleted.
- [transaction](nspersistenthistorychange/transaction.md) — The persistent history transaction containing this change.
- [updatedProperties](nspersistenthistorychange/updatedproperties.md) — The set of properties that were updated on the managed object.

## See Also

### Reading History

- [NSPersistentHistoryTransaction](nspersistenthistorytransaction.md) — A set of changes in the persistent history based on a context save or batch operation.
