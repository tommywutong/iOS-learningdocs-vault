---
title: shouldCollapseItemHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers/shouldcollapseitemhandler
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers/shouldcollapseitemhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers/shouldcollapseitemhandler.json'
content_hash: 'sha256:09ba8687697328a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSourceSectionSnapshotHandlers](../uicollectionviewdiffabledatasourcesectionsnapshothandlers.md)

# shouldCollapseItemHandler

<sub>Instance Property</sub>

The handler that determines whether a particular item is collapsable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) BOOL (^shouldCollapseItemHandler)(ItemType );
```

## See Also

### Expanding and collapsing items

- [shouldExpandItemHandler](shouldexpanditemhandler.md) — The handler that determines whether a particular item is expandable.
- [willCollapseItemHandler](willcollapseitemhandler.md) — The handler that prepares the diffable data source for collapsing an item.
- [willExpandItemHandler](willexpanditemhandler.md) — The handler that prepares the diffable data source for expanding an item.
- [snapshotForExpandingParentItemHandler](snapshotforexpandingparentitemhandler.md) — The handler that provides the section snapshot for expanding the parent item.
