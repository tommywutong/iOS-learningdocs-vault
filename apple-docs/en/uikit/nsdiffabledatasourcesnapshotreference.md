---
title: NSDiffableDataSourceSnapshotReference
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesnapshotreference
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference.json'
content_hash: 'sha256:2d567510113f0daa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDiffableDataSourceSnapshotReference

<sub>Class</sub>

A representation of the state of the data in a view at a specific point in time.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSDiffableDataSourceSnapshotReference
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

```objc
// Create a snapshot.
NSDiffableDataSourceSnapshot<NSNumber *, NSUUID *> *snapshot = [[NSDiffableDataSourceSnapshot alloc] init];

// Populate the snapshot.
[snapshot appendSectionsWithIdentifiers:@[@0]];
[snapshot appendItemsWithIdentifiers:@[[NSUUID UUID], [NSUUID UUID], [NSUUID UUID]]];

// Apply the snapshot.
[self.dataSource applySnapshot:snapshot animatingDifferences:YES];
```

For more information, see the diffable data source types:

- [UICollectionViewDiffableDataSourceReference](uicollectionviewdiffabledatasourcereference.md)
- [UITableViewDiffableDataSourceReference](uitableviewdiffabledatasourcereference.md)
- [NSCollectionViewDiffableDataSource](../appkit/nscollectionviewdiffabledatasource-axww.md)

> [!important] Important
> If you’re working in a Swift codebase, always use [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md) instead.

Avoid using this type in Swift code. Only use this type to bridge from Objective-C code to Swift code by typecasting from a snapshot reference to a snapshot:

```swift
let snapshot = snapshotReference as NSDiffableDataSourceSnapshot<Int, UUID>
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a snapshot

- [- appendSectionsWithIdentifiers:](<nsdiffabledatasourcesnapshotreference/appendsections(withidentifiers_).md>) — Adds the sections with the specified identifiers to the snapshot.
- [- appendItemsWithIdentifiers:intoSectionWithIdentifier:](<nsdiffabledatasourcesnapshotreference/appenditems(withidentifiers_intosectionwithidentifier_).md>) — Adds the items with the specified identifiers to the specified section of the snapshot.
- [- appendItemsWithIdentifiers:](<nsdiffabledatasourcesnapshotreference/appenditems(withidentifiers_).md>) — Adds the items with the specified identifiers to the last section of the snapshot.

### Getting item and section metrics

- [numberOfItems](nsdiffabledatasourcesnapshotreference/numberofitems.md) — The number of items in the snapshot.
- [numberOfSections](nsdiffabledatasourcesnapshotreference/numberofsections.md) — The number of sections in the snapshot.
- [- numberOfItemsInSection:](<nsdiffabledatasourcesnapshotreference/numberofitems(insection_).md>) — Returns the number of items in the specified section of the snapshot.

### Identifying items and sections

- [itemIdentifiers](nsdiffabledatasourcesnapshotreference/itemidentifiers.md) — The identifiers of all of the items in the snapshot.
- [sectionIdentifiers](nsdiffabledatasourcesnapshotreference/sectionidentifiers.md) — The identifiers of all of the sections in the snapshot.
- [- indexOfItemIdentifier:](<nsdiffabledatasourcesnapshotreference/index(ofitemidentifier_).md>) — Returns the index of the item in the snapshot with the specified identifier.
- [- indexOfSectionIdentifier:](<nsdiffabledatasourcesnapshotreference/index(ofsectionidentifier_).md>) — Returns the index of the section of the snapshot with the specified identifier.
- [- itemIdentifiersInSectionWithIdentifier:](<nsdiffabledatasourcesnapshotreference/itemidentifiersinsection(withidentifier_).md>) — Returns the identifiers of all of the items in the specified section of the snapshot.
- [- sectionIdentifierForSectionContainingItemIdentifier:](<nsdiffabledatasourcesnapshotreference/sectionidentifier(forsectioncontainingitemidentifier_).md>) — Returns the identifier of the section containing the specified item in the snapshot.

### Inserting items and sections

- [- insertItemsWithIdentifiers:afterItemWithIdentifier:](<nsdiffabledatasourcesnapshotreference/insertitems(withidentifiers_afteritemwithidentifier_).md>) — Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [- insertItemsWithIdentifiers:beforeItemWithIdentifier:](<nsdiffabledatasourcesnapshotreference/insertitems(withidentifiers_beforeitemwithidentifier_).md>) — Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [- insertSectionsWithIdentifiers:afterSectionWithIdentifier:](<nsdiffabledatasourcesnapshotreference/insertsections(withidentifiers_aftersectionwithidentifier_).md>) — Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
- [- insertSectionsWithIdentifiers:beforeSectionWithIdentifier:](<nsdiffabledatasourcesnapshotreference/insertsections(withidentifiers_beforesectionwithidentifier_).md>) — Inserts the provided sections immediately before the section with the specified identifier in the snapshot.

### Removing items and sections

- [- deleteAllItems](<nsdiffabledatasourcesnapshotreference/deleteallitems().md>) — Deletes all of the items from the snapshot.
- [- deleteItemsWithIdentifiers:](<nsdiffabledatasourcesnapshotreference/deleteitems(withidentifiers_).md>) — Deletes the items with the specified identifiers from the snapshot.
- [- deleteSectionsWithIdentifiers:](<nsdiffabledatasourcesnapshotreference/deletesections(withidentifiers_).md>) — Deletes the sections with the specified identifiers from the snapshot.

### Reordering items and sections

- [- moveItemWithIdentifier:afterItemWithIdentifier:](<nsdiffabledatasourcesnapshotreference/moveitem(withidentifier_afteritemwithidentifier_).md>) — Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [- moveItemWithIdentifier:beforeItemWithIdentifier:](<nsdiffabledatasourcesnapshotreference/moveitem(withidentifier_beforeitemwithidentifier_).md>) — Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [- moveSectionWithIdentifier:afterSectionWithIdentifier:](<nsdiffabledatasourcesnapshotreference/movesection(withidentifier_aftersectionwithidentifier_).md>) — Moves the section from its current position in the snapshot to the position immediately after the specified section.
- [- moveSectionWithIdentifier:beforeSectionWithIdentifier:](<nsdiffabledatasourcesnapshotreference/movesection(withidentifier_beforesectionwithidentifier_).md>) — Moves the section from its current position in the snapshot to the position immediately before the specified section.

### Reloading data

- [- reconfigureItemsWithIdentifiers:](<nsdiffabledatasourcesnapshotreference/reconfigureitems(withidentifiers_).md>) — Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [reconfiguredItemIdentifiers](nsdiffabledatasourcesnapshotreference/reconfigureditemidentifiers.md) — Identifies the items reconfigured by the changes to the snapshot.
- [- reloadItemsWithIdentifiers:](<nsdiffabledatasourcesnapshotreference/reloaditems(withidentifiers_).md>) — Reloads the data within the specified items in the snapshot.
- [reloadedItemIdentifiers](nsdiffabledatasourcesnapshotreference/reloadeditemidentifiers.md) — Identifies the items reloaded by the changes to the snapshot.
- [- reloadSectionsWithIdentifiers:](<nsdiffabledatasourcesnapshotreference/reloadsections(withidentifiers_).md>) — Reloads the data within the specified sections of the snapshot.
- [reloadedSectionIdentifiers](nsdiffabledatasourcesnapshotreference/reloadedsectionidentifiers.md) — Identifies the sections reloaded by the changes to the snapshot.
