---
title: UIBandSelectionInteraction.State.possible
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibandselectioninteraction/state-swift.enum/possible
source_url: 'https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.enum/possible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibandselectioninteraction/state-swift.enum/possible.json'
content_hash: 'sha256:1d5de978ec875724'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIBandSelectionInteraction](../../uibandselectioninteraction.md) · [State](../state-swift.enum.md)

# UIBandSelectionInteraction.State.possible

<sub>Case</sub>

A state that indicates the interaction object is ready to start a new interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case possible
```

## Discussion

A [UIBandSelectionInteraction](../../uibandselectioninteraction.md) object in this state is waiting for events to occur that start the interaction. When an interaction concludes, the interaction returns to this state until a new interaction begins.

## See Also

### Getting the selection state

- [UIBandSelectionInteractionStateBegan](began.md) — A state that indicates the interaction object began a new interaction.
- [UIBandSelectionInteractionStateSelecting](selecting.md) — A state that indicates the interaction object is tracking changes to the selection rectangle.
- [UIBandSelectionInteractionStateEnded](ended.md) — A state that indicates the current interaction ended.
