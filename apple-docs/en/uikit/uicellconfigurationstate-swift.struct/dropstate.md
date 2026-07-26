---
title: UICellConfigurationState.DropState
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellconfigurationstate-swift.struct/dropstate
source_url: 'https://developer.apple.com/documentation/uikit/uicellconfigurationstate-swift.struct/dropstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellconfigurationstate-swift.struct/dropstate.json'
content_hash: 'sha256:b2d82e90526df2c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellConfigurationState](../uicellconfigurationstate-swift.struct.md)

# UICellConfigurationState.DropState

<sub>Enumeration</sub>

Constants that describe the cell’s drop state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum DropState
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md)

## Topics

### Drop states

- [UICellConfigurationState.DropState.none](dropstate/none.md) — The system hasn’t associated the cell with a drag session.
- [UICellConfigurationState.DropState.notTargeted](dropstate/nottargeted.md) — A drag session is active and can perform a drop in the cell’s container, but the cell itself isn’t the drop target.
- [UICellConfigurationState.DropState.targeted](dropstate/targeted.md) — The cell is the drop target for a drag session.

## See Also

### Managing cell configuration states

- [isEditing](isediting.md) — A Boolean value that indicates whether the cell is in editing mode.
- [isSwiped](isswiped.md) — A Boolean value that indicates whether the cell is in a swiped state.
- [isExpanded](isexpanded.md) — A Boolean value that indicates whether the cell is in an expanded state, such as in an outline.
- [isReordering](isreordering.md) — A Boolean value that indicates whether the cell is reordering.
- [cellDragState](celldragstate.md) — The cell’s drag state.
- [cellDropState](celldropstate.md) — The cell’s drop state.
- [DragState](dragstate.md) — Constants that describe the cell’s drag state.
