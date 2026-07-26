---
title: 'textDraggableView(_:dragSessionWillBegin:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdragdelegate/textdraggableview(_:dragsessionwillbegin:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragdelegate/textdraggableview(_:dragsessionwillbegin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragdelegate/textdraggableview%28_%3Adragsessionwillbegin%3A%29.json'
content_hash: 'sha256:c05f00dd8d281b4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDragDelegate](../uitextdragdelegate.md)

# textDraggableView(_:dragSessionWillBegin:)

<sub>Instance Method</sub>

Tells the delegate that the text has been lifted out of the text view and the user is beginning to drag the text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textDraggableView(_ textDraggableView: any UIView & UITextDraggable, dragSessionWillBegin session: any UIDragSession)
```

## Parameters

- `textDraggableView` — The text view where the drag activity was started.

- `session` — The drag session of the current drag activity.

## See Also

### Handling drag session notifications

- [- textDraggableView:dragSessionDidEnd:withOperation:](<textdraggableview(__dragsessiondidend_with_).md>) — Tells the delegate that the drag session has ended.
