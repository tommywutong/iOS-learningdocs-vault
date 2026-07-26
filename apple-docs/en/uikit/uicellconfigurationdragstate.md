---
title: UICellConfigurationDragState
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellconfigurationdragstate
source_url: 'https://developer.apple.com/documentation/uikit/uicellconfigurationdragstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellconfigurationdragstate.json'
content_hash: 'sha256:cb1c588a5b872787'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICellConfigurationDragState

<sub>Enumeration</sub>

Constants that describe the cell’s drag state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
enum UICellConfigurationDragState : NSInteger;
```

## Topics

### Drag states

- [UICellConfigurationDragStateNone](uicellconfigurationdragstate/uicellconfigurationdragstatenone.md) — The system hasn’t associated the cell with a drag session.
- [UICellConfigurationDragStateLifting](uicellconfigurationdragstate/uicellconfigurationdragstatelifting.md) — A user interaction is lifting the cell, but it isn’t yet part of an active drag session.
- [UICellConfigurationDragStateDragging](uicellconfigurationdragstate/uicellconfigurationdragstatedragging.md) — The cell is part of an active drag session.

## See Also

### Managing cell configuration states

- [editing](uicellconfigurationstate-c.class/editing.md) — A Boolean value that indicates whether the cell is in editing mode.
- [swiped](uicellconfigurationstate-c.class/swiped.md) — A Boolean value that indicates whether the cell is in a swiped state.
- [expanded](uicellconfigurationstate-c.class/expanded.md) — A Boolean value that indicates whether the cell is in an expanded state, such as in an outline.
- [reordering](uicellconfigurationstate-c.class/reordering.md) — A Boolean value that indicates whether the cell is reordering.
- [cellDragState](uicellconfigurationstate-c.class/celldragstate.md) — The cell’s drag state.
- [cellDropState](uicellconfigurationstate-c.class/celldropstate.md) — The cell’s drop state.
- [UICellConfigurationDropState](uicellconfigurationdropstate.md) — Constants that describe the cell’s drop state.
