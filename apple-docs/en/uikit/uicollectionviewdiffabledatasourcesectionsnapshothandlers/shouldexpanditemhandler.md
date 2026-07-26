---
title: shouldExpandItemHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers/shouldexpanditemhandler
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers/shouldexpanditemhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers/shouldexpanditemhandler.json'
content_hash: 'sha256:639008ec4bf7be12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSourceSectionSnapshotHandlers](../uicollectionviewdiffabledatasourcesectionsnapshothandlers.md)

# shouldExpandItemHandler

<sub>Instance Property</sub>

The handler that determines whether a particular item is expandable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) BOOL (^shouldExpandItemHandler)(ItemType );
```

## See Also

### Expanding and collapsing items

- [shouldCollapseItemHandler](shouldcollapseitemhandler.md) — The handler that determines whether a particular item is collapsable.
- [willCollapseItemHandler](willcollapseitemhandler.md) — The handler that prepares the diffable data source for collapsing an item.
- [willExpandItemHandler](willexpanditemhandler.md) — The handler that prepares the diffable data source for expanding an item.
- [snapshotForExpandingParentItemHandler](snapshotforexpandingparentitemhandler.md) — The handler that provides the section snapshot for expanding the parent item.
