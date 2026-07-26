---
title: DefaultHistoryDelete
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/defaulthistorydelete
source_url: 'https://developer.apple.com/documentation/swiftdata/defaulthistorydelete'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/defaulthistorydelete.json'
content_hash: 'sha256:64ca9f1d1e5eb8d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# DefaultHistoryDelete

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DefaultHistoryDelete<Model> where Model : PersistentModel
```

## Relationships

- **Conforms To**: [HistoryDelete](historydelete.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<defaulthistorydelete/==(____).md>)

### Instance Methods

- [hash(into:)](<defaulthistorydelete/hash(into_).md>)

## See Also

### History life cycle

- [HistoryChange](historychange.md) — Values that describe data history transactions.
- [HistoryDelete](historydelete.md) — An interface that enables a custom data store to delete items from the history of changes to its persisted models.
- [HistoryInsert](historyinsert.md)
- [HistoryToken](historytoken.md)
- [HistoryTransaction](historytransaction.md)
- [HistoryUpdate](historyupdate.md)
- [HistoryTombstone](historytombstone.md)
- [DefaultHistoryInsert](defaulthistoryinsert.md)
- [DefaultHistoryUpdate](defaulthistoryupdate.md)
- [DefaultHistoryToken](defaulthistorytoken.md)
- [DefaultHistoryTransaction](defaulthistorytransaction.md)
