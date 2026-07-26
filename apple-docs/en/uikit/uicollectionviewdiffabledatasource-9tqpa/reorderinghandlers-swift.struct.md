---
title: UICollectionViewDiffableDataSource.ReorderingHandlers
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct.json'
content_hash: 'sha256:9b326e24659fcc6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md)

# UICollectionViewDiffableDataSource.ReorderingHandlers

<sub>Structure</sub>

Handlers for reordering items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct ReorderingHandlers
```

## Topics

### Reordering items

- [canReorderItem](reorderinghandlers-swift.struct/canreorderitem.md) — The handler that determines whether you can reorder a particular item.
- [willReorder](reorderinghandlers-swift.struct/willreorder.md) — The handler that prepares the diffable data source for reordering its items.
- [didReorder](reorderinghandlers-swift.struct/didreorder.md) — The handler that processes a reordering transaction.

### Initializers

- [init()](<reorderinghandlers-swift.struct/init().md>) — Creates a reordering handlers structure.

## See Also

### Supporting reordering

- [reorderingHandlers](reorderinghandlers-swift.property.md) — The diffable data source’s handlers for reordering items.
- [NSDiffableDataSourceTransaction](../nsdiffabledatasourcetransaction-swift.struct.md) — A transaction that describes the changes after reordering the items in the view.
- [NSDiffableDataSourceSectionTransaction](../nsdiffabledatasourcesectiontransaction-swift.struct.md) — A transaction that describes the changes after reordering the items in a section.
