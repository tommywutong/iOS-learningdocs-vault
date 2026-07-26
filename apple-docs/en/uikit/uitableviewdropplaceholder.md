---
title: UITableViewDropPlaceholder
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdropplaceholder
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropplaceholder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropplaceholder.json'
content_hash: 'sha256:059bdb3d3ee8566c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewDropPlaceholder

<sub>Class</sub>

A placeholder cell that supports customizing the drop preview parameters.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UITableViewDropPlaceholder
```

## Overview

When you want to insert a placeholder cell into your table, create a [UITableViewDropPlaceholder](uitableviewdropplaceholder.md) object and pass it to the [- dropItem:toPlaceholder:](<uitableviewdropcoordinator/drop(__to_)-3znax.md>) method of your [UITableViewDropCoordinator](uitableviewdropcoordinator.md). You use a placeholder cell to display a temporary interface while you load the cell’s contents asynchronously. For example, your placeholder cell might display a progress indicator or a message that the cell content isn’t yet available. The placeholder object contains the reuse identifier of the temporary cell you want to display in your table. It can also include a custom preview to use during the drop.

You must register the cells you use with your placeholders in advance. In your storyboard file, add a table view cell object to your table, configure its appearance, set its class to [UITableViewCell](uitableviewcell.md) (or an appropriate subclass), and assign a reuse identifier to it. When you create your [UITableViewDropPlaceholder](uitableviewdropplaceholder.md) object, pass the cell’s reuse identifier to [- initWithInsertionIndexPath:reuseIdentifier:rowHeight:](<uitableviewplaceholder/init(insertionindexpath_reuseidentifier_rowheight_).md>). The table view uses the information in your placeholder object to insert the cell into the table.

Set the [cellUpdateHandler](uitableviewplaceholder/cellupdatehandler.md) to a block of code that configures the cell as a placeholder for the incoming data.

For more information, see [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md).

> [!important] Important
> Placeholder cells are meant to be a temporary part of your table view. Always replace them with actual cells as soon as possible, or cancel the drop to remove them from the table. Use the methods of a [UITableViewDropPlaceholderContext](uitableviewdropplaceholdercontext.md) object to remove placeholders from your table.

## Relationships

- **Inherits From**: [UITableViewPlaceholder](uitableviewplaceholder.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing preview parameters

- [previewParametersProvider](uitableviewdropplaceholder/previewparametersprovider.md) — The handler block that provides the preview parameters for the specified cell.

## See Also

### Placeholder cells

- [UITableViewDropPlaceholderContext](uitableviewdropplaceholdercontext.md) — An object for tracking a placeholder cell that you added to your table during a drop operation.
- [UITableViewPlaceholder](uitableviewplaceholder.md) — An object that contains information about a placeholder cell being inserted into a table.
