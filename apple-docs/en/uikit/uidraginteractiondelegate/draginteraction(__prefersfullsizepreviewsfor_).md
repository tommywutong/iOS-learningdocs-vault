---
title: 'dragInteraction(_:prefersFullSizePreviewsFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraginteractiondelegate/draginteraction(_:prefersfullsizepreviewsfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:prefersfullsizepreviewsfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteractiondelegate/draginteraction%28_%3Aprefersfullsizepreviewsfor%3A%29.json'
content_hash: 'sha256:5dbb81851f30cc94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteractionDelegate](../uidraginteractiondelegate.md)

# dragInteraction(_:prefersFullSizePreviewsFor:)

<sub>Instance Method</sub>

Asks the delegate whether the preview should appear in its original size or a scaled size.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, prefersFullSizePreviewsFor session: any UIDragSession) -> Bool
```

## Parameters

- `interaction` — The interaction that called this method.

- `session` — The current drag session.

## Return Value

[true](../../swift/true.md) to tell the system the preview should appear in its original size; otherwise [false](../../swift/false.md), which is the default if you don’t provide this method.

## Discussion

The return value is a recommendation to the system. The system may choose to scale the preview to a smaller size, according to its own rules, even if you return [true](../../swift/true.md).

## See Also

### Providing drag previews

- [- dragInteraction:previewForLiftingItem:session:](<draginteraction(__previewforlifting_session_).md>) — Asks the delegate for the targeted drag item preview that will appear during the lift animation.
- [- dragInteraction:previewForCancellingItem:withDefault:](<draginteraction(__previewforcancelling_withdefault_).md>) — Asks the delegate for the targeted drag item preview to show during the cancellation animation.
