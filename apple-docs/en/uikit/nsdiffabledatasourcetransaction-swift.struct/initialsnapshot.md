---
title: initialSnapshot
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcetransaction-swift.struct/initialsnapshot
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcetransaction-swift.struct/initialsnapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcetransaction-swift.struct/initialsnapshot.json'
content_hash: 'sha256:4f883f599b373142'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceTransaction](../nsdiffabledatasourcetransaction-swift.struct.md)

# initialSnapshot

<sub>Instance Property</sub>

The snapshot before the transaction occured.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var initialSnapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType> { get }
```

## See Also

### Accessing a transaction’s information

- [sectionTransactions](sectiontransactions.md) — An array of section transactions for the transaction.
- [finalSnapshot](finalsnapshot.md) — The snapshot after the transaction occured.
- [difference](difference.md) — A collection of insertions and removals that describe the difference between initial and final snapshots.
