---
title: UIBandSelectionInteraction.State.selecting
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibandselectioninteraction/state-swift.enum/selecting
source_url: 'https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.enum/selecting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibandselectioninteraction/state-swift.enum/selecting.json'
content_hash: 'sha256:22ff72311aa66075'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIBandSelectionInteraction](../../uibandselectioninteraction.md) · [State](../state-swift.enum.md)

# UIBandSelectionInteraction.State.selecting

<sub>Case</sub>

A state that indicates the interaction object is tracking changes to the selection rectangle.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case selecting
```

## Discussion

Use this state to select items that intersect the current selection rectangle.

## See Also

### Getting the selection state

- [UIBandSelectionInteractionStatePossible](possible.md) — A state that indicates the interaction object is ready to start a new interaction.
- [UIBandSelectionInteractionStateBegan](began.md) — A state that indicates the interaction object began a new interaction.
- [UIBandSelectionInteractionStateEnded](ended.md) — A state that indicates the current interaction ended.
