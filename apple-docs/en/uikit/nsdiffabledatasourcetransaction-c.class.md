---
title: NSDiffableDataSourceTransaction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcetransaction-c.class
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcetransaction-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcetransaction-c.class.json'
content_hash: 'sha256:544f5b77d2bef032'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDiffableDataSourceTransaction

<sub>Class</sub>

A transaction that describes the changes after reordering the items in the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface NSDiffableDataSourceTransaction : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Accessing a transaction’s information

- [sectionTransactions](nsdiffabledatasourcetransaction-c.class/sectiontransactions.md) — An array of section transactions for the transaction.
- [initialSnapshot](nsdiffabledatasourcetransaction-c.class/initialsnapshot.md) — The snapshot before the transaction occured.
- [finalSnapshot](nsdiffabledatasourcetransaction-c.class/finalsnapshot.md) — The snapshot after the transaction occured.
- [difference](nsdiffabledatasourcetransaction-c.class/difference.md) — A collection of insertions and removals that describe the difference between initial and final snapshots.

## See Also

### Supporting reordering

- [reorderingHandlers](uicollectionviewdiffabledatasourcereference/reorderinghandlers.md) — The diffable data source’s handlers for reordering items.
- [UICollectionViewDiffableDataSourceReorderingHandlers](uicollectionviewdiffabledatasourcereorderinghandlers.md) — Handlers for reordering items.
- [NSDiffableDataSourceSectionTransaction](nsdiffabledatasourcesectiontransaction-c.class.md) — A transaction that describes the changes after reordering the items in a section.
