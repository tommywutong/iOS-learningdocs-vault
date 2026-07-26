---
title: HistoryInsert
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historyinsert
source_url: 'https://developer.apple.com/documentation/swiftdata/historyinsert'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historyinsert.json'
content_hash: 'sha256:3ca855a912d52785'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# HistoryInsert

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol HistoryInsert<Model> : Sendable
```

## Relationships

- **Inherits From**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DefaultHistoryInsert](defaulthistoryinsert.md)

## Topics

### Associated Types

- [ChangeIdentifier](historyinsert/changeidentifier-swift.associatedtype.md)
- [Model](historyinsert/model.md)
- [TransactionIdentifier](historyinsert/transactionidentifier-swift.associatedtype.md)

### Instance Properties

- [changeIdentifier](historyinsert/changeidentifier-swift.property.md)
- [changedPersistentIdentifier](historyinsert/changedpersistentidentifier.md)
- [transactionIdentifier](historyinsert/transactionidentifier-swift.property.md)

## See Also

### History life cycle

- [HistoryChange](historychange.md) — Values that describe data history transactions.
- [HistoryDelete](historydelete.md) — An interface that enables a custom data store to delete items from the history of changes to its persisted models.
- [HistoryToken](historytoken.md)
- [HistoryTransaction](historytransaction.md)
- [HistoryUpdate](historyupdate.md)
- [HistoryTombstone](historytombstone.md)
- [DefaultHistoryInsert](defaulthistoryinsert.md)
- [DefaultHistoryUpdate](defaulthistoryupdate.md)
- [DefaultHistoryDelete](defaulthistorydelete.md)
- [DefaultHistoryToken](defaulthistorytoken.md)
- [DefaultHistoryTransaction](defaulthistorytransaction.md)
