---
title: 'textDroppableView(_:willPerformDrop:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdropdelegate/textdroppableview(_:willperformdrop:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:willperformdrop:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropdelegate/textdroppableview%28_%3Awillperformdrop%3A%29.json'
content_hash: 'sha256:07f0b80b62b9235c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDropDelegate](../uitextdropdelegate.md)

# textDroppableView(_:willPerformDrop:)

<sub>Instance Method</sub>

Tells the delegate that the drop operation is about to happen.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, willPerformDrop drop: any UITextDropRequest)
```

## Parameters

- `textDroppableView` — The text view that received the drop activity.

- `drop` — The drop request.

## Discussion

If you need to modify the drag items before the drop operation happens, provide the text view a [pasteDelegate](../uitextpasteconfigurationsupporting/pastedelegate.md) object that implements the [- pasteItemProviders:](<../uipasteconfigurationsupporting/paste(itemproviders_).md>) method. In the implementation, do the item conversion and paste the text.
