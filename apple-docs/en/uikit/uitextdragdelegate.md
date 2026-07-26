---
title: UITextDragDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdragdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragdelegate.json'
content_hash: 'sha256:25b5377509dad7b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextDragDelegate

<sub>Protocol</sub>

The interface for customizing the behavior of a drag activity for a text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITextDragDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling drag session notifications

- [- textDraggableView:dragSessionWillBegin:](<uitextdragdelegate/textdraggableview(__dragsessionwillbegin_).md>) — Tells the delegate that the text has been lifted out of the text view and the user is beginning to drag the text.
- [- textDraggableView:dragSessionDidEnd:withOperation:](<uitextdragdelegate/textdraggableview(__dragsessiondidend_with_).md>) — Tells the delegate that the drag session has ended.

### Providing additional animations

- [- textDraggableView:willAnimateLiftWithAnimator:session:](<uitextdragdelegate/textdraggableview(__willanimateliftwith_session_).md>) — Tells the delegate when the lift animation is about to begin, and gives you a chance to animate additional changes alongside the system animation.

### Providing custom drag items

- [- textDraggableView:itemsForDrag:](<uitextdragdelegate/textdraggableview(__itemsfordrag_).md>) — Asks the delegate for custom drag items from a text view.

### Providing a custom preview for a drag activity

- [- textDraggableView:dragPreviewForLiftingItem:session:](<uitextdragdelegate/textdraggableview(__dragpreviewforliftingitem_session_).md>) — Asks the delegate for the preview to show during the lift animation that happens when a user begins to drag an item from a text view.

## See Also

### Text view additions

- [UITextDropDelegate](uitextdropdelegate.md) — The interface for configuring a text view’s drop behavior.
- [UITextDraggable](uitextdraggable.md) — The interface that determines if a text view is a drag source.
- [UITextDragOptions](uitextdragoptions.md) — A set of options that determine the behavior of a draggable text view.
- [UITextDroppable](uitextdroppable.md) — The interface that determines if a text view is a drop destination.
- [UITextDropEditability](uitextdropeditability.md) — The text-drop editability styles for noneditable text views.
