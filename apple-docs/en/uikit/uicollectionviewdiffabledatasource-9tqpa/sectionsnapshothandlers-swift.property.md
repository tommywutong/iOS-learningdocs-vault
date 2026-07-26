---
title: sectionSnapshotHandlers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.property.json'
content_hash: 'sha256:cc36c9bf173d5155'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md)

# sectionSnapshotHandlers

<sub>Instance Property</sub>

The diffable data source’s handlers for expanding and collapsing items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var sectionSnapshotHandlers: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SectionSnapshotHandlers<ItemIdentifierType> { get set }
```

## Discussion

Provide section snapshot handlers to support the expanding or collapsing of items in your collection view.

Use the [snapshotForExpandingParent](sectionsnapshothandlers-swift.struct/snapshotforexpandingparent.md) handler to customize the snapshot that returns when a particular parent item is expanded.

```swift
// Allow every item to be collapsed
dataSource.sectionSnapshotHandlers.shouldCollapseItem = { item in return true }

dataSource.sectionSnapshotHandlers.snapshotForExpandingParent = {
    parent, currentChildSnapshot -> NSDiffableDataSourceSectionSnapshot<String> in
    
    // Return child snapshot for the parent, or just currentChildSnapshot
}
```

## See Also

### Supporting expanding and collapsing

- [SectionSnapshotHandlers](sectionsnapshothandlers-swift.struct.md) — Handlers for expanding and collapsing items.
