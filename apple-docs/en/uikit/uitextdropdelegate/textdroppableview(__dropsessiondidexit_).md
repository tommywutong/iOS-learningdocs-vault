---
title: 'textDroppableView(_:dropSessionDidExit:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdropdelegate/textdroppableview(_:dropsessiondidexit:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:dropsessiondidexit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropdelegate/textdroppableview%28_%3Adropsessiondidexit%3A%29.json'
content_hash: 'sha256:173dc0b6fb99afb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDropDelegate](../uitextdropdelegate.md)

# textDroppableView(_:dropSessionDidExit:)

<sub>Instance Method</sub>

Tells the delegate that the user has moved the drag items out of the text view’s coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, dropSessionDidExit session: any UIDropSession)
```

## Parameters

- `textDroppableView` — The text view that received the drop activity.

- `session` — The current drop session.

## See Also

### Handling drop session notifications

- [- textDroppableView:dropSessionDidEnter:](<textdroppableview(__dropsessiondidenter_).md>) — Tells the delegate that the user has moved the drag items into the coordinate system of the text view.
- [- textDroppableView:dropSessionDidUpdate:](<textdroppableview(__dropsessiondidupdate_).md>) — Tells the delegate that the drop session has been updated.
- [- textDroppableView:dropSessionDidEnd:](<textdroppableview(__dropsessiondidend_).md>) — Tells the delegate that the drop session has ended.
