---
title: UITableViewDiffableDataSourceReference
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdiffabledatasourcereference
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdiffabledatasourcereference.json'
content_hash: 'sha256:2274c26f4f93f2b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewDiffableDataSourceReference

<sub>Class</sub>

The object you use to manage data and provide cells for a table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITableViewDiffableDataSourceReference
```

## Overview

> [!important] Important
> If you’re working in a Swift codebase, always use [UITableViewDiffableDataSource](uitableviewdiffabledatasource-2euir.md) instead.

A _diffable data source_ object is a specialized type of data source that works together with your table view object. It provides the behavior you need to manage updates to your table view’s data and UI in a simple, efficient way. It also conforms to the [UITableViewDataSource](uitableviewdatasource.md) protocol and provides implementations for all of the protocol’s methods.

To fill a table view with data:

1. Connect a diffable data source to your table view.
2. Implement a cell provider to configure your table view’s cells.
3. Generate the current state of the data.
4. Display the data in the UI.

To connect a diffable data source to a table view, you create the diffable data source using its [- initWithTableView:cellProvider:](<uitableviewdiffabledatasourcereference/init(tableview_cellprovider_).md>) initializer, passing in the table view you want to associate with that data source. You also pass in a cell provider, where you configure each of your cells to determine how to display your data in the UI.

```swift
self.dataSource = [[UITableViewDiffableDataSource alloc] initWithTableView:self.tableView cellProvider:^UITableViewCell *(UITableView *tableView, NSIndexPath *indexPath, id itemIdentifier) {
    // configure and return cell
}];
```

Then, you generate the current state of the data and display the data in the UI by constructing and applying a snapshot. For more information, see [NSDiffableDataSourceSnapshotReference](nsdiffabledatasourcesnapshotreference.md).

> [!important] Important
> Do not change the [dataSource](uitableview/datasource.md) on the table view after you configure it with a diffable data source. If the table view needs a new data source after you configure it initially, create and configure a new table view and diffable data source.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UITableViewDataSource](uitableviewdatasource.md)

## Topics

### Creating a diffable data source

- [- initWithTableView:cellProvider:](<uitableviewdiffabledatasourcereference/init(tableview_cellprovider_).md>) — Creates a diffable data source with the specified cell provider, and connects it to the specified table view.
- [UITableViewDiffableDataSourceReferenceCellProvider](uitableviewdiffabledatasourcereferencecellprovider.md) — A closure that configures and returns a cell for a table view from its diffable data source.

### Identifying items

- [- itemIdentifierForIndexPath:](<uitableviewdiffabledatasourcereference/itemidentifier(for_).md>) — Returns an identifier for the item at the specified index path in the table view.
- [- indexPathForItemIdentifier:](<uitableviewdiffabledatasourcereference/indexpath(foritemidentifier_).md>) — Returns an index path for the item with the specified identifier in the table view.

### Identifying sections

- [- sectionIdentifierForIndex:](<uitableviewdiffabledatasourcereference/sectionidentifier(for_).md>) — Returns an identifier for the section at the index you specify in the table view.
- [- indexForSectionIdentifier:](<uitableviewdiffabledatasourcereference/index(forsectionidentifier_).md>) — Returns an index for the section with the identifier you specify in the table view.

### Updating data

- [- snapshot](<uitableviewdiffabledatasourcereference/snapshot().md>) — Returns a representation of the current state of the data in the table view.
- [- applySnapshot:animatingDifferences:](<uitableviewdiffabledatasourcereference/applysnapshot(__animatingdifferences_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [- applySnapshot:animatingDifferences:completion:](<uitableviewdiffabledatasourcereference/applysnapshot(__animatingdifferences_completion_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [- applySnapshotUsingReloadData:](<uitableviewdiffabledatasourcereference/applysnapshot(usingreloaddata_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [- applySnapshotUsingReloadData:completion:](<uitableviewdiffabledatasourcereference/applysnapshot(usingreloaddata_completion_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.
- [defaultRowAnimation](uitableviewdiffabledatasourcereference/defaultrowanimation.md) — The default type of animation to use when inserting or deleting rows.
