---
title: 'dragInteraction(_:previewForCancelling:withDefault:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraginteractiondelegate/draginteraction(_:previewforcancelling:withdefault:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:previewforcancelling:withdefault:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteractiondelegate/draginteraction%28_%3Apreviewforcancelling%3Awithdefault%3A%29.json'
content_hash: 'sha256:470a4ded098764b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteractionDelegate](../uidraginteractiondelegate.md)

# dragInteraction(_:previewForCancelling:withDefault:)

<sub>Instance Method</sub>

Asks the delegate for the targeted drag item preview to show during the cancellation animation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, previewForCancelling item: UIDragItem, withDefault defaultPreview: UITargetedDragPreview) -> UITargetedDragPreview?
```

## Parameters

- `interaction` — The interaction that called this method.

- `item` — The drag item represented by the preview.

- `defaultPreview` — A targeted drag preview provided by the system.

## Return Value

- The default preview provided by the system.
- A targeted drag item preview you create.
- The preview returned after moving to a new preview target (using the `defaultPreview`’s [- retargetedPreviewWithTarget:](<../uitargeteddragpreview/retargetedpreview(with_).md>) method).
- `nil` to fade the preview that is currently displayed to the user, which is the same behavior as not implementing this method.

## Discussion

The system calls this method multiple times, once for each visible drag item.

When you return a preview, the system shows it during the cancellation animation in order to visually “move” the drag item to the location of the preview’s associated `view`.

## See Also

### Providing drag previews

- [- dragInteraction:previewForLiftingItem:session:](<draginteraction(__previewforlifting_session_).md>) — Asks the delegate for the targeted drag item preview that will appear during the lift animation.
- [- dragInteraction:prefersFullSizePreviewsForSession:](<draginteraction(__prefersfullsizepreviewsfor_).md>) — Asks the delegate whether the preview should appear in its original size or a scaled size.
