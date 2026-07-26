---
title: NSDiffableDataSourceSectionTransaction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class.json'
content_hash: 'sha256:59384b69c6544764'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDiffableDataSourceSectionTransaction

<sub>Class</sub>

A transaction that describes the changes after reordering the items in a section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface NSDiffableDataSourceSectionTransaction : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Accessing a transaction’s information

- [sectionIdentifier](nsdiffabledatasourcesectiontransaction-c.class/sectionidentifier.md) — The identifier of the section for the transaction.
- [initialSnapshot](nsdiffabledatasourcesectiontransaction-c.class/initialsnapshot.md) — The section snapshot before the transaction occured.
- [finalSnapshot](nsdiffabledatasourcesectiontransaction-c.class/finalsnapshot.md) — The section snapshot after the transaction occured.
- [difference](nsdiffabledatasourcesectiontransaction-c.class/difference.md) — A collection of insertions and removals that describe the difference between initial and final section snapshots.

## See Also

### Supporting reordering

- [reorderingHandlers](uicollectionviewdiffabledatasourcereference/reorderinghandlers.md) — The diffable data source’s handlers for reordering items.
- [UICollectionViewDiffableDataSourceReorderingHandlers](uicollectionviewdiffabledatasourcereorderinghandlers.md) — Handlers for reordering items.
- [NSDiffableDataSourceTransaction](nsdiffabledatasourcetransaction-c.class.md) — A transaction that describes the changes after reordering the items in the view.
