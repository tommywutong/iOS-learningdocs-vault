---
title: willReorder
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/willreorder
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/willreorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/willreorder.json'
content_hash: 'sha256:ed78379550add2ef'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionViewDiffableDataSource](../../uicollectionviewdiffabledatasource-9tqpa.md) · [ReorderingHandlers](../reorderinghandlers-swift.struct.md)

# willReorder

<sub>Instance Property</sub>

The handler that prepares the diffable data source for reordering its items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var willReorder: ((NSDiffableDataSourceTransaction<SectionIdentifierType, ItemIdentifierType>) -> Void)? { get set }
```

## See Also

### Reordering items

- [canReorderItem](canreorderitem.md) — The handler that determines whether you can reorder a particular item.
- [didReorder](didreorder.md) — The handler that processes a reordering transaction.
