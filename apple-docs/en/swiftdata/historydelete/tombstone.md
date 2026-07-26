---
title: tombstone
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historydelete/tombstone
source_url: 'https://developer.apple.com/documentation/swiftdata/historydelete/tombstone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historydelete/tombstone.json'
content_hash: 'sha256:8669c0603f484856'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [HistoryDelete](../historydelete.md)

# tombstone

<sub>Instance Property</sub>

The value the framework uses to represent information about data the Swift Data previously deleted from a model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tombstone: HistoryTombstone<Self.Model> { get }
```

## See Also

### History deletion properites

- [changeIdentifier](changeidentifier-swift.property.md) — The change identifier of the delete operation.
- [changedPersistentIdentifier](changedpersistentidentifier.md) — The changed persistent identifier of the delete operation.
- [transactionIdentifier](transactionidentifier-swift.property.md) — The delete operation’s transaction identifier.
