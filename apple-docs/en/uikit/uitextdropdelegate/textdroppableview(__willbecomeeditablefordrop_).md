---
title: 'textDroppableView(_:willBecomeEditableForDrop:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdropdelegate/textdroppableview(_:willbecomeeditablefordrop:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:willbecomeeditablefordrop:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropdelegate/textdroppableview%28_%3Awillbecomeeditablefordrop%3A%29.json'
content_hash: 'sha256:6a579ad0dd82f278'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDropDelegate](../uitextdropdelegate.md)

# textDroppableView(_:willBecomeEditableForDrop:)

<sub>Instance Method</sub>

Asks the delegate if a noneditable text view can accept a drop operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, willBecomeEditableForDrop drop: any UITextDropRequest) -> UITextDropEditability
```

## Parameters

- `textDroppableView` — The text view that received the drop activity.

- `drop` — The drop request.

## Return Value

A text drop editability style that indicates whether the text view can accept a drop operation.

## Discussion

By default, a text view that is not editable can’t accept drop requests. However, you can change this behavior by returning the editability style [UITextDropEditabilityTemporary](../uitextdropeditability/temporary.md) or [UITextDropEditabilityYes](../uitextdropeditability/yes.md) in your implementation of this method. Not implementing this method is the same as returning the [UITextDropEditabilityNo](../uitextdropeditability/no.md) style.

## See Also

### Accepting a drop activity

- [- textDroppableView:proposalForDrop:](<textdroppableview(__proposalfordrop_).md>) — Asks the delegate if the text view can accept a drop operation.
