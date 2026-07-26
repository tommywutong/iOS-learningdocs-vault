---
title: NSPersistentHistoryTransaction
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistorytransaction
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorytransaction.json'
content_hash: 'sha256:f32a44b1b62b9fdd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentHistoryTransaction

<sub>Class</sub>

A set of changes in the persistent history based on a context save or batch operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPersistentHistoryTransaction
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Requesting Notifications

- [- objectIDNotification](<nspersistenthistorytransaction/objectidnotification().md>) — Obtains a notification for use in merging the transaction’s changes into a managed object context.

### Customizing History Fetch Requests

- [fetchRequest](nspersistenthistorytransaction/fetchrequest.md) — A fetch request that has the persistent history transaction as the entity.
- [entityDescription](nspersistenthistorytransaction/entitydescription.md) — The entity description of the persistent history transaction entity.
- [+ entityDescriptionWithContext:](<nspersistenthistorytransaction/entitydescription(with_).md>) — Requests an entity description using the provided context for the managed object type affected by the transaction.

### Inspecting Transaction Details

- [author](nspersistenthistorytransaction/author.md) — A granular description of the context that made the persistent history change, if available.
- [bundleID](nspersistenthistorytransaction/bundleid.md) — The originating bundle’s identifier.
- [changes](nspersistenthistorytransaction/changes.md) — The array of persistent history changes.
- [contextName](nspersistenthistorytransaction/contextname.md) — The originating context’s name.
- [processID](nspersistenthistorytransaction/processid.md) — The originating process’s identifier.
- [storeID](nspersistenthistorytransaction/storeid.md) — The originating store’s identifier.
- [timestamp](nspersistenthistorytransaction/timestamp.md) — The date of the persistent history change.
- [token](nspersistenthistorytransaction/token.md) — The token that represents this transaction in the persistent history.
- [transactionNumber](nspersistenthistorytransaction/transactionnumber.md) — The transaction’s numeric identifier.

## See Also

### Reading History

- [NSPersistentHistoryChange](nspersistenthistorychange.md) — A change representing the insertion, update, or deletion of a managed object in the persistent store.
