---
title: 'dragInteraction(_:previewForLifting:session:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraginteractiondelegate/draginteraction(_:previewforlifting:session:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:previewforlifting:session:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteractiondelegate/draginteraction%28_%3Apreviewforlifting%3Asession%3A%29.json'
content_hash: 'sha256:81a44195d878d1bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteractionDelegate](../uidraginteractiondelegate.md)

# dragInteraction(_:previewForLifting:session:)

<sub>Instance Method</sub>

Asks the delegate for the targeted drag item preview that will appear during the lift animation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, previewForLifting item: UIDragItem, session: any UIDragSession) -> UITargetedDragPreview?
```

## Parameters

- `interaction` — The interaction that called this method.

- `item` — The drag item represented by the preview.

- `session` — The current drag session.

## Return Value

A targeted drag item preview you create, or `nil` to tell the system not to display the lift animation.

## Discussion

If you don’t provide this method, the system creates a preview based on the view owned by the drag interaction.

## See Also

### Providing drag previews

- [- dragInteraction:previewForCancellingItem:withDefault:](<draginteraction(__previewforcancelling_withdefault_).md>) — Asks the delegate for the targeted drag item preview to show during the cancellation animation.
- [- dragInteraction:prefersFullSizePreviewsForSession:](<draginteraction(__prefersfullsizepreviewsfor_).md>) — Asks the delegate whether the preview should appear in its original size or a scaled size.
