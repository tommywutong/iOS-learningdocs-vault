---
title: UICellConfigurationDropState
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellconfigurationdropstate
source_url: 'https://developer.apple.com/documentation/uikit/uicellconfigurationdropstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellconfigurationdropstate.json'
content_hash: 'sha256:75b4eeda7ac8ca02'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICellConfigurationDropState

<sub>Enumeration</sub>

Constants that describe the cell’s drop state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
enum UICellConfigurationDropState : NSInteger;
```

## Topics

### Drop states

- [UICellConfigurationDropStateNone](uicellconfigurationdropstate/uicellconfigurationdropstatenone.md) — The system hasn’t associated the cell with a drag session.
- [UICellConfigurationDropStateNotTargeted](uicellconfigurationdropstate/uicellconfigurationdropstatenottargeted.md) — A drag session is active and can perform a drop in the cell’s container, but the cell itself isn’t the drop target.
- [UICellConfigurationDropStateTargeted](uicellconfigurationdropstate/uicellconfigurationdropstatetargeted.md) — The cell is the drop target for a drag session.

## See Also

### Managing cell configuration states

- [editing](uicellconfigurationstate-c.class/editing.md) — A Boolean value that indicates whether the cell is in editing mode.
- [swiped](uicellconfigurationstate-c.class/swiped.md) — A Boolean value that indicates whether the cell is in a swiped state.
- [expanded](uicellconfigurationstate-c.class/expanded.md) — A Boolean value that indicates whether the cell is in an expanded state, such as in an outline.
- [reordering](uicellconfigurationstate-c.class/reordering.md) — A Boolean value that indicates whether the cell is reordering.
- [cellDragState](uicellconfigurationstate-c.class/celldragstate.md) — The cell’s drag state.
- [cellDropState](uicellconfigurationstate-c.class/celldropstate.md) — The cell’s drop state.
- [UICellConfigurationDragState](uicellconfigurationdragstate.md) — Constants that describe the cell’s drag state.
