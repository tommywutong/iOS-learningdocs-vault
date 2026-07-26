---
title: HistoryChange
framework: SwiftData
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historychange
source_url: 'https://developer.apple.com/documentation/swiftdata/historychange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historychange.json'
content_hash: 'sha256:1775bf448b0a8e85'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# HistoryChange

<sub>Enumeration</sub>

Values that describe data history transactions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum HistoryChange
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Operations

- [HistoryChange.delete(_:)](<historychange/delete(__).md>) — A value that indicates a delete operation.
- [HistoryChange.insert(_:)](<historychange/insert(__).md>) — A value that indicates an insertion operation.
- [HistoryChange.update(_:)](<historychange/update(__).md>) — A value that indicates an update operation.

### Getting information about a change

- [changedPersistentIdentifier](historychange/changedpersistentidentifier.md) — The persistent identifier of the change.

## See Also

### History life cycle

- [HistoryDelete](historydelete.md) — An interface that enables a custom data store to delete items from the history of changes to its persisted models.
- [HistoryInsert](historyinsert.md)
- [HistoryToken](historytoken.md)
- [HistoryTransaction](historytransaction.md)
- [HistoryUpdate](historyupdate.md)
- [HistoryTombstone](historytombstone.md)
- [DefaultHistoryInsert](defaulthistoryinsert.md)
- [DefaultHistoryUpdate](defaulthistoryupdate.md)
- [DefaultHistoryDelete](defaulthistorydelete.md)
- [DefaultHistoryToken](defaulthistorytoken.md)
- [DefaultHistoryTransaction](defaulthistorytransaction.md)
