---
title: canReorderItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/canreorderitem
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/canreorderitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/canreorderitem.json'
content_hash: 'sha256:0a19e3fa3c21be64'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionViewDiffableDataSource](../../uicollectionviewdiffabledatasource-9tqpa.md) · [ReorderingHandlers](../reorderinghandlers-swift.struct.md)

# canReorderItem

<sub>Instance Property</sub>

The handler that determines whether you can reorder a particular item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var canReorderItem: ((ItemIdentifierType) -> Bool)? { get set }
```

## See Also

### Reordering items

- [willReorder](willreorder.md) — The handler that prepares the diffable data source for reordering its items.
- [didReorder](didreorder.md) — The handler that processes a reordering transaction.
