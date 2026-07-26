---
title: 'textDraggableView(_:itemsForDrag:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdragdelegate/textdraggableview(_:itemsfordrag:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragdelegate/textdraggableview(_:itemsfordrag:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragdelegate/textdraggableview%28_%3Aitemsfordrag%3A%29.json'
content_hash: 'sha256:80e1279a226d2316'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDragDelegate](../uitextdragdelegate.md)

# textDraggableView(_:itemsForDrag:)

<sub>Instance Method</sub>

Asks the delegate for custom drag items from a text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textDraggableView(_ textDraggableView: any UIView & UITextDraggable, itemsForDrag dragRequest: any UITextDragRequest) -> [UIDragItem]
```

## Parameters

- `textDraggableView` — The text view where the drag activity was started.

- `dragRequest` — The current drag request.

## Return Value

An array of drag items that represent the items to drag.

## Discussion

You implement this method when you need to provide custom drag items. The drag request gives you the text range of the text that is included in the drag activity. It also gives you the default drag items, which you can add to or change. If you return an empty array, the drag operation does not happen.

> [!note] Note
> This method may be called more than once. For instance, it is called each time the user adds more drag items to the session. You can detect additional calls to this method by checking the [existingItems](../uitextdragrequest/existingitems.md) property on the drag request.
