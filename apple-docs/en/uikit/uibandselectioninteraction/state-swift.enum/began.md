---
title: UIBandSelectionInteraction.State.began
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibandselectioninteraction/state-swift.enum/began
source_url: 'https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.enum/began'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibandselectioninteraction/state-swift.enum/began.json'
content_hash: 'sha256:ff443b342e7d4041'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIBandSelectionInteraction](../../uibandselectioninteraction.md) · [State](../state-swift.enum.md)

# UIBandSelectionInteraction.State.began

<sub>Case</sub>

A state that indicates the interaction object began a new interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case began
```

## Discussion

The interaction object enters this state once at the beginning of each interaction, and subsequently transitions to the [UIBandSelectionInteractionStateSelecting](selecting.md) or [UIBandSelectionInteractionStateEnded](ended.md) state. When in this state, perform any one-time tasks that you need to manage your app’s state. For example, you might prepare your view to start the selection of items.

## See Also

### Getting the selection state

- [UIBandSelectionInteractionStatePossible](possible.md) — A state that indicates the interaction object is ready to start a new interaction.
- [UIBandSelectionInteractionStateSelecting](selecting.md) — A state that indicates the interaction object is tracking changes to the selection rectangle.
- [UIBandSelectionInteractionStateEnded](ended.md) — A state that indicates the current interaction ended.
