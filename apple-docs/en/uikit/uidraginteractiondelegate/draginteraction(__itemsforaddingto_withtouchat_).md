---
title: 'dragInteraction(_:itemsForAddingTo:withTouchAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraginteractiondelegate/draginteraction(_:itemsforaddingto:withtouchat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:itemsforaddingto:withtouchat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteractiondelegate/draginteraction%28_%3Aitemsforaddingto%3Awithtouchat%3A%29.json'
content_hash: 'sha256:26a8de82d28c83e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteractionDelegate](../uidraginteractiondelegate.md)

# dragInteraction(_:itemsForAddingTo:withTouchAt:)

<sub>Instance Method</sub>

Asks the delegate for the drag items to add to an in-progress drag session, in response to a user gesture to add the items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, itemsForAddingTo session: any UIDragSession, withTouchAt point: CGPoint) -> [UIDragItem]
```

## Parameters

- `interaction` — The interaction that called this method.

- `session` — The current drag session.

- `point` — The location of the user’s touch in the interaction’s view. The touch point is in the view’s coordinate system.

## Return Value

An array of drag items to add to the drag session, or an empty array if there are no items to add to the session.

## Discussion

Not implementing this method is the same as always returning an empty array.

## See Also

### Performing the drag

- [- dragInteraction:itemsForBeginningSession:](<draginteraction(__itemsforbeginning_).md>) — Asks the delegate for the array of drag items for an impending drag interaction.
- [- dragInteraction:sessionForAddingItems:withTouchAtPoint:](<draginteraction(__sessionforaddingitems_withtouchat_).md>) — Asks the delegate which drag session to add drag items to when there is more than one in-progress session.
