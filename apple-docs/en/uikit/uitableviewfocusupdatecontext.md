---
title: UITableViewFocusUpdateContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewfocusupdatecontext
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewfocusupdatecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewfocusupdatecontext.json'
content_hash: 'sha256:406d4875d68c7f39'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewFocusUpdateContext

<sub>Class</sub>

A context object that provides information relevant to a specific focus update from one view to another.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITableViewFocusUpdateContext
```

## Overview

A focus update context provides extra information that’s only relevant to focus updates involving table views. Instances of this class are ephemeral and are usually discarded after the update is finished.

## Relationships

- **Inherits From**: [UIFocusUpdateContext](uifocusupdatecontext.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Locating focusable items in a table view

- [previouslyFocusedIndexPath](uitableviewfocusupdatecontext/previouslyfocusedindexpath.md) — Returns the index path of the cell containing the context’s previously focused view.
- [nextFocusedIndexPath](uitableviewfocusupdatecontext/nextfocusedindexpath.md) — Returns the index path of the cell containing the context’s next focused view.

## See Also

### Table management

- [Estimating the height of a table’s scrolling area](estimating-the-height-of-a-table-s-scrolling-area.md) — Provide height estimates for your table view’s headers, footers, and rows to ensure that scrolling accurately reflects the size of your content.
- [UITableViewController](uitableviewcontroller.md) — A view controller that specializes in managing a table view.
- [UITableViewDelegate](uitableviewdelegate.md) — Methods for managing selections, configuring section headers and footers, deleting and reordering cells, and performing other actions in a table view.
