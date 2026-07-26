---
title: UICollectionViewDiffableDataSourceReference
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasourcereference
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereference.json'
content_hash: 'sha256:9271fb24fa78fbd0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewDiffableDataSourceReference

<sub>Class</sub>

The object you use to manage data and provide cells for a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UICollectionViewDiffableDataSourceReference
```

## Overview

> [!important] Important
> If you’re working in a Swift codebase, always use [UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md) instead.

A _diffable data source_ object is a specialized type of data source that works together with your collection view object. It provides the behavior you need to manage updates to your collection view’s data and UI in a simple, efficient way. It also conforms to the [UICollectionViewDataSource](uicollectionviewdatasource.md) protocol and provides implementations for all of the protocol’s methods.

To fill a collection view with data:

1. Connect a diffable data source to your collection view.
2. Implement a cell provider to configure your collection view’s cells.
3. Generate the current state of the data.
4. Display the data in the UI.

To connect a diffable data source to a collection view, you create the diffable data source using its [- initWithCollectionView:cellProvider:](<uicollectionviewdiffabledatasourcereference/init(collectionview_cellprovider_).md>) initializer, passing in the collection view you want to associate with that data source. You also pass in a cell provider, where you configure each of your cells to determine how to display your data in the UI.

```objc
self.dataSource = [[UICollectionViewDiffableDataSource alloc] initWithCollectionView:self.collectionView cellProvider:^UICollectionViewCell *(UICollectionView *collectionView, NSIndexPath *indexPath, id item) {
    // Configure and return cell.
}];
```

Then, you generate the current state of the data and display the data in the UI by constructing and applying a snapshot. For more information, see [NSDiffableDataSourceSnapshotReference](nsdiffabledatasourcesnapshotreference.md).

> [!important] Important
> Don’t change the [dataSource](uicollectionview/datasource.md) on the collection view after you configure it with a diffable data source. If the collection view needs a new data source after you configure it initially, create and configure a new collection view and diffable data source.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UICollectionViewDataSource](uicollectionviewdatasource.md)

## Topics

### Creating a diffable data source

- [- initWithCollectionView:cellProvider:](<uicollectionviewdiffabledatasourcereference/init(collectionview_cellprovider_).md>) — Creates a diffable data source with the specified cell provider, and connects it to the specified collection view.
- [UICollectionViewDiffableDataSourceReferenceCellProvider](uicollectionviewdiffabledatasourcereferencecellprovider.md) — A closure that configures and returns a cell for a collection view from its diffable data source.

### Creating supplementary views

- [supplementaryViewProvider](uicollectionviewdiffabledatasourcereference/supplementaryviewprovider.md) — The closure that configures and returns the collection view’s supplementary views, such as headers and footers, from the diffable data source.
- [UICollectionViewDiffableDataSourceReferenceSupplementaryViewProvider](uicollectionviewdiffabledatasourcereferencesupplementaryviewprovider.md) — A closure that configures and returns a collection view’s supplementary view, such as a header or footer, from a diffable data source.

### Identifying items

- [- itemIdentifierForIndexPath:](<uicollectionviewdiffabledatasourcereference/itemidentifier(for_).md>) — Returns an identifier for the item at the specified index path in the collection view.
- [- indexPathForItemIdentifier:](<uicollectionviewdiffabledatasourcereference/indexpath(foritemidentifier_).md>) — Returns an index path for the item with the specified identifier in the collection view.

### Identifying sections

- [- sectionIdentifierForIndex:](<uicollectionviewdiffabledatasourcereference/sectionidentifier(for_).md>) — Returns an identifier for the section at the index you specify in the collection view.
- [- indexForSectionIdentifier:](<uicollectionviewdiffabledatasourcereference/index(forsectionidentifier_).md>) — Returns an index for the section with the identifier you specify in the collection view.

### Updating data

- [- snapshot](<uicollectionviewdiffabledatasourcereference/snapshot().md>) — Returns a representation of the current state of the data in the collection view.
- [- applySnapshot:animatingDifferences:](<uicollectionviewdiffabledatasourcereference/applysnapshot(__animatingdifferences_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [- applySnapshot:animatingDifferences:completion:](<uicollectionviewdiffabledatasourcereference/applysnapshot(__animatingdifferences_completion_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [- applySnapshotUsingReloadData:](<uicollectionviewdiffabledatasourcereference/applysnapshot(usingreloaddata_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [- applySnapshotUsingReloadData:completion:](<uicollectionviewdiffabledatasourcereference/applysnapshot(usingreloaddata_completion_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.

### Updating section data

- [- snapshotForSection:](<uicollectionviewdiffabledatasourcereference/snapshot(forsection_).md>) — Returns a representation of the current state of the data in the specified section of the collection view.
- [- applySnapshot:toSection:animatingDifferences:completion:](<uicollectionviewdiffabledatasourcereference/applysnapshot(__tosection_animatingdifferences_completion_).md>) — Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.
- [- applySnapshot:toSection:animatingDifferences:](<uicollectionviewdiffabledatasourcereference/applysnapshot(__tosection_animatingdifferences_).md>) — Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.

### Supporting reordering

- [reorderingHandlers](uicollectionviewdiffabledatasourcereference/reorderinghandlers.md) — The diffable data source’s handlers for reordering items.

### Supporting expanding and collapsing

- [sectionSnapshotHandlers](uicollectionviewdiffabledatasourcereference/sectionsnapshothandlers.md) — The diffable data source’s handlers for expanding and collapsing items.
