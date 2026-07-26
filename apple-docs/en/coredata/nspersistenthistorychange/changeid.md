---
title: changeID
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistorychange/changeid
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychange/changeid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychange/changeid.json'
content_hash: 'sha256:f417a575c2d37d04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryChange](../nspersistenthistorychange.md)

# changeID

<sub>Instance Property</sub>

The change’s numeric identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var changeID: Int64 { get }
```

## See Also

### Inspecting Change Details

- [changeType](changetype.md) — The type of change to the managed object in the persistent store.
- [NSPersistentHistoryChangeType](../nspersistenthistorychangetype.md) — The types of changes to managed objects reflected in persistent history.
- [changedObjectID](changedobjectid.md) — The identifier of the managed object that changed. (swift) Declaration: @property(readonly, copy) NSManagedObjectID *changedObjectID; (objc) Availability: iOS: 11.0 — iPadOS: 11.0 — Mac Catalyst: 13.1 — macOS: 10.13 — tvOS: 11.0 — visionOS: 1.0 — watchOS: 4.0 (objc,swift) }
- [tombstone](tombstone.md) — A dictionary of attributes marked for preservation after deletion, and their values when deleted.
- [transaction](transaction.md) — The persistent history transaction containing this change.
- [updatedProperties](updatedproperties.md) — The set of properties that were updated on the managed object.
