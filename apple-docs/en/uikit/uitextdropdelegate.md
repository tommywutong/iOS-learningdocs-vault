---
title: UITextDropDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropdelegate.json'
content_hash: 'sha256:4ff11925b5a15bbf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextDropDelegate

<sub>Protocol</sub>

The interface for configuring a text view’s drop behavior.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITextDropDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accepting a drop activity

- [- textDroppableView:proposalForDrop:](<uitextdropdelegate/textdroppableview(__proposalfordrop_).md>) — Asks the delegate if the text view can accept a drop operation.
- [- textDroppableView:willBecomeEditableForDrop:](<uitextdropdelegate/textdroppableview(__willbecomeeditablefordrop_).md>) — Asks the delegate if a noneditable text view can accept a drop operation.

### Handling drop session notifications

- [- textDroppableView:dropSessionDidEnter:](<uitextdropdelegate/textdroppableview(__dropsessiondidenter_).md>) — Tells the delegate that the user has moved the drag items into the coordinate system of the text view.
- [- textDroppableView:dropSessionDidExit:](<uitextdropdelegate/textdroppableview(__dropsessiondidexit_).md>) — Tells the delegate that the user has moved the drag items out of the text view’s coordinate system.
- [- textDroppableView:dropSessionDidUpdate:](<uitextdropdelegate/textdroppableview(__dropsessiondidupdate_).md>) — Tells the delegate that the drop session has been updated.
- [- textDroppableView:dropSessionDidEnd:](<uitextdropdelegate/textdroppableview(__dropsessiondidend_).md>) — Tells the delegate that the drop session has ended.

### Handling drop activity notifications

- [- textDroppableView:willPerformDrop:](<uitextdropdelegate/textdroppableview(__willperformdrop_).md>) — Tells the delegate that the drop operation is about to happen.

### Providing a custom preview for a drop activity

- [- textDroppableView:previewForDroppingAllItemsWithDefault:](<uitextdropdelegate/textdroppableview(__previewfordroppingallitemswithdefault_).md>) — Asks the delegate for the preview to show during the drop animation.

## See Also

### Text view additions

- [UITextDragDelegate](uitextdragdelegate.md) — The interface for customizing the behavior of a drag activity for a text view.
- [UITextDraggable](uitextdraggable.md) — The interface that determines if a text view is a drag source.
- [UITextDragOptions](uitextdragoptions.md) — A set of options that determine the behavior of a draggable text view.
- [UITextDroppable](uitextdroppable.md) — The interface that determines if a text view is a drop destination.
- [UITextDropEditability](uitextdropeditability.md) — The text-drop editability styles for noneditable text views.
