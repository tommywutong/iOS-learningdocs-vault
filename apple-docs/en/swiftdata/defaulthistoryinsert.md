---
title: DefaultHistoryInsert
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/defaulthistoryinsert
source_url: 'https://developer.apple.com/documentation/swiftdata/defaulthistoryinsert'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/defaulthistoryinsert.json'
content_hash: 'sha256:c4e31f3bfb297cb0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# DefaultHistoryInsert

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DefaultHistoryInsert<Model> where Model : PersistentModel
```

## Relationships

- **Conforms To**: [HistoryInsert](historyinsert.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<defaulthistoryinsert/==(____).md>)

### Instance Methods

- [hash(into:)](<defaulthistoryinsert/hash(into_).md>)

## See Also

### History life cycle

- [HistoryChange](historychange.md) — Values that describe data history transactions.
- [HistoryDelete](historydelete.md) — An interface that enables a custom data store to delete items from the history of changes to its persisted models.
- [HistoryInsert](historyinsert.md)
- [HistoryToken](historytoken.md)
- [HistoryTransaction](historytransaction.md)
- [HistoryUpdate](historyupdate.md)
- [HistoryTombstone](historytombstone.md)
- [DefaultHistoryUpdate](defaulthistoryupdate.md)
- [DefaultHistoryDelete](defaulthistorydelete.md)
- [DefaultHistoryToken](defaulthistorytoken.md)
- [DefaultHistoryTransaction](defaulthistorytransaction.md)
