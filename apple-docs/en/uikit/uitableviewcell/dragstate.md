---
title: UITableViewCell.DragState
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/dragstate
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/dragstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/dragstate.json'
content_hash: 'sha256:db413c888742ab08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# UITableViewCell.DragState

<sub>Enumeration</sub>

Constants indicating the current state of a row involved in a drag operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum DragState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UITableViewCellDragStateNone](dragstate/none.md) — The cell isn’t involved in a drag operation.
- [UITableViewCellDragStateLifting](dragstate/lifting.md) — The cell is being animated off of the table’s surface.
- [UITableViewCellDragStateDragging](dragstate/dragging.md) — The cell is currently being dragged.

### Initializers

- [init(rawValue:)](<dragstate/init(rawvalue_).md>)

## See Also

### Dragging the row

- [userInteractionEnabledWhileDragging](userinteractionenabledwhiledragging.md) — A Boolean value indicating whether users can interact with a cell while it is being dragged.
- [- dragStateDidChange:](<dragstatedidchange(__).md>) — Notifies the cell that its drag status changed.
