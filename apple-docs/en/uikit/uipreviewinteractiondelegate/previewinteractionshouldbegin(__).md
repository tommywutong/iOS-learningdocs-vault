---
title: 'previewInteractionShouldBegin(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipreviewinteractiondelegate/previewinteractionshouldbegin(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewinteractiondelegate/previewinteractionshouldbegin(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewinteractiondelegate/previewinteractionshouldbegin%28_%3A%29.json'
content_hash: 'sha256:d25b01d0b28b5254'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewInteractionDelegate](../uipreviewinteractiondelegate.md)

# previewInteractionShouldBegin(_:)

<sub>Instance Method</sub>

Asks the delegate whether a preview interaction is allowed to begin.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func previewInteractionShouldBegin(_ previewInteraction: UIPreviewInteraction) -> Bool
```

## Parameters

- `previewInteraction` — The preview interaction that’s responding to user input.

## Return Value

[true](../../swift/true.md) if the preview interaction should continue into the preview and commit phases; otherwise [false](../../swift/false.md).

## Discussion

If you don’t implement this optional method, the default return value of [true](../../swift/true.md) is assumed.

When [false](../../swift/false.md), no further delegate calls are made for the specified preview interaction until the user restarts the 3D Touch interaction.

## See Also

### Managing preview interactions

- [- previewInteraction:didUpdatePreviewTransition:ended:](<previewinteraction(__didupdatepreviewtransition_ended_).md>) — Informs the delegate of the progress through the preview phase of the preview interaction.
- [- previewInteraction:didUpdateCommitTransition:ended:](<previewinteraction(__didupdatecommittransition_ended_).md>) — Informs the delegate of the preview interaction’s progress through the commit phase.
- [- previewInteractionDidCancel:](<previewinteractiondidcancel(__).md>) — Informs the delegate that the specified preview interaction was canceled.
