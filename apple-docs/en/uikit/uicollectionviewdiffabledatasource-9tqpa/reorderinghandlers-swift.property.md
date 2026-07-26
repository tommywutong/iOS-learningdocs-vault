---
title: reorderingHandlers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.property.json'
content_hash: 'sha256:b80916dd9ae622c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md)

# reorderingHandlers

<sub>Instance Property</sub>

The diffable data source’s handlers for reordering items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var reorderingHandlers: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.ReorderingHandlers { get set }
```

## Discussion

Provide reordering handlers to support the reordering of items in your collection view.

The system calls the [didReorder](reorderinghandlers-swift.struct/didreorder.md) handler after a reordering transaction ([NSDiffableDataSourceTransaction](../nsdiffabledatasourcetransaction-swift.struct.md)) occurs, so you can update your data backing store with information about the changes.

```swift
// Allow every item to be reordered
dataSource.reorderingHandlers.canReorderItem = { item in return true }

// Option 1: Update the backing store from a CollectionDifference
dataSource.reorderingHandlers.didReorder = { [weak self] transaction in
    guard let self = self else { return }
    
    if let updatedBackingStore = self.backingStore.applying(transaction.difference) {
        self.backingStore = updatedBackingStore
    }
}

// Option 2: Update the backing store from the final item identifiers
dataSource.reorderingHandlers.didReorder = { [weak self] transaction in
    guard let self = self else { return }
    
    self.backingStore = transaction.finalSnapshot.itemIdentifiers
}
```

## See Also

### Supporting reordering

- [ReorderingHandlers](reorderinghandlers-swift.struct.md) — Handlers for reordering items.
- [NSDiffableDataSourceTransaction](../nsdiffabledatasourcetransaction-swift.struct.md) — A transaction that describes the changes after reordering the items in the view.
- [NSDiffableDataSourceSectionTransaction](../nsdiffabledatasourcesectiontransaction-swift.struct.md) — A transaction that describes the changes after reordering the items in a section.
