---
title: UICellConfigurationState.DragState
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellconfigurationstate-swift.struct/dragstate
source_url: 'https://developer.apple.com/documentation/uikit/uicellconfigurationstate-swift.struct/dragstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellconfigurationstate-swift.struct/dragstate.json'
content_hash: 'sha256:e37d9d74227fcf79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellConfigurationState](../uicellconfigurationstate-swift.struct.md)

# UICellConfigurationState.DragState

<sub>Enumeration</sub>

Constants that describe the cell’s drag state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum DragState
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md)

## Topics

### Drag states

- [UICellConfigurationState.DragState.none](dragstate/none.md) — The system hasn’t associated the cell with a drag session.
- [UICellConfigurationState.DragState.lifting](dragstate/lifting.md) — A user interaction is lifting the cell, but it isn’t yet part of an active drag session.
- [UICellConfigurationState.DragState.dragging](dragstate/dragging.md) — The cell is part of an active drag session.

## See Also

### Managing cell configuration states

- [isEditing](isediting.md) — A Boolean value that indicates whether the cell is in editing mode.
- [isSwiped](isswiped.md) — A Boolean value that indicates whether the cell is in a swiped state.
- [isExpanded](isexpanded.md) — A Boolean value that indicates whether the cell is in an expanded state, such as in an outline.
- [isReordering](isreordering.md) — A Boolean value that indicates whether the cell is reordering.
- [cellDragState](celldragstate.md) — The cell’s drag state.
- [cellDropState](celldropstate.md) — The cell’s drop state.
- [DropState](dropstate.md) — Constants that describe the cell’s drop state.
