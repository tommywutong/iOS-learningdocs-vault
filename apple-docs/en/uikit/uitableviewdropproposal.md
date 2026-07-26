---
title: UITableViewDropProposal
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdropproposal
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropproposal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropproposal.json'
content_hash: 'sha256:efd08ddfd1ead7dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewDropProposal

<sub>Class</sub>

Your proposed solution for handling a drop in a table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UITableViewDropProposal
```

## Overview

Create instances of this class in the [- tableView:dropSessionDidUpdate:withDestinationIndexPath:](<uitableviewdropdelegate/tableview(__dropsessiondidupdate_withdestinationindexpath_).md>) method of your drop delegate object. You create drop proposals to let the table view know how you intend to handle a drop at the currently specified location. The table view uses that information to provide appropriate visual feedback to the user.

## Relationships

- **Inherits From**: [UIDropProposal](uidropproposal.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a drop proposal

- [- initWithDropOperation:intent:](<uitableviewdropproposal/init(operation_intent_).md>) — Creates a drop proposal object that specifies how to incorporate the dropped content.

### Getting the proposed drop location

- [intent](uitableviewdropproposal/intent-swift.property.md) — The option to use when incorporating dropped items into your content.
- [Intent](uitableviewdropproposal/intent-swift.enum.md) — Constants indicating how you intend to handle a drop.
- [UIDropOperation](uidropoperation.md) — Operation types that determine how a drag and drop activity resolves when the user drops a drag item.

### Initializers

- [init(dropOperation:intent:)](<uitableviewdropproposal/init(dropoperation_intent_).md>)

## See Also

### Drag and drop

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md) — Initiate drags and handle drops from a table view.
- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md) — Demonstrates how to enable and implement drag and drop for a table view.
- [UITableViewDragDelegate](uitableviewdragdelegate.md) — The interface for initiating drags from a table view.
- [UITableViewDropDelegate](uitableviewdropdelegate.md) — The interface for handling drops in a table view.
- [UITableViewDropCoordinator](uitableviewdropcoordinator.md) — An interface for coordinating your custom drop-related actions with the table view.
- [UITableViewDropItem](uitableviewdropitem.md) — The data associated with an item being dropped into the table view.
