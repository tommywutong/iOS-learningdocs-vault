---
title: UITableViewPlaceholder
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewplaceholder
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewplaceholder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewplaceholder.json'
content_hash: 'sha256:a1c60a861129abe9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewPlaceholder

<sub>Class</sub>

An object that contains information about a placeholder cell being inserted into a table.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UITableViewPlaceholder
```

## Overview

During a drop operation, create a [UITableViewDropPlaceholder](uitableviewdropplaceholder.md) object (instead of this one) to insert placeholders into your table.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UITableViewDropPlaceholder](uitableviewdropplaceholder.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a placeholder cell

- [- initWithInsertionIndexPath:reuseIdentifier:rowHeight:](<uitableviewplaceholder/init(insertionindexpath_reuseidentifier_rowheight_).md>) — Creates a placeholder object with the specified index path and cell-related information.

### Updating the cell’s content

- [cellUpdateHandler](uitableviewplaceholder/cellupdatehandler.md) — The block that updates the contents of the placeholder cell.

## See Also

### Placeholder cells

- [UITableViewDropPlaceholderContext](uitableviewdropplaceholdercontext.md) — An object for tracking a placeholder cell that you added to your table during a drop operation.
- [UITableViewDropPlaceholder](uitableviewdropplaceholder.md) — A placeholder cell that supports customizing the drop preview parameters.
