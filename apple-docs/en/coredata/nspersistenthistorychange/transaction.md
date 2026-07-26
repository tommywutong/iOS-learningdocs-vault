---
title: transaction
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistorychange/transaction
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychange/transaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychange/transaction.json'
content_hash: 'sha256:929078b9847b3e40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryChange](../nspersistenthistorychange.md)

# transaction

<sub>Instance Property</sub>

The persistent history transaction containing this change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transaction: NSPersistentHistoryTransaction? { get }
```

## See Also

### Inspecting Change Details

- [changeID](changeid.md) — The change’s numeric identifier.
- [changeType](changetype.md) — The type of change to the managed object in the persistent store.
- [NSPersistentHistoryChangeType](../nspersistenthistorychangetype.md) — The types of changes to managed objects reflected in persistent history.
- [changedObjectID](changedobjectid.md) — The identifier of the managed object that changed. (swift) Declaration: @property(readonly, copy) NSManagedObjectID *changedObjectID; (objc) Availability: iOS: 11.0 — iPadOS: 11.0 — Mac Catalyst: 13.1 — macOS: 10.13 — tvOS: 11.0 — visionOS: 1.0 — watchOS: 4.0 (objc,swift) }
- [tombstone](tombstone.md) — A dictionary of attributes marked for preservation after deletion, and their values when deleted.
- [updatedProperties](updatedproperties.md) — The set of properties that were updated on the managed object.
