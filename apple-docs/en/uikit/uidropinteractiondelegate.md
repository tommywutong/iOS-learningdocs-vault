---
title: UIDropInteractionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidropinteractiondelegate
source_url: 'https://developer.apple.com/documentation/uikit/uidropinteractiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropinteractiondelegate.json'
content_hash: 'sha256:60d7effe95be5d4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDropInteractionDelegate

<sub>Protocol</sub>

The interface for configuring and controlling a drop interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIDropInteractionDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling the drop

- [- dropInteraction:canHandleSession:](<uidropinteractiondelegate/dropinteraction(__canhandle_).md>) — Asks the delegate whether it can handle the session’s drag items.
- [- dropInteraction:performDrop:](<uidropinteractiondelegate/dropinteraction(__performdrop_).md>) — Tells the delegate it can request the item provider data from the session’s drag items.

### Tracking the drop movements

- [- dropInteraction:sessionDidEnter:](<uidropinteractiondelegate/dropinteraction(__sessiondidenter_).md>) — Tells the delegate the drop session has moved into the drop interaction’s view.
- [- dropInteraction:sessionDidUpdate:](<uidropinteractiondelegate/dropinteraction(__sessiondidupdate_).md>) — Tells the delegate the drop session has changed.
- [- dropInteraction:sessionDidExit:](<uidropinteractiondelegate/dropinteraction(__sessiondidexit_).md>) — Tells the delegate the drop session has moved out of the drop interaction’s view.
- [- dropInteraction:sessionDidEnd:](<uidropinteractiondelegate/dropinteraction(__sessiondidend_).md>) — Tells the delegate the drop session has ended.

### Animating the drop

- [- dropInteraction:item:willAnimateDropWithAnimator:](<uidropinteractiondelegate/dropinteraction(__item_willanimatedropwith_).md>) — Tells the delegate the system’s drop animation is about to start.
- [- dropInteraction:previewForDroppingItem:withDefault:](<uidropinteractiondelegate/dropinteraction(__previewfordropping_withdefault_).md>) — Asks the delegate for the targeted drag item preview to show during the drop animation.
- [- dropInteraction:concludeDrop:](<uidropinteractiondelegate/dropinteraction(__concludedrop_).md>) — Tells the delegate the drop activity and its related animations have finished.

## See Also

### Drag and drop interactions

- [UIDragInteractionDelegate](uidraginteractiondelegate.md) — The interface for configuring and controlling a drag interaction.
- [UIDragInteraction](uidraginteraction.md) — An interaction to enable dragging of items from a view, employing a delegate to provide drag items and to respond to calls from the drag session.
- [UIDropInteraction](uidropinteraction.md) — An interaction to enable dropping of items onto a view, employing a delegate to instantiate objects and respond to calls from the drop session.
