---
title: 'previewInteraction(_:didUpdatePreviewTransition:ended:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipreviewinteractiondelegate/previewinteraction(_:didupdatepreviewtransition:ended:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewinteractiondelegate/previewinteraction(_:didupdatepreviewtransition:ended:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewinteractiondelegate/previewinteraction%28_%3Adidupdatepreviewtransition%3Aended%3A%29.json'
content_hash: 'sha256:1ac406f3a67f7193'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewInteractionDelegate](../uipreviewinteractiondelegate.md)

# previewInteraction(_:didUpdatePreviewTransition:ended:)

<sub>Instance Method</sub>

Informs the delegate of the progress through the preview phase of the preview interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func previewInteraction(_ previewInteraction: UIPreviewInteraction, didUpdatePreviewTransition transitionProgress: CGFloat, ended: Bool)
```

## Parameters

- `previewInteraction` — The preview interaction associated with the current user input.

- `transitionProgress` — The progress through the preview phase of the transition. A [CGFloat](../../corefoundation/cgfloat-swift.struct.md) with a value from `0` to `1`.

- `ended` — A Boolean whose value indicates whether the preview phase of the transition is complete.

## Discussion

This method is called repeatedly during the preview phase of the preview interaction. Use the supplied `transitionProgress` parameter to update the UI to reflect the progress of the interaction. For example, the _peek_ effect in view controller preview transitions progressively blurs everything except the appropriate view.

The `ended` parameter is [false](../../swift/false.md) throughout the preview phase and becomes [true](../../swift/true.md) as the phase is completed. The preview interaction then transitions to the commit phase, so you should use this point to update the UI as required.

## See Also

### Managing preview interactions

- [- previewInteractionShouldBegin:](<previewinteractionshouldbegin(__).md>) — Asks the delegate whether a preview interaction is allowed to begin.
- [- previewInteraction:didUpdateCommitTransition:ended:](<previewinteraction(__didupdatecommittransition_ended_).md>) — Informs the delegate of the preview interaction’s progress through the commit phase.
- [- previewInteractionDidCancel:](<previewinteractiondidcancel(__).md>) — Informs the delegate that the specified preview interaction was canceled.
