---
title: 'dragInteraction(_:itemsForBeginning:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraginteractiondelegate/draginteraction(_:itemsforbeginning:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:itemsforbeginning:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteractiondelegate/draginteraction%28_%3Aitemsforbeginning%3A%29.json'
content_hash: 'sha256:198aeca709c840df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteractionDelegate](../uidraginteractiondelegate.md)

# dragInteraction(_:itemsForBeginning:)

<sub>Instance Method</sub>

Asks the delegate for the array of drag items for an impending drag interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func dragInteraction(_ interaction: UIDragInteraction, itemsForBeginning session: any UIDragSession) -> [UIDragItem]
```

## Parameters

- `interaction` — The interaction asking for the drag items.

- `session` — The current drag session.

## Return Value

An array of drag items to include in the drag session, or an empty array if there are no drag items for the session.

## Discussion

As part of enabling dragging from a view, implement this method to return an array of one or more drag items. The system calls this method and uses this array to populate the drag session’s `items` property.

If the drag items represent model objects in your app that are shown in a linear order, return them in the natural first-to-last order that users expect. The system handles any order-flipping required for right-to-left scripts.

Typically, the system shows multiple dragged items as a stack of images, with the array’s first element on top. If you return an empty array, the system does not start a drag interaction.

## See Also

### Performing the drag

- [- dragInteraction:itemsForAddingToSession:withTouchAtPoint:](<draginteraction(__itemsforaddingto_withtouchat_).md>) — Asks the delegate for the drag items to add to an in-progress drag session, in response to a user gesture to add the items.
- [- dragInteraction:sessionForAddingItems:withTouchAtPoint:](<draginteraction(__sessionforaddingitems_withtouchat_).md>) — Asks the delegate which drag session to add drag items to when there is more than one in-progress session.
