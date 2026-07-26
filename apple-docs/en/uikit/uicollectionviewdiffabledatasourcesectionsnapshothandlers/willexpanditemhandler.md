---
title: willExpandItemHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers/willexpanditemhandler
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers/willexpanditemhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers/willexpanditemhandler.json'
content_hash: 'sha256:204783d0845d2684'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSourceSectionSnapshotHandlers](../uicollectionviewdiffabledatasourcesectionsnapshothandlers.md)

# willExpandItemHandler

<sub>Instance Property</sub>

The handler that prepares the diffable data source for expanding an item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) void (^willExpandItemHandler)(ItemType );
```

## See Also

### Expanding and collapsing items

- [shouldCollapseItemHandler](shouldcollapseitemhandler.md) — The handler that determines whether a particular item is collapsable.
- [shouldExpandItemHandler](shouldexpanditemhandler.md) — The handler that determines whether a particular item is expandable.
- [willCollapseItemHandler](willcollapseitemhandler.md) — The handler that prepares the diffable data source for collapsing an item.
- [snapshotForExpandingParentItemHandler](snapshotforexpandingparentitemhandler.md) — The handler that provides the section snapshot for expanding the parent item.
