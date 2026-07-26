---
title: 'dragInteraction(_:session:willAdd:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraginteractiondelegate/draginteraction(_:session:willadd:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:session:willadd:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteractiondelegate/draginteraction%28_%3Asession%3Awilladd%3Afor%3A%29.json'
content_hash: 'sha256:9c42483fafc43907'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteractionDelegate](../uidraginteractiondelegate.md)

# dragInteraction(_:session:willAdd:for:)

<sub>Instance Method</sub>

Tells the delegate an interaction is about to add items to a drag session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, session: any UIDragSession, willAdd items: [UIDragItem], for addingInteraction: UIDragInteraction)
```

## Parameters

- `interaction` — The interaction that called this method.

- `session` — The current drag session.

- `items` — The drag items the interaction will add to the session.

- `addingInteraction` — The interaction adding the drag items.

## See Also

### Monitoring drag progress

- [- dragInteraction:sessionWillBegin:](<draginteraction(__sessionwillbegin_).md>) — Tells the delegate the lift animation has finished and the user is starting to move the items across the screen.
- [- dragInteraction:sessionDidMove:](<draginteraction(__sessiondidmove_).md>) — Tells the delegate the user moved the drag items to a new location on the screen.
- [- dragInteraction:session:willEndWithOperation:](<draginteraction(__session_willendwith_).md>) — Tells the delegate the drag activity will end with the specified operation.
- [- dragInteraction:session:didEndWithOperation:](<draginteraction(__session_didendwith_).md>) — Tells the delegate the drag activity and its related animations have finished.
- [- dragInteraction:sessionDidTransferItems:](<draginteraction(__sessiondidtransferitems_).md>) — Tells the delegate the destination view has received the data for the drag items.
