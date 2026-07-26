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
doc_path: /documentation/uikit/nsdiffabledatasourcesectiontransaction-swift.struct/initialsnapshot
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectiontransaction-swift.struct/initialsnapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectiontransaction-swift.struct/initialsnapshot.json'
content_hash: 'sha256:4bd2e1203c8da134'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionTransaction](../nsdiffabledatasourcesectiontransaction-swift.struct.md)

# initialSnapshot

<sub>Instance Property</sub>

The section snapshot before the transaction occured.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var initialSnapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType> { get }
```

## See Also

### Accessing a transaction’s information

- [sectionIdentifier](sectionidentifier.md) — The identifier of the section for the transaction.
- [finalSnapshot](finalsnapshot.md) — The section snapshot after the transaction occured.
- [difference](difference.md) — A collection of insertions and removals that describe the difference between initial and final section snapshots.
