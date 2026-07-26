---
title: DefaultHistoryUpdate
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/defaulthistoryupdate
source_url: 'https://developer.apple.com/documentation/swiftdata/defaulthistoryupdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/defaulthistoryupdate.json'
content_hash: 'sha256:560002c42ddba6ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# DefaultHistoryUpdate

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DefaultHistoryUpdate<Model> where Model : PersistentModel
```

## Relationships

- **Conforms To**: [HistoryUpdate](historyupdate.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<defaulthistoryupdate/==(____).md>)

### Instance Methods

- [hash(into:)](<defaulthistoryupdate/hash(into_).md>)

### Type Aliases

- [PropertyUpdate](defaulthistoryupdate/propertyupdate.md)

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
- [DefaultHistoryDelete](defaulthistorydelete.md)
- [DefaultHistoryToken](defaulthistorytoken.md)
- [DefaultHistoryTransaction](defaulthistorytransaction.md)
