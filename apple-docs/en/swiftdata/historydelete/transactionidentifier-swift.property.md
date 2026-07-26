---
title: transactionIdentifier
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historydelete/transactionidentifier-swift.property
source_url: 'https://developer.apple.com/documentation/swiftdata/historydelete/transactionidentifier-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historydelete/transactionidentifier-swift.property.json'
content_hash: 'sha256:d5b3da1e28aa238e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [HistoryDelete](../historydelete.md)

# transactionIdentifier

<sub>Instance Property</sub>

The delete operation’s transaction identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transactionIdentifier: Self.TransactionIdentifier { get }
```

## See Also

### History deletion properites

- [changeIdentifier](changeidentifier-swift.property.md) — The change identifier of the delete operation.
- [changedPersistentIdentifier](changedpersistentidentifier.md) — The changed persistent identifier of the delete operation.
- [tombstone](tombstone.md) — The value the framework uses to represent information about data the Swift Data previously deleted from a model.
