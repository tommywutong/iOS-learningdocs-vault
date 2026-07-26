---
title: 'textDroppableView(_:dropSessionDidUpdate:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdropdelegate/textdroppableview(_:dropsessiondidupdate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:dropsessiondidupdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropdelegate/textdroppableview%28_%3Adropsessiondidupdate%3A%29.json'
content_hash: 'sha256:ac3000295c4fed1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDropDelegate](../uitextdropdelegate.md)

# textDroppableView(_:dropSessionDidUpdate:)

<sub>Instance Method</sub>

Tells the delegate that the drop session has been updated.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, dropSessionDidUpdate session: any UIDropSession)
```

## Parameters

- `textDroppableView` — The text view that received the drop activity.

- `session` — The current drop session.

## Discussion

The system usually—but not always—calls this method before calling the [- textDroppableView:proposalForDrop:](<textdroppableview(__proposalfordrop_).md>) method. However, it’s called frequently, so do only what is necessary in your implementation.

## See Also

### Handling drop session notifications

- [- textDroppableView:dropSessionDidEnter:](<textdroppableview(__dropsessiondidenter_).md>) — Tells the delegate that the user has moved the drag items into the coordinate system of the text view.
- [- textDroppableView:dropSessionDidExit:](<textdroppableview(__dropsessiondidexit_).md>) — Tells the delegate that the user has moved the drag items out of the text view’s coordinate system.
- [- textDroppableView:dropSessionDidEnd:](<textdroppableview(__dropsessiondidend_).md>) — Tells the delegate that the drop session has ended.
