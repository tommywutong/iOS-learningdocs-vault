---
title: UICollectionViewDiffableDataSourceSectionSnapshotHandlers
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers.json'
content_hash: 'sha256:1d4a508600a11b09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewDiffableDataSourceSectionSnapshotHandlers

<sub>Class</sub>

Handlers for expanding and collapsing items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UICollectionViewDiffableDataSourceSectionSnapshotHandlers : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md)

## Topics

### Expanding and collapsing items

- [shouldCollapseItemHandler](uicollectionviewdiffabledatasourcesectionsnapshothandlers/shouldcollapseitemhandler.md) — The handler that determines whether a particular item is collapsable.
- [shouldExpandItemHandler](uicollectionviewdiffabledatasourcesectionsnapshothandlers/shouldexpanditemhandler.md) — The handler that determines whether a particular item is expandable.
- [willCollapseItemHandler](uicollectionviewdiffabledatasourcesectionsnapshothandlers/willcollapseitemhandler.md) — The handler that prepares the diffable data source for collapsing an item.
- [willExpandItemHandler](uicollectionviewdiffabledatasourcesectionsnapshothandlers/willexpanditemhandler.md) — The handler that prepares the diffable data source for expanding an item.
- [snapshotForExpandingParentItemHandler](uicollectionviewdiffabledatasourcesectionsnapshothandlers/snapshotforexpandingparentitemhandler.md) — The handler that provides the section snapshot for expanding the parent item.

## See Also

### Supporting expanding and collapsing

- [sectionSnapshotHandlers](uicollectionviewdiffabledatasourcereference/sectionsnapshothandlers.md) — The diffable data source’s handlers for expanding and collapsing items.
