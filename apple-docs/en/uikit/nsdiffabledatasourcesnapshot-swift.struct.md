---
title: NSDiffableDataSourceSnapshot
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct.json'
content_hash: 'sha256:9022aaf2c6290101'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDiffableDataSourceSnapshot

<sub>Structure</sub>

A representation of the state of the data in a view at a specific point in time.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@preconcurrency struct NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType> where SectionIdentifierType : Hashable, SectionIdentifierType : Sendable, ItemIdentifierType : Hashable, ItemIdentifierType : Sendable
```

## Overview

Diffable data sources use _snapshots_ to provide data for collection views and table views. You use a snapshot to set up the initial state of the data that a view displays, and you use snapshots to reflect changes to the data that the view displays.

The data in a snapshot is made up of the sections and items you want to display, in the order that you determine. You configure what to display by adding, deleting, or moving the sections and items.

> [!important] Important
> Each of your sections and items must have unique identifiers that conform to the [Hashable](../swift/hashable.md) protocol. Use `struct` or `enum` Swift value types for your identifiers, including built-in types such as `Int`, `String`, or `UUID`. If you use a Swift `class` for your identifiers, your `class` must be a subclass of `NSObject`.

To display data in a view using a snapshot:

1. Create a snapshot and populate it with the state of the data you want to display.
2. Apply the snapshot to reflect the changes in the UI.

You can create and configure a snapshot in one of these ways:

- Create an empty snapshot, then append sections and items to it.
- Get the current snapshot by calling the diffable data source’s [snapshot()](<uicollectionviewdiffabledatasource-9tqpa/snapshot().md>) method, then modify that snapshot to reflect the new state of the data that you want to display.

For example, the following code creates an empty snapshot and populates it with a single section with three items. Then, the code applies the snapshot, animating the UI updates between the previous state and the new state.

```swift
// Create a snapshot.
var snapshot = NSDiffableDataSourceSnapshot<Int, UUID>()        

// Populate the snapshot.
snapshot.appendSections([0])
snapshot.appendItems([UUID(), UUID(), UUID()])

// Apply the snapshot.
dataSource.apply(snapshot, animatingDifferences: true)
```

For more information, see the diffable data source types:

- [UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md)
- [UITableViewDiffableDataSource](uitableviewdiffabledatasource-2euir.md)
- [NSCollectionViewDiffableDataSource](../appkit/nscollectionviewdiffabledatasource-axww.md)

### Bridging

You can bridge from an [NSDiffableDataSourceSnapshotReference](nsdiffabledatasourcesnapshotreference.md) object to this type:

```swift
let snapshot = snapshotReference as NSDiffableDataSourceSnapshot<Int, UUID>
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a snapshot

- [init()](<nsdiffabledatasourcesnapshot-swift.struct/init().md>) — Creates an empty snapshot.
- [appendSections(_:)](<nsdiffabledatasourcesnapshot-swift.struct/appendsections(__).md>) — Adds the sections with the specified identifiers to the snapshot.
- [appendItems(_:toSection:)](<nsdiffabledatasourcesnapshot-swift.struct/appenditems(__tosection_).md>) — Adds the items with the specified identifiers to the specified section of the snapshot.

### Getting item and section metrics

- [numberOfItems](nsdiffabledatasourcesnapshot-swift.struct/numberofitems.md) — The number of items in the snapshot.
- [numberOfSections](nsdiffabledatasourcesnapshot-swift.struct/numberofsections.md) — The number of sections in the snapshot.
- [numberOfItems(inSection:)](<nsdiffabledatasourcesnapshot-swift.struct/numberofitems(insection_).md>) — Returns the number of items in the specified section of the snapshot.

### Identifying items and sections

- [itemIdentifiers](nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers.md) — The identifiers of all of the items in the snapshot.
- [sectionIdentifiers](nsdiffabledatasourcesnapshot-swift.struct/sectionidentifiers.md) — The identifiers of all of the sections in the snapshot.
- [indexOfItem(_:)](<nsdiffabledatasourcesnapshot-swift.struct/indexofitem(__).md>) — Returns the index of the item in the snapshot with the specified identifier.
- [indexOfSection(_:)](<nsdiffabledatasourcesnapshot-swift.struct/indexofsection(__).md>) — Returns the index of the section of the snapshot with the specified identifier.
- [itemIdentifiers(inSection:)](<nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers(insection_).md>) — Returns the identifiers of all of the items in the specified section of the snapshot.
- [sectionIdentifier(containingItem:)](<nsdiffabledatasourcesnapshot-swift.struct/sectionidentifier(containingitem_).md>) — Returns the identifier of the section containing the specified item in the snapshot.

### Inserting items and sections

- [insertItems(_:afterItem:)](<nsdiffabledatasourcesnapshot-swift.struct/insertitems(__afteritem_).md>) — Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [insertItems(_:beforeItem:)](<nsdiffabledatasourcesnapshot-swift.struct/insertitems(__beforeitem_).md>) — Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [insertSections(_:afterSection:)](<nsdiffabledatasourcesnapshot-swift.struct/insertsections(__aftersection_).md>) — Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
- [insertSections(_:beforeSection:)](<nsdiffabledatasourcesnapshot-swift.struct/insertsections(__beforesection_).md>) — Inserts the provided sections immediately before the section with the specified identifier in the snapshot.

### Removing items and sections

- [deleteAllItems()](<nsdiffabledatasourcesnapshot-swift.struct/deleteallitems().md>) — Deletes all of the items from the snapshot.
- [deleteItems(_:)](<nsdiffabledatasourcesnapshot-swift.struct/deleteitems(__).md>) — Deletes the items with the specified identifiers from the snapshot.
- [deleteSections(_:)](<nsdiffabledatasourcesnapshot-swift.struct/deletesections(__).md>) — Deletes the sections with the specified identifiers from the snapshot.

### Reordering items and sections

- [moveItem(_:afterItem:)](<nsdiffabledatasourcesnapshot-swift.struct/moveitem(__afteritem_).md>) — Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [moveItem(_:beforeItem:)](<nsdiffabledatasourcesnapshot-swift.struct/moveitem(__beforeitem_).md>) — Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [moveSection(_:afterSection:)](<nsdiffabledatasourcesnapshot-swift.struct/movesection(__aftersection_).md>) — Moves the section from its current position in the snapshot to the position immediately after the specified section.
- [moveSection(_:beforeSection:)](<nsdiffabledatasourcesnapshot-swift.struct/movesection(__beforesection_).md>) — Moves the section from its current position in the snapshot to the position immediately before the specified section.

### Reloading data

- [reconfigureItems(_:)](<nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(__).md>) — Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [reconfiguredItemIdentifiers](nsdiffabledatasourcesnapshot-swift.struct/reconfigureditemidentifiers.md) — Identifies the items reconfigured by the changes to the snapshot.
- [reloadItems(_:)](<nsdiffabledatasourcesnapshot-swift.struct/reloaditems(__).md>) — Reloads the data within the specified items in the snapshot.
- [reloadedItemIdentifiers](nsdiffabledatasourcesnapshot-swift.struct/reloadeditemidentifiers.md) — Identifies the items reloaded by the changes to the snapshot.
- [reloadSections(_:)](<nsdiffabledatasourcesnapshot-swift.struct/reloadsections(__).md>) — Reloads the data within the specified sections of the snapshot.
- [reloadedSectionIdentifiers](nsdiffabledatasourcesnapshot-swift.struct/reloadedsectionidentifiers.md) — Identifies the sections reloaded by the changes to the snapshot.

### Supporting bridging

- [NSDiffableDataSourceSnapshotReference](nsdiffabledatasourcesnapshotreference.md) — A representation of the state of the data in a view at a specific point in time.

## See Also

### Data

- [Updating collection views using diffable data sources](updating-collection-views-using-diffable-data-sources.md) — Streamline the display and update of data in a collection view using a diffable data source that contains identifiers.
- [Implementing modern collection views](implementing-modern-collection-views.md) — Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [Building high-performance lists and collection views](building-high-performance-lists-and-collection-views.md) — Improve the performance of lists and collections in your app with prefetching and image preparation.
- [UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md) — The object you use to manage data and provide cells for a collection view.
- [UICollectionViewDataSource](uicollectionviewdatasource.md) — The methods adopted by the object you use to manage data and provide cells for a collection view.
- [UICollectionViewDataSourcePrefetching](uicollectionviewdatasourceprefetching.md) — A protocol that provides advance warning of the data requirements for a collection view, allowing the triggering of asynchronous data load operations.
- [NSDiffableDataSourceSectionSnapshot](nsdiffabledatasourcesectionsnapshot-swift.struct.md) — A representation of the state of the data in a layout section at a specific point in time.
- [UIRefreshControl](uirefreshcontrol.md) — A standard control that can initiate the refreshing of a scroll view’s contents.
