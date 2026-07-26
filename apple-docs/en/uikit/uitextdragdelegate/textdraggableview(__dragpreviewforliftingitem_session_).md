---
title: 'textDraggableView(_:dragPreviewForLiftingItem:session:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdragdelegate/textdraggableview(_:dragpreviewforliftingitem:session:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragdelegate/textdraggableview(_:dragpreviewforliftingitem:session:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragdelegate/textdraggableview%28_%3Adragpreviewforliftingitem%3Asession%3A%29.json'
content_hash: 'sha256:d263856cdeadb309'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDragDelegate](../uitextdragdelegate.md)

# textDraggableView(_:dragPreviewForLiftingItem:session:)

<sub>Instance Method</sub>

Asks the delegate for the preview to show during the lift animation that happens when a user begins to drag an item from a text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textDraggableView(_ textDraggableView: any UIView & UITextDraggable, dragPreviewForLiftingItem item: UIDragItem, session: any UIDragSession) -> UITargetedDragPreview?
```

## Parameters

- `textDraggableView` — The text view where the drag activity was started.

- `item` — The drag item that is being lifted.

- `session` — The drag session of the current drag activity.

## Return Value

A targeted drag preview to show during the lift animation, or `nil` to show the default preview.

## Discussion

You implement this method when you want to show a nondefault preview during the lift animation. If you return `nil`, the system shows default preview.

> [!note] Note
> This method is not called when the [suggestedItems](../uitextdragrequest/suggesteditems.md) array for the text drag request contains the drag item.
