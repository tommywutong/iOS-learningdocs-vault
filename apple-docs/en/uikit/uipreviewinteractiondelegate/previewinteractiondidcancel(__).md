---
title: 'previewInteractionDidCancel(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipreviewinteractiondelegate/previewinteractiondidcancel(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewinteractiondelegate/previewinteractiondidcancel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewinteractiondelegate/previewinteractiondidcancel%28_%3A%29.json'
content_hash: 'sha256:2593deae7ee49dcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewInteractionDelegate](../uipreviewinteractiondelegate.md)

# previewInteractionDidCancel(_:)

<sub>Instance Method</sub>

Informs the delegate that the specified preview interaction was canceled.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func previewInteractionDidCancel(_ previewInteraction: UIPreviewInteraction)
```

## Parameters

- `previewInteraction` — The preview interaction associated with the current user input.

## Discussion

This method is called when the preview interaction is canceled, either programmatically through the [- cancelInteraction](<../uipreviewinteraction/cancel().md>) method on [UIPreviewInteraction](../uipreviewinteraction.md), or by interrupting the preview interaction before the commit phase is complete.

## See Also

### Managing preview interactions

- [- previewInteractionShouldBegin:](<previewinteractionshouldbegin(__).md>) — Asks the delegate whether a preview interaction is allowed to begin.
- [- previewInteraction:didUpdatePreviewTransition:ended:](<previewinteraction(__didupdatepreviewtransition_ended_).md>) — Informs the delegate of the progress through the preview phase of the preview interaction.
- [- previewInteraction:didUpdateCommitTransition:ended:](<previewinteraction(__didupdatecommittransition_ended_).md>) — Informs the delegate of the preview interaction’s progress through the commit phase.
