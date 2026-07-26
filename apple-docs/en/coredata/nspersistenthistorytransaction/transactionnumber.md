---
title: transactionNumber
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistorytransaction/transactionnumber
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction/transactionnumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorytransaction/transactionnumber.json'
content_hash: 'sha256:3832fdaa66e80bc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryTransaction](../nspersistenthistorytransaction.md)

# transactionNumber

<sub>Instance Property</sub>

The transaction’s numeric identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transactionNumber: Int64 { get }
```

## See Also

### Inspecting Transaction Details

- [author](author.md) — A granular description of the context that made the persistent history change, if available.
- [bundleID](bundleid.md) — The originating bundle’s identifier.
- [changes](changes.md) — The array of persistent history changes.
- [contextName](contextname.md) — The originating context’s name.
- [processID](processid.md) — The originating process’s identifier.
- [storeID](storeid.md) — The originating store’s identifier.
- [timestamp](timestamp.md) — The date of the persistent history change.
- [token](token.md) — The token that represents this transaction in the persistent history.
