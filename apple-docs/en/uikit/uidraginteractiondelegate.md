---
title: UIDragInteractionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidraginteractiondelegate
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteractiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteractiondelegate.json'
content_hash: 'sha256:2f4d3a53e156548a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDragInteractionDelegate

<sub>Protocol</sub>

The interface for configuring and controlling a drag interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIDragInteractionDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Performing the drag

- [- dragInteraction:itemsForBeginningSession:](<uidraginteractiondelegate/draginteraction(__itemsforbeginning_).md>) — Asks the delegate for the array of drag items for an impending drag interaction.
- [- dragInteraction:itemsForAddingToSession:withTouchAtPoint:](<uidraginteractiondelegate/draginteraction(__itemsforaddingto_withtouchat_).md>) — Asks the delegate for the drag items to add to an in-progress drag session, in response to a user gesture to add the items.
- [- dragInteraction:sessionForAddingItems:withTouchAtPoint:](<uidraginteractiondelegate/draginteraction(__sessionforaddingitems_withtouchat_).md>) — Asks the delegate which drag session to add drag items to when there is more than one in-progress session.

### Animating the drag behaviors

- [- dragInteraction:willAnimateLiftWithAnimator:session:](<uidraginteractiondelegate/draginteraction(__willanimateliftwith_session_).md>) — Tells the delegate the system’s lift animation is about to start.
- [- dragInteraction:item:willAnimateCancelWithAnimator:](<uidraginteractiondelegate/draginteraction(__item_willanimatecancelwith_).md>) — Tells the delegate the system’s cancellation animation is about to start.

### Monitoring drag progress

- [- dragInteraction:sessionWillBegin:](<uidraginteractiondelegate/draginteraction(__sessionwillbegin_).md>) — Tells the delegate the lift animation has finished and the user is starting to move the items across the screen.
- [- dragInteraction:session:willAddItems:forInteraction:](<uidraginteractiondelegate/draginteraction(__session_willadd_for_).md>) — Tells the delegate an interaction is about to add items to a drag session.
- [- dragInteraction:sessionDidMove:](<uidraginteractiondelegate/draginteraction(__sessiondidmove_).md>) — Tells the delegate the user moved the drag items to a new location on the screen.
- [- dragInteraction:session:willEndWithOperation:](<uidraginteractiondelegate/draginteraction(__session_willendwith_).md>) — Tells the delegate the drag activity will end with the specified operation.
- [- dragInteraction:session:didEndWithOperation:](<uidraginteractiondelegate/draginteraction(__session_didendwith_).md>) — Tells the delegate the drag activity and its related animations have finished.
- [- dragInteraction:sessionDidTransferItems:](<uidraginteractiondelegate/draginteraction(__sessiondidtransferitems_).md>) — Tells the delegate the destination view has received the data for the drag items.

### Providing drag previews

- [- dragInteraction:previewForLiftingItem:session:](<uidraginteractiondelegate/draginteraction(__previewforlifting_session_).md>) — Asks the delegate for the targeted drag item preview that will appear during the lift animation.
- [- dragInteraction:previewForCancellingItem:withDefault:](<uidraginteractiondelegate/draginteraction(__previewforcancelling_withdefault_).md>) — Asks the delegate for the targeted drag item preview to show during the cancellation animation.
- [- dragInteraction:prefersFullSizePreviewsForSession:](<uidraginteractiondelegate/draginteraction(__prefersfullsizepreviewsfor_).md>) — Asks the delegate whether the preview should appear in its original size or a scaled size.

### Restricting the drag behavior

- [- dragInteraction:sessionIsRestrictedToDraggingApplication:](<uidraginteractiondelegate/draginteraction(__sessionisrestrictedtodraggingapplication_).md>) — Asks the delegate whether the system should restrict the drag session to the app that started the session.
- [- dragInteraction:sessionAllowsMoveOperation:](<uidraginteractiondelegate/draginteraction(__sessionallowsmoveoperation_).md>) — Asks the delegate whether the session allows the move operation.

## See Also

### Drag and drop interactions

- [UIDropInteractionDelegate](uidropinteractiondelegate.md) — The interface for configuring and controlling a drop interaction.
- [UIDragInteraction](uidraginteraction.md) — An interaction to enable dragging of items from a view, employing a delegate to provide drag items and to respond to calls from the drag session.
- [UIDropInteraction](uidropinteraction.md) — An interaction to enable dropping of items onto a view, employing a delegate to instantiate objects and respond to calls from the drop session.
