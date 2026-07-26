---
title: changeIdentifier
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historydelete/changeidentifier-swift.property
source_url: 'https://developer.apple.com/documentation/swiftdata/historydelete/changeidentifier-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historydelete/changeidentifier-swift.property.json'
content_hash: 'sha256:3dd57ea7b4c1fa70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [HistoryDelete](../historydelete.md)

# changeIdentifier

<sub>Instance Property</sub>

The change identifier of the delete operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var changeIdentifier: Self.ChangeIdentifier { get }
```

## See Also

### History deletion properites

- [changedPersistentIdentifier](changedpersistentidentifier.md) — The changed persistent identifier of the delete operation.
- [tombstone](tombstone.md) — The value the framework uses to represent information about data the Swift Data previously deleted from a model.
- [transactionIdentifier](transactionidentifier-swift.property.md) — The delete operation’s transaction identifier.
