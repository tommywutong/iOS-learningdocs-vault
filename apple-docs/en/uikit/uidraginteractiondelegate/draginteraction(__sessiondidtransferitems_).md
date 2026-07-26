---
title: 'dragInteraction(_:sessionDidTransferItems:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessiondidtransferitems:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessiondidtransferitems:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteractiondelegate/draginteraction%28_%3Asessiondidtransferitems%3A%29.json'
content_hash: 'sha256:436e4cc32b4323b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteractionDelegate](../uidraginteractiondelegate.md)

# dragInteraction(_:sessionDidTransferItems:)

<sub>Instance Method</sub>

Tells the delegate the destination view has received the data for the drag items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, sessionDidTransferItems session: any UIDragSession)
```

## Parameters

- `interaction` — The interaction that called this method.

- `session` — The drag session that has ended.

## Discussion

Implement this method if you need to clean up resources related to the drag items or their item provider objects.

## See Also

### Monitoring drag progress

- [- dragInteraction:sessionWillBegin:](<draginteraction(__sessionwillbegin_).md>) — Tells the delegate the lift animation has finished and the user is starting to move the items across the screen.
- [- dragInteraction:session:willAddItems:forInteraction:](<draginteraction(__session_willadd_for_).md>) — Tells the delegate an interaction is about to add items to a drag session.
- [- dragInteraction:sessionDidMove:](<draginteraction(__sessiondidmove_).md>) — Tells the delegate the user moved the drag items to a new location on the screen.
- [- dragInteraction:session:willEndWithOperation:](<draginteraction(__session_willendwith_).md>) — Tells the delegate the drag activity will end with the specified operation.
- [- dragInteraction:session:didEndWithOperation:](<draginteraction(__session_didendwith_).md>) — Tells the delegate the drag activity and its related animations have finished.
