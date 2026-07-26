---
title: HistoryToken
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historytoken
source_url: 'https://developer.apple.com/documentation/swiftdata/historytoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historytoken.json'
content_hash: 'sha256:a41a7d068431eaf2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# HistoryToken

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol HistoryToken : Comparable, Decodable, Encodable, Hashable, Identifiable, Sendable
```

## Relationships

- **Inherits From**: [Comparable](../swift/comparable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Identifiable](../swift/identifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DefaultHistoryToken](defaulthistorytoken.md)

## Topics

### Associated Types

- [TokenType](historytoken/tokentype.md)

### Instance Properties

- [tokenValue](historytoken/tokenvalue.md)

## See Also

### History life cycle

- [HistoryChange](historychange.md) — Values that describe data history transactions.
- [HistoryDelete](historydelete.md) — An interface that enables a custom data store to delete items from the history of changes to its persisted models.
- [HistoryInsert](historyinsert.md)
- [HistoryTransaction](historytransaction.md)
- [HistoryUpdate](historyupdate.md)
- [HistoryTombstone](historytombstone.md)
- [DefaultHistoryInsert](defaulthistoryinsert.md)
- [DefaultHistoryUpdate](defaulthistoryupdate.md)
- [DefaultHistoryDelete](defaulthistorydelete.md)
- [DefaultHistoryToken](defaulthistorytoken.md)
- [DefaultHistoryTransaction](defaulthistorytransaction.md)
