---
title: 'previewInteraction(_:didUpdateCommitTransition:ended:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipreviewinteractiondelegate/previewinteraction(_:didupdatecommittransition:ended:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewinteractiondelegate/previewinteraction(_:didupdatecommittransition:ended:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewinteractiondelegate/previewinteraction%28_%3Adidupdatecommittransition%3Aended%3A%29.json'
content_hash: 'sha256:165164ef212c069c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewInteractionDelegate](../uipreviewinteractiondelegate.md)

# previewInteraction(_:didUpdateCommitTransition:ended:)

<sub>Instance Method</sub>

Informs the delegate of the preview interaction’s progress through the commit phase.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func previewInteraction(_ previewInteraction: UIPreviewInteraction, didUpdateCommitTransition transitionProgress: CGFloat, ended: Bool)
```

## Parameters

- `previewInteraction` — The preview interaction associated with the current user input.

- `transitionProgress` — The progress through the commit phase of the transition. A [CGFloat](../../corefoundation/cgfloat-swift.struct.md) with a value from `0` to `1`.

- `ended` — A `Boolean` whose value indicates whether the commit phase of the transition is complete.

## Discussion

This method is called repeatedly during the commit phase of the preview interaction. Use the supplied `transitionProgress` parameter to update the UI to reflect the progress of the interaction. For example, the _pop_ effect in view controller preview transitions progressively increases the size of the child view controller as the transition progresses.

The `ended` parameter is false throughout the commit phase and becomes [true](../../swift/true.md) when the phase is completed. At this point, the preview interaction is complete, and you should update the UI appropriately. For example, in view controller preview interactions, the child view controller becomes the main view controller.

## See Also

### Managing preview interactions

- [- previewInteractionShouldBegin:](<previewinteractionshouldbegin(__).md>) — Asks the delegate whether a preview interaction is allowed to begin.
- [- previewInteraction:didUpdatePreviewTransition:ended:](<previewinteraction(__didupdatepreviewtransition_ended_).md>) — Informs the delegate of the progress through the preview phase of the preview interaction.
- [- previewInteractionDidCancel:](<previewinteractiondidcancel(__).md>) — Informs the delegate that the specified preview interaction was canceled.
