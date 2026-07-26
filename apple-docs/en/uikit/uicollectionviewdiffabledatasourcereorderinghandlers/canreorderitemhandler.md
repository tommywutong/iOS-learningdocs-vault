---
title: canReorderItemHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasourcereorderinghandlers/canreorderitemhandler
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereorderinghandlers/canreorderitemhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereorderinghandlers/canreorderitemhandler.json'
content_hash: 'sha256:6f7436413f28e6c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSourceReorderingHandlers](../uicollectionviewdiffabledatasourcereorderinghandlers.md)

# canReorderItemHandler

<sub>Instance Property</sub>

The handler that determines whether you can reorder a particular item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) BOOL (^canReorderItemHandler)(ItemType );
```

## See Also

### Reordering items

- [willReorderHandler](willreorderhandler.md) — The handler that prepares the diffable data source for reordering its items.
- [didReorderHandler](didreorderhandler.md) — The handler that processes a reordering transaction.
