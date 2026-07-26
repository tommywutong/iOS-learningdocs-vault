---
title: HistoryTransaction
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historytransaction
source_url: 'https://developer.apple.com/documentation/swiftdata/historytransaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historytransaction.json'
content_hash: 'sha256:b32935c2805d6f91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# HistoryTransaction

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol HistoryTransaction : Hashable, Identifiable, Sendable
```

## Relationships

- **Inherits From**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Identifiable](../swift/identifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DefaultHistoryTransaction](defaulthistorytransaction.md)

## Topics

### Associated Types

- [TokenType](historytransaction/tokentype.md)
- [TransactionIdentifier](historytransaction/transactionidentifier-swift.associatedtype.md)

### Instance Properties

- [author](historytransaction/author.md)
- [changes](historytransaction/changes.md)
- [storeIdentifier](historytransaction/storeidentifier.md)
- [timestamp](historytransaction/timestamp.md)
- [token](historytransaction/token.md)
- [transactionIdentifier](historytransaction/transactionidentifier-swift.property.md)

## See Also

### History life cycle

- [HistoryChange](historychange.md) — Values that describe data history transactions.
- [HistoryDelete](historydelete.md) — An interface that enables a custom data store to delete items from the history of changes to its persisted models.
- [HistoryInsert](historyinsert.md)
- [HistoryToken](historytoken.md)
- [HistoryUpdate](historyupdate.md)
- [HistoryTombstone](historytombstone.md)
- [DefaultHistoryInsert](defaulthistoryinsert.md)
- [DefaultHistoryUpdate](defaulthistoryupdate.md)
- [DefaultHistoryDelete](defaulthistorydelete.md)
- [DefaultHistoryToken](defaulthistorytoken.md)
- [DefaultHistoryTransaction](defaulthistorytransaction.md)
