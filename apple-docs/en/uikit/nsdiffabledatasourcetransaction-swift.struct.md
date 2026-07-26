---
title: NSDiffableDataSourceTransaction
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcetransaction-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcetransaction-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcetransaction-swift.struct.json'
content_hash: 'sha256:146f6b187bc60b31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDiffableDataSourceTransaction

<sub>Structure</sub>

A transaction that describes the changes after reordering the items in the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@preconcurrency struct NSDiffableDataSourceTransaction<SectionIdentifierType, ItemIdentifierType> where SectionIdentifierType : Hashable, SectionIdentifierType : Sendable, ItemIdentifierType : Hashable, ItemIdentifierType : Sendable
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing a transaction’s information

- [sectionTransactions](nsdiffabledatasourcetransaction-swift.struct/sectiontransactions.md) — An array of section transactions for the transaction.
- [initialSnapshot](nsdiffabledatasourcetransaction-swift.struct/initialsnapshot.md) — The snapshot before the transaction occured.
- [finalSnapshot](nsdiffabledatasourcetransaction-swift.struct/finalsnapshot.md) — The snapshot after the transaction occured.
- [difference](nsdiffabledatasourcetransaction-swift.struct/difference.md) — A collection of insertions and removals that describe the difference between initial and final snapshots.

## See Also

### Supporting reordering

- [reorderingHandlers](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.property.md) — The diffable data source’s handlers for reordering items.
- [ReorderingHandlers](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct.md) — Handlers for reordering items.
- [NSDiffableDataSourceSectionTransaction](nsdiffabledatasourcesectiontransaction-swift.struct.md) — A transaction that describes the changes after reordering the items in a section.
