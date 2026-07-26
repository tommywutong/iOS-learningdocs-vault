---
title: willCollapseItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/willcollapseitem
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/willcollapseitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/willcollapseitem.json'
content_hash: 'sha256:c9aee070e08211f0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionViewDiffableDataSource](../../uicollectionviewdiffabledatasource-9tqpa.md) · [SectionSnapshotHandlers](../sectionsnapshothandlers-swift.struct.md)

# willCollapseItem

<sub>Instance Property</sub>

The handler that prepares the diffable data source for collapsing an item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var willCollapseItem: ((ItemIdentifierType) -> Void)? { get set }
```

## See Also

### Expanding and collapsing items

- [shouldCollapseItem](shouldcollapseitem.md) — The handler that determines whether a particular item is collapsable.
- [shouldExpandItem](shouldexpanditem.md) — The handler that determines whether a particular item is expandable.
- [willExpandItem](willexpanditem.md) — The handler that prepares the diffable data source for expanding an item.
- [snapshotForExpandingParent](snapshotforexpandingparent.md) — The handler that provides the section snapshot for expanding the parent item.
