---
title: 'textDroppableView(_:previewForDroppingAllItemsWithDefault:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdropdelegate/textdroppableview(_:previewfordroppingallitemswithdefault:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:previewfordroppingallitemswithdefault:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropdelegate/textdroppableview%28_%3Apreviewfordroppingallitemswithdefault%3A%29.json'
content_hash: 'sha256:8a27e1a9eae44734'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDropDelegate](../uitextdropdelegate.md)

# textDroppableView(_:previewForDroppingAllItemsWithDefault:)

<sub>Instance Method</sub>

Asks the delegate for the preview to show during the drop animation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, previewForDroppingAllItemsWithDefault defaultPreview: UITargetedDragPreview) -> UITargetedDragPreview?
```

## Parameters

- `textDroppableView` — The text view that received the drop activity.

- `defaultPreview` — The preview that is displayed when the delegate doesn’t provide this method.

## Return Value

A target drag preview to show during the drop animation, or `nil` to show the default preview.

## Discussion

You implement this method when you want to show a nondefault preview during the drop animation. If you return `nil`, the system shows the default preview.
