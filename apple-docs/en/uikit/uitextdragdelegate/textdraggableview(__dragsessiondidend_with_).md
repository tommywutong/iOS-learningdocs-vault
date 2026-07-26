---
title: 'textDraggableView(_:dragSessionDidEnd:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdragdelegate/textdraggableview(_:dragsessiondidend:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragdelegate/textdraggableview(_:dragsessiondidend:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragdelegate/textdraggableview%28_%3Adragsessiondidend%3Awith%3A%29.json'
content_hash: 'sha256:99979e3e9d7b1779'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDragDelegate](../uitextdragdelegate.md)

# textDraggableView(_:dragSessionDidEnd:with:)

<sub>Instance Method</sub>

Tells the delegate that the drag session has ended.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textDraggableView(_ textDraggableView: any UIView & UITextDraggable, dragSessionDidEnd session: any UIDragSession, with operation: UIDropOperation)
```

## Parameters

- `textDraggableView` — The text view where the drag activity was started.

- `session` — The drag session of the current drag activity.

- `operation` — The operation that occurred during the drop activity.

## See Also

### Handling drag session notifications

- [- textDraggableView:dragSessionWillBegin:](<textdraggableview(__dragsessionwillbegin_).md>) — Tells the delegate that the text has been lifted out of the text view and the user is beginning to drag the text.
