---
title: changedPersistentIdentifier
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historydelete/changedpersistentidentifier
source_url: 'https://developer.apple.com/documentation/swiftdata/historydelete/changedpersistentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historydelete/changedpersistentidentifier.json'
content_hash: 'sha256:815ef0e03b03283e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [HistoryDelete](../historydelete.md)

# changedPersistentIdentifier

<sub>Instance Property</sub>

The changed persistent identifier of the delete operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var changedPersistentIdentifier: PersistentIdentifier { get }
```

## See Also

### History deletion properites

- [changeIdentifier](changeidentifier-swift.property.md) — The change identifier of the delete operation.
- [tombstone](tombstone.md) — The value the framework uses to represent information about data the Swift Data previously deleted from a model.
- [transactionIdentifier](transactionidentifier-swift.property.md) — The delete operation’s transaction identifier.
