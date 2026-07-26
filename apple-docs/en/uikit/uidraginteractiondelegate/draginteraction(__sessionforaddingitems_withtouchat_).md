---
title: 'dragInteraction(_:sessionForAddingItems:withTouchAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessionforaddingitems:withtouchat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessionforaddingitems:withtouchat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteractiondelegate/draginteraction%28_%3Asessionforaddingitems%3Awithtouchat%3A%29.json'
content_hash: 'sha256:fec665f6549f0d82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteractionDelegate](../uidraginteractiondelegate.md)

# dragInteraction(_:sessionForAddingItems:withTouchAt:)

<sub>Instance Method</sub>

Asks the delegate which drag session to add drag items to when there is more than one in-progress session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, sessionForAddingItems sessions: [any UIDragSession], withTouchAt point: CGPoint) -> (any UIDragSession)?
```

## Parameters

- `interaction` — The interaction that called this method.

- `sessions` — An array of in-progress drag sessions.

- `point` — The location of the user’s touch in the view. The touch point is in the view’s coordinate system.

## Return Value

The drag session to add drag items to, or `nil` to continue without adding drag items to any drag session.

## Discussion

If more than one drag session exists, the session used to add drag items may not be apparent to the user. Therefore, by default, no items are added to any session. If you want to change this behavior, implement this method and return the appropriate session. Return `nil` to continue without adding items.

## See Also

### Performing the drag

- [- dragInteraction:itemsForBeginningSession:](<draginteraction(__itemsforbeginning_).md>) — Asks the delegate for the array of drag items for an impending drag interaction.
- [- dragInteraction:itemsForAddingToSession:withTouchAtPoint:](<draginteraction(__itemsforaddingto_withtouchat_).md>) — Asks the delegate for the drag items to add to an in-progress drag session, in response to a user gesture to add the items.
