---
title: UICollectionViewDiffableDataSourceReorderingHandlers
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasourcereorderinghandlers
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereorderinghandlers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereorderinghandlers.json'
content_hash: 'sha256:b18e24d61725fab4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewDiffableDataSourceReorderingHandlers

<sub>Class</sub>

Handlers for reordering items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UICollectionViewDiffableDataSourceReorderingHandlers : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md)

## Topics

### Reordering items

- [canReorderItemHandler](uicollectionviewdiffabledatasourcereorderinghandlers/canreorderitemhandler.md) — The handler that determines whether you can reorder a particular item.
- [willReorderHandler](uicollectionviewdiffabledatasourcereorderinghandlers/willreorderhandler.md) — The handler that prepares the diffable data source for reordering its items.
- [didReorderHandler](uicollectionviewdiffabledatasourcereorderinghandlers/didreorderhandler.md) — The handler that processes a reordering transaction.

## See Also

### Supporting reordering

- [reorderingHandlers](uicollectionviewdiffabledatasourcereference/reorderinghandlers.md) — The diffable data source’s handlers for reordering items.
- [NSDiffableDataSourceTransaction](nsdiffabledatasourcetransaction-c.class.md) — A transaction that describes the changes after reordering the items in the view.
- [NSDiffableDataSourceSectionTransaction](nsdiffabledatasourcesectiontransaction-c.class.md) — A transaction that describes the changes after reordering the items in a section.
