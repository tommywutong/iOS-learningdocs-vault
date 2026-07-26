---
title: NSDiffableDataSourceSectionSnapshot
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct.json'
content_hash: 'sha256:0dbc0cc1abe3bfae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDiffableDataSourceSectionSnapshot

<sub>Structure</sub>

A representation of the state of the data in a layout section at a specific point in time.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@preconcurrency struct NSDiffableDataSourceSectionSnapshot<ItemIdentifierType> where ItemIdentifierType : Hashable, ItemIdentifierType : Sendable
```

## Overview

A section snapshot represents the data for a single section in a collection view. Through a section snapshot, you set up the initial state of the data that displays in an individual section of your view, and later update that data.

You can use section snapshots with or instead of an [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md), which represents the data in the entire view. Use a section snapshot when you need precise management of the data in a section of your layout, such as when the sections of your layout acquire their data from different sources. You can also use a section snapshot to represent data with a hierarchical structure, such as an outline with expandable items.

The following example creates a section snapshot with two root items, with one that contains three child items:

```swift
for section in Section.allCases {
    // Create a section snapshot
    var sectionSnapshot = NSDiffableDataSourceSectionSnapshot<String>()
    
    // Populate the section snapshot
    sectionSnapshot.append(["Food", "Drinks"])
    sectionSnapshot.append(["🍏", "🍓", "🥐"], to: "Food")
    
    // Apply the section snapshot
    dataSource.apply(sectionSnapshot,
                     to: section,
                     animatingDifferences: true)
}
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a section snapshot

- [init()](<nsdiffabledatasourcesectionsnapshot-swift.struct/init().md>) — Creates an empty section snapshot.
- [init(_:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/init(__).md>) — Creates a copy of the provided section snapshot.
- [snapshot(of:includingParent:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/snapshot(of_includingparent_).md>) — Creates a section snapshot that contains the child items of the specified parent item, optionally including the parent item.
- [append(_:to:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/append(__to_).md>) — Adds the specified items as child items of the specified parent item in the section snapshot.

### Accessing items

- [items](nsdiffabledatasourcesectionsnapshot-swift.struct/items.md) — The identifiers of all items in the section snapshot.
- [rootItems](nsdiffabledatasourcesectionsnapshot-swift.struct/rootitems.md) — The identifiers of the items at the top level of the section snapshot’s hierarchy.
- [visibleItems](nsdiffabledatasourcesectionsnapshot-swift.struct/visibleitems.md) — The identifiers of the currently visible items in the section snapshot.

### Getting item metrics

- [index(of:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/index(of_).md>) — Finds the index of the specified item in the section snapshot.
- [level(of:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/level(of_).md>) — Finds the hierarchical level of the specified item in the section snapshot.
- [parent(of:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/parent(of_).md>) — Finds the parent item of the specified item in the section snapshot.
- [contains(_:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/contains(__).md>) — Indicates whether the section snapshot contains the specified item.
- [isVisible(_:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/isvisible(__).md>) — Indicates whether the specified item is currently visible onscreen.

### Inserting items

- [insert(_:after:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/insert(__after_)-9v9c7.md>) — Inserts the provided items immediately after the item with the specified identifier in the section snapshot.
- [insert(_:after:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/insert(__after_)-4it9s.md>) — Inserts the provided section snapshot immediately after the item with the specified identifier in the section snapshot.
- [insert(_:before:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/insert(__before_)-5o91y.md>) — Inserts the provided items immediately before the item with the specified identifier in the section snapshot.
- [insert(_:before:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/insert(__before_)-bsrn.md>) — Inserts the provided section snapshot immediately before the item with the specified identifier in the section snapshot.

### Removing items

- [delete(_:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/delete(__).md>) — Deletes the items with the specified identifiers, and any of their child items, from the section snapshot.
- [deleteAll()](<nsdiffabledatasourcesectionsnapshot-swift.struct/deleteall().md>) — Deletes all of the items from the section snapshot.

### Replacing items

- [replace(childrenOf:using:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/replace(childrenof_using_).md>) — Replaces all child items of the specified parent item with the provided section snapshot.

### Expanding and collapsing items

- [isExpanded(_:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/isexpanded(__).md>) — Indicates whether the item with the specified identifier is in an expanded state.
- [expand(_:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/expand(__).md>) — Expands the specified items in the section snapshot.
- [collapse(_:)](<nsdiffabledatasourcesectionsnapshot-swift.struct/collapse(__).md>) — Collapses the specified items in the section snapshot.

### Debugging section snapshots

- [visualDescription()](<nsdiffabledatasourcesectionsnapshot-swift.struct/visualdescription().md>) — Returns a string with an ASCII representation of the section snapshot.

### Supporting bridging

- [NSDiffableDataSourceSectionSnapshotReference](nsdiffabledatasourcesectionsnapshotreference.md) — A representation of the state of the data in a layout section at a specific point in time.

### Instance Properties

- [expandedItems](nsdiffabledatasourcesectionsnapshot-swift.struct/expandeditems.md)

## See Also

### Data

- [Updating collection views using diffable data sources](updating-collection-views-using-diffable-data-sources.md) — Streamline the display and update of data in a collection view using a diffable data source that contains identifiers.
- [Implementing modern collection views](implementing-modern-collection-views.md) — Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [Building high-performance lists and collection views](building-high-performance-lists-and-collection-views.md) — Improve the performance of lists and collections in your app with prefetching and image preparation.
- [UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md) — The object you use to manage data and provide cells for a collection view.
- [UICollectionViewDataSource](uicollectionviewdatasource.md) — The methods adopted by the object you use to manage data and provide cells for a collection view.
- [UICollectionViewDataSourcePrefetching](uicollectionviewdatasourceprefetching.md) — A protocol that provides advance warning of the data requirements for a collection view, allowing the triggering of asynchronous data load operations.
- [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md) — A representation of the state of the data in a view at a specific point in time.
- [UIRefreshControl](uirefreshcontrol.md) — A standard control that can initiate the refreshing of a scroll view’s contents.
