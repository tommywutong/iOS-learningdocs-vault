---
title: finalSnapshot
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesectiontransaction-swift.struct/finalsnapshot
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectiontransaction-swift.struct/finalsnapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectiontransaction-swift.struct/finalsnapshot.json'
content_hash: 'sha256:56e90c158f8299dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionTransaction](../nsdiffabledatasourcesectiontransaction-swift.struct.md)

# finalSnapshot

<sub>Instance Property</sub>

The section snapshot after the transaction occured.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var finalSnapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType> { get }
```

## See Also

### Accessing a transaction’s information

- [sectionIdentifier](sectionidentifier.md) — The identifier of the section for the transaction.
- [initialSnapshot](initialsnapshot.md) — The section snapshot before the transaction occured.
- [difference](difference.md) — A collection of insertions and removals that describe the difference between initial and final section snapshots.
