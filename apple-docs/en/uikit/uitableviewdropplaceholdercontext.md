---
title: UITableViewDropPlaceholderContext
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdropplaceholdercontext
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropplaceholdercontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropplaceholdercontext.json'
content_hash: 'sha256:a8f30b1f02bee42a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewDropPlaceholderContext

<sub>Protocol</sub>

An object for tracking a placeholder cell that you added to your table during a drop operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITableViewDropPlaceholderContext : UIDragAnimating
```

## Overview

Don’t create instances of this class yourself. Instead, call [- dropItem:toPlaceholder:](<uitableviewdropcoordinator/drop(__to_)-3znax.md>) from your drop coordinator object. That method inserts a placeholder cell into the table and returns a [UITableViewDropPlaceholderContext](uitableviewdropplaceholdercontext.md) object for managing that placeholder.

When you’re ready to swap a placeholder cell for a cell with the actual data, call the [- commitInsertionWithDataSourceUpdates:](<uitableviewdropplaceholdercontext/commitinsertion(datasourceupdates_).md>) method of the context object. To remove the placeholder cell without providing a replacement, call [- deletePlaceholder](<uitableviewdropplaceholdercontext/deleteplaceholder().md>) instead.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIDragAnimating](uidraganimating.md)

## Topics

### Updating the placeholder cell

- [- commitInsertionWithDataSourceUpdates:](<uitableviewdropplaceholdercontext/commitinsertion(datasourceupdates_).md>) — Exchanges the placeholder cell for a cell with the final content.

### Removing the placeholder cell

- [- deletePlaceholder](<uitableviewdropplaceholdercontext/deleteplaceholder().md>) — Removes an unneeded placeholder cell from the table view.

### Getting the drag item

- [dragItem](uitableviewdropplaceholdercontext/dragitem.md) — The drag item represented by the placeholder cell.

## See Also

### Placeholder cells

- [UITableViewDropPlaceholder](uitableviewdropplaceholder.md) — A placeholder cell that supports customizing the drop preview parameters.
- [UITableViewPlaceholder](uitableviewplaceholder.md) — An object that contains information about a placeholder cell being inserted into a table.
