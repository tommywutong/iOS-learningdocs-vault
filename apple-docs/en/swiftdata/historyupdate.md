---
title: HistoryUpdate
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historyupdate
source_url: 'https://developer.apple.com/documentation/swiftdata/historyupdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historyupdate.json'
content_hash: 'sha256:3cb5a0df4bd54c68'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# HistoryUpdate

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol HistoryUpdate<Model> : Sendable
```

## Relationships

- **Inherits From**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DefaultHistoryUpdate](defaulthistoryupdate.md)

## Topics

### Associated Types

- [ChangeIdentifier](historyupdate/changeidentifier-swift.associatedtype.md)
- [Model](historyupdate/model.md)
- [TransactionIdentifier](historyupdate/transactionidentifier-swift.associatedtype.md)

### Instance Properties

- [changeIdentifier](historyupdate/changeidentifier-swift.property.md)
- [changedPersistentIdentifier](historyupdate/changedpersistentidentifier.md)
- [transactionIdentifier](historyupdate/transactionidentifier-swift.property.md)
- [updatedAttributes](historyupdate/updatedattributes.md)

### Type Aliases

- [PropertyUpdate](historyupdate/propertyupdate.md)

## See Also

### History life cycle

- [HistoryChange](historychange.md) — Values that describe data history transactions.
- [HistoryDelete](historydelete.md) — An interface that enables a custom data store to delete items from the history of changes to its persisted models.
- [HistoryInsert](historyinsert.md)
- [HistoryToken](historytoken.md)
- [HistoryTransaction](historytransaction.md)
- [HistoryTombstone](historytombstone.md)
- [DefaultHistoryInsert](defaulthistoryinsert.md)
- [DefaultHistoryUpdate](defaulthistoryupdate.md)
- [DefaultHistoryDelete](defaulthistorydelete.md)
- [DefaultHistoryToken](defaulthistorytoken.md)
- [DefaultHistoryTransaction](defaulthistorytransaction.md)
