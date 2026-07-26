---
title: willReorderHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasourcereorderinghandlers/willreorderhandler
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereorderinghandlers/willreorderhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereorderinghandlers/willreorderhandler.json'
content_hash: 'sha256:c224a4645f935c56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSourceReorderingHandlers](../uicollectionviewdiffabledatasourcereorderinghandlers.md)

# willReorderHandler

<sub>Instance Property</sub>

The handler that prepares the diffable data source for reordering its items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) void (^willReorderHandler)(NSDiffableDataSourceTransaction<id,id> *);
```

## See Also

### Reordering items

- [canReorderItemHandler](canreorderitemhandler.md) — The handler that determines whether you can reorder a particular item.
- [didReorderHandler](didreorderhandler.md) — The handler that processes a reordering transaction.
