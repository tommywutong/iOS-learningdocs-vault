---
title: sectionTransactions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcetransaction-swift.struct/sectiontransactions
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcetransaction-swift.struct/sectiontransactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcetransaction-swift.struct/sectiontransactions.json'
content_hash: 'sha256:edff3576f9cea08c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceTransaction](../nsdiffabledatasourcetransaction-swift.struct.md)

# sectionTransactions

<sub>Instance Property</sub>

An array of section transactions for the transaction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sectionTransactions: [NSDiffableDataSourceSectionTransaction<SectionIdentifierType, ItemIdentifierType>] { get }
```

## See Also

### Accessing a transaction’s information

- [initialSnapshot](initialsnapshot.md) — The snapshot before the transaction occured.
- [finalSnapshot](finalsnapshot.md) — The snapshot after the transaction occured.
- [difference](difference.md) — A collection of insertions and removals that describe the difference between initial and final snapshots.
