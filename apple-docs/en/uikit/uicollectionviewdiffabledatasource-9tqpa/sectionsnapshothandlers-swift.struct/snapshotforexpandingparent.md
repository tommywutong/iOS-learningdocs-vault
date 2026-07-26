---
title: snapshotForExpandingParent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/snapshotforexpandingparent
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/snapshotforexpandingparent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/snapshotforexpandingparent.json'
content_hash: 'sha256:54f1890b0849fac7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionViewDiffableDataSource](../../uicollectionviewdiffabledatasource-9tqpa.md) · [SectionSnapshotHandlers](../sectionsnapshothandlers-swift.struct.md)

# snapshotForExpandingParent

<sub>Instance Property</sub>

The handler that provides the section snapshot for expanding the parent item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var snapshotForExpandingParent: ((ItemIdentifierType, NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)? { get set }
```

## Discussion

Use the [snapshotForExpandingParent](snapshotforexpandingparent.md) handler to customize the snapshot that returns when a particular parent item is expanded.

```swift
// Allow every item to be collapsed
dataSource.sectionSnapshotHandlers.shouldCollapseItem = { item in return true }

dataSource.sectionSnapshotHandlers.snapshotForExpandingParent = {
    parent, existingSnapshot -> NSDiffableDataSourceSectionSnapshot<String> in
    
    // Return child snapshot for the parent, or just existingSnapshot
}
```

## See Also

### Expanding and collapsing items

- [shouldCollapseItem](shouldcollapseitem.md) — The handler that determines whether a particular item is collapsable.
- [shouldExpandItem](shouldexpanditem.md) — The handler that determines whether a particular item is expandable.
- [willCollapseItem](willcollapseitem.md) — The handler that prepares the diffable data source for collapsing an item.
- [willExpandItem](willexpanditem.md) — The handler that prepares the diffable data source for expanding an item.
