---
title: NSDiffableDataSourceSectionTransaction
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesectiontransaction-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectiontransaction-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectiontransaction-swift.struct.json'
content_hash: 'sha256:4d6c71c18f5bdf22'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDiffableDataSourceSectionTransaction

<sub>Structure</sub>

A transaction that describes the changes after reordering the items in a section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@preconcurrency struct NSDiffableDataSourceSectionTransaction<SectionIdentifierType, ItemIdentifierType> where SectionIdentifierType : Hashable, SectionIdentifierType : Sendable, ItemIdentifierType : Hashable, ItemIdentifierType : Sendable
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing a transaction’s information

- [sectionIdentifier](nsdiffabledatasourcesectiontransaction-swift.struct/sectionidentifier.md) — The identifier of the section for the transaction.
- [initialSnapshot](nsdiffabledatasourcesectiontransaction-swift.struct/initialsnapshot.md) — The section snapshot before the transaction occured.
- [finalSnapshot](nsdiffabledatasourcesectiontransaction-swift.struct/finalsnapshot.md) — The section snapshot after the transaction occured.
- [difference](nsdiffabledatasourcesectiontransaction-swift.struct/difference.md) — A collection of insertions and removals that describe the difference between initial and final section snapshots.

## See Also

### Supporting reordering

- [reorderingHandlers](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.property.md) — The diffable data source’s handlers for reordering items.
- [ReorderingHandlers](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct.md) — Handlers for reordering items.
- [NSDiffableDataSourceTransaction](nsdiffabledatasourcetransaction-swift.struct.md) — A transaction that describes the changes after reordering the items in the view.
