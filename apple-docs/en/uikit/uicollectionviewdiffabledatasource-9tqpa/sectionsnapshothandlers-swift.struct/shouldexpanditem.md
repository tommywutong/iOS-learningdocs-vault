---
title: shouldExpandItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/shouldexpanditem
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/shouldexpanditem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/shouldexpanditem.json'
content_hash: 'sha256:78d2f78003dee233'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionViewDiffableDataSource](../../uicollectionviewdiffabledatasource-9tqpa.md) · [SectionSnapshotHandlers](../sectionsnapshothandlers-swift.struct.md)

# shouldExpandItem

<sub>Instance Property</sub>

The handler that determines whether a particular item is expandable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var shouldExpandItem: ((ItemIdentifierType) -> Bool)? { get set }
```

## See Also

### Expanding and collapsing items

- [shouldCollapseItem](shouldcollapseitem.md) — The handler that determines whether a particular item is collapsable.
- [willCollapseItem](willcollapseitem.md) — The handler that prepares the diffable data source for collapsing an item.
- [willExpandItem](willexpanditem.md) — The handler that prepares the diffable data source for expanding an item.
- [snapshotForExpandingParent](snapshotforexpandingparent.md) — The handler that provides the section snapshot for expanding the parent item.
