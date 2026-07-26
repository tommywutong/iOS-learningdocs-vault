---
title: NSDiffableDataSourceSectionSnapshotReference
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesectionsnapshotreference
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference.json'
content_hash: 'sha256:dd7aedb13278660e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDiffableDataSourceSectionSnapshotReference

<sub>Class</sub>

A representation of the state of the data in a layout section at a specific point in time.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSDiffableDataSourceSectionSnapshotReference
```

## Overview

A section snapshot represents the data for a single section in a collection view. Through a section snapshot, you set up the initial state of the data that displays in an individual section of your view, and later update that data.

You can use section snapshots with or instead of an [NSDiffableDataSourceSnapshotReference](nsdiffabledatasourcesnapshotreference.md), which represents the data in the entire view. Use a section snapshot when you need precise management of the data in a section of your layout, such as when the sections of your layout acquire their data from different sources. You can also use a section snapshot to represent data with a hierarchical structure, such as an outline with expandable items.

The following example creates a section snapshot with one root item that contains three child items:

```objc
for (NSNumber *section in sections) {
    // Create a section snapshot.
    NSDiffableDataSourceSectionSnapshot<NSString *> *sectionSnapshot = [[NSDiffableDataSourceSectionSnapshot alloc] init];
    
    // Populate the section snapshot.
    [sectionSnapshot appendItems: @[@"Food", @"Drinks"]];
    [sectionSnapshot appendItems: @[@"🍏", @"🍓", @"🥐"] intoParentItem: @"Food"];
    
    // Apply the section snapshot.
    [dataSource applySnapshot: sectionSnapshot
                    toSection: section
         animatingDifferences: YES];
}
```

> [!important] Important
> If you’re working in a Swift codebase, always use [NSDiffableDataSourceSectionSnapshot](nsdiffabledatasourcesectionsnapshot-swift.struct.md) instead.

Avoid using this type in Swift code. Only use this type to bridge from Objective-C code to Swift code by typecasting from a section snapshot reference to a section snapshot:

```swift
let sectionSnapshot = sectionSnapshotRef as NSDiffableDataSourceSectionSnapshot<UUID>
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a section snapshot

- [- init](<nsdiffabledatasourcesectionsnapshotreference/init().md>) — Creates an empty section snapshot.
- [- snapshotOfParentItem:](<nsdiffabledatasourcesectionsnapshotreference/ofparentitem(__).md>) — Creates a section snapshot containing the child items of the specified parent item, excluding the parent item.
- [- snapshotOfParentItem:includingParentItem:](<nsdiffabledatasourcesectionsnapshotreference/ofparentitem(__includingparentitem_).md>) — Creates a section snapshot containing the child items of the specified parent item, including the parent item.
- [- appendItems:](<nsdiffabledatasourcesectionsnapshotreference/appenditems(__).md>) — Adds the specified items to the section snapshot.
- [- appendItems:intoParentItem:](<nsdiffabledatasourcesectionsnapshotreference/appenditems(__intoparentitem_).md>) — Adds the specified items as child items of the specified parent item in the section snapshot.

### Accessing items

- [items](nsdiffabledatasourcesectionsnapshotreference/items.md) — The identifiers of all items in the section snapshot.
- [rootItems](nsdiffabledatasourcesectionsnapshotreference/rootitems.md) — The identifiers of the items at the top level of the section snapshot’s hierarchy.
- [visibleItems](nsdiffabledatasourcesectionsnapshotreference/visibleitems.md) — The identifiers of the currently visible items in the section snapshot.

### Getting item metrics

- [- indexOfItem:](<nsdiffabledatasourcesectionsnapshotreference/index(ofitem_).md>) — Finds the index of the specified item in the section snapshot.
- [- levelOfItem:](<nsdiffabledatasourcesectionsnapshotreference/level(ofitem_).md>) — Finds the hierarchical level of the specified item in the section snapshot.
- [- parentOfChildItem:](<nsdiffabledatasourcesectionsnapshotreference/parent(ofchilditem_).md>) — Finds the parent item of the specified item in the section snapshot.
- [- containsItem:](<nsdiffabledatasourcesectionsnapshotreference/containsitem(__).md>) — Indicates whether the section snapshot contains the specified item.
- [- isVisible:](<nsdiffabledatasourcesectionsnapshotreference/isvisible(__).md>) — Indicates whether the specified item is currently visible onscreen.

### Inserting items

- [- insertSnapshot:afterItem:](<nsdiffabledatasourcesectionsnapshotreference/insert(__afteritem_).md>) — Inserts the provided section snapshot immediately after the item with the specified identifier in the section snapshot.
- [- insertItems:afterItem:](<nsdiffabledatasourcesectionsnapshotreference/insertitems(__afteritem_).md>) — Inserts the provided items immediately after the item with the specified identifier in the section snapshot.
- [- insertSnapshot:beforeItem:](<nsdiffabledatasourcesectionsnapshotreference/insert(__beforeitem_).md>) — Inserts the provided section snapshot immediately before the item with the specified identifier in the section snapshot.
- [- insertItems:beforeItem:](<nsdiffabledatasourcesectionsnapshotreference/insertitems(__beforeitem_).md>) — Inserts the provided items immediately before the item with the specified identifier in the section snapshot.

### Removing items

- [- deleteItems:](<nsdiffabledatasourcesectionsnapshotreference/deleteitems(__).md>) — Deletes the items with the specified identifiers, and any of their child items, from the section snapshot.
- [- deleteAllItems](<nsdiffabledatasourcesectionsnapshotreference/deleteallitems().md>) — Deletes all of the items from the section snapshot.

### Replacing items

- [- replaceChildrenOfParentItem:withSnapshot:](<nsdiffabledatasourcesectionsnapshotreference/replacechildren(ofparentitem_with_).md>) — Replaces all child items of the specified parent item with the provided section snapshot.

### Expanding and collapsing items

- [- isExpanded:](<nsdiffabledatasourcesectionsnapshotreference/isexpanded(__).md>) — Indicates whether the item with the specified identifier is in an expanded state.
- [- expandItems:](<nsdiffabledatasourcesectionsnapshotreference/expanditems(__).md>) — Expands the specified items in the section snapshot.
- [- collapseItems:](<nsdiffabledatasourcesectionsnapshotreference/collapseitems(__).md>) — Collapses the specified items in the section snapshot.

### Debugging section snapshots

- [- visualDescription](<nsdiffabledatasourcesectionsnapshotreference/visualdescription().md>) — Returns a string with an ASCII representation of the section snapshot.

### Instance Methods

- [- expandedItems](<nsdiffabledatasourcesectionsnapshotreference/expandeditems().md>) — The identifiers of all expanded items in the section snapshot.
