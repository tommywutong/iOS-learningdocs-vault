---
title: UIBandSelectionInteraction.State.ended
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibandselectioninteraction/state-swift.enum/ended
source_url: 'https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.enum/ended'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibandselectioninteraction/state-swift.enum/ended.json'
content_hash: 'sha256:3f553823d476f60f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIBandSelectionInteraction](../../uibandselectioninteraction.md) · [State](../state-swift.enum.md)

# UIBandSelectionInteraction.State.ended

<sub>Case</sub>

A state that indicates the current interaction ended.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case ended
```

## Discussion

Use this state to finalize the interaction. For example, you might finalize the selection of items in your view.

## See Also

### Getting the selection state

- [UIBandSelectionInteractionStatePossible](possible.md) — A state that indicates the interaction object is ready to start a new interaction.
- [UIBandSelectionInteractionStateBegan](began.md) — A state that indicates the interaction object began a new interaction.
- [UIBandSelectionInteractionStateSelecting](selecting.md) — A state that indicates the interaction object is tracking changes to the selection rectangle.
