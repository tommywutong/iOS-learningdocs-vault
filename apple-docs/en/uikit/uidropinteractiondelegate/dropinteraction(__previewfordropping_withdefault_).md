---
title: 'dropInteraction(_:previewForDropping:withDefault:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:previewfordropping:withdefault:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:previewfordropping:withdefault:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropinteractiondelegate/dropinteraction%28_%3Apreviewfordropping%3Awithdefault%3A%29.json'
content_hash: 'sha256:7866df7bd832c8fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropInteractionDelegate](../uidropinteractiondelegate.md)

# dropInteraction(_:previewForDropping:withDefault:)

<sub>Instance Method</sub>

Asks the delegate for the targeted drag item preview to show during the drop animation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dropInteraction(_ interaction: UIDropInteraction, previewForDropping item: UIDragItem, withDefault defaultPreview: UITargetedDragPreview) -> UITargetedDragPreview?
```

## Parameters

- `interaction` — The interaction that called this method.

- `item` — The drag item represented by the preview.

- `defaultPreview` — A targeted drag preview provided by the system, if this is the first call for this item; otherwise, it’s the previous value for the drag preview.

## Return Value

- The default preview, which is the same behavior as not implementing this method.
- A targeted drag item preview that you create.
- The preview returned after moving to a new preview target by using the `defaultPreview`’s [- retargetedPreviewWithTarget:](<../uitargeteddragpreview/retargetedpreview(with_).md>) method.
- `nil` to fade the preview that is currently displayed to the user.

## Discussion

The system calls this method multiple times, once for each visible drag item. It shows the preview during the drop animation in order to visually _drop_ the drag item into place.

If you call [- setNeedsDropPreviewUpdate](<../uidragitem/setneedsdroppreviewupdate().md>) to tell the system to request a new drop preview, the system provides the previous value in the `defaultPreview` parameter.

## See Also

### Animating the drop

- [- dropInteraction:item:willAnimateDropWithAnimator:](<dropinteraction(__item_willanimatedropwith_).md>) — Tells the delegate the system’s drop animation is about to start.
- [- dropInteraction:concludeDrop:](<dropinteraction(__concludedrop_).md>) — Tells the delegate the drop activity and its related animations have finished.
