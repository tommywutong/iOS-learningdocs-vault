---
title: UICollectionViewDiffableDataSource.SectionSnapshotHandlers
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct.json'
content_hash: 'sha256:9549c2035a269174'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md)

# UICollectionViewDiffableDataSource.SectionSnapshotHandlers

<sub>Structure</sub>

Handlers for expanding and collapsing items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@preconcurrency struct SectionSnapshotHandlers<ItemIdentifierType> where ItemIdentifierType : Hashable, ItemIdentifierType : Sendable
```

## Topics

### Expanding and collapsing items

- [shouldCollapseItem](sectionsnapshothandlers-swift.struct/shouldcollapseitem.md) — The handler that determines whether a particular item is collapsable.
- [shouldExpandItem](sectionsnapshothandlers-swift.struct/shouldexpanditem.md) — The handler that determines whether a particular item is expandable.
- [willCollapseItem](sectionsnapshothandlers-swift.struct/willcollapseitem.md) — The handler that prepares the diffable data source for collapsing an item.
- [willExpandItem](sectionsnapshothandlers-swift.struct/willexpanditem.md) — The handler that prepares the diffable data source for expanding an item.
- [snapshotForExpandingParent](sectionsnapshothandlers-swift.struct/snapshotforexpandingparent.md) — The handler that provides the section snapshot for expanding the parent item.

### Initializers

- [init()](<sectionsnapshothandlers-swift.struct/init().md>) — Creates a section snapshot handlers structure.

## See Also

### Supporting expanding and collapsing

- [sectionSnapshotHandlers](sectionsnapshothandlers-swift.property.md) — The diffable data source’s handlers for expanding and collapsing items.
