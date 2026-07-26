---
title: processID
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistorytransaction/processid
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction/processid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorytransaction/processid.json'
content_hash: 'sha256:5ad31362d8e055b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryTransaction](../nspersistenthistorytransaction.md)

# processID

<sub>Instance Property</sub>

The originating process’s identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var processID: String { get }
```

## See Also

### Inspecting Transaction Details

- [author](author.md) — A granular description of the context that made the persistent history change, if available.
- [bundleID](bundleid.md) — The originating bundle’s identifier.
- [changes](changes.md) — The array of persistent history changes.
- [contextName](contextname.md) — The originating context’s name.
- [storeID](storeid.md) — The originating store’s identifier.
- [timestamp](timestamp.md) — The date of the persistent history change.
- [token](token.md) — The token that represents this transaction in the persistent history.
- [transactionNumber](transactionnumber.md) — The transaction’s numeric identifier.
