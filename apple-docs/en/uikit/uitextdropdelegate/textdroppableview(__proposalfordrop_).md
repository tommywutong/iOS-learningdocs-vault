---
title: 'textDroppableView(_:proposalForDrop:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdropdelegate/textdroppableview(_:proposalfordrop:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:proposalfordrop:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropdelegate/textdroppableview%28_%3Aproposalfordrop%3A%29.json'
content_hash: 'sha256:72c3702eed000fc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDropDelegate](../uitextdropdelegate.md)

# textDroppableView(_:proposalForDrop:)

<sub>Instance Method</sub>

Asks the delegate if the text view can accept a drop operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, proposalForDrop drop: any UITextDropRequest) -> UITextDropProposal
```

## Parameters

- `textDroppableView` — The text view that received the drop activity.

- `drop` — The drop request.

## Return Value

A text drop proposal that specifies the behavior of the drop operation.

## Discussion

This method is called multiple times while the user performs the drag and drop activity. For instance, it’s called when the user drags items into the text view. It’s also called when the text position changes while the user drags items over the text view. If the drag session changes, which happens when the user adds more items to the drag item set, the method is called again.

Because this method is called frequently, it’s important for your implementation to do only what is necessary to return the appropriate drop proposal as quickly as possible.

## See Also

### Accepting a drop activity

- [- textDroppableView:willBecomeEditableForDrop:](<textdroppableview(__willbecomeeditablefordrop_).md>) — Asks the delegate if a noneditable text view can accept a drop operation.
