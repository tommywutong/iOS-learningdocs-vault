---
title: 'dismiss(animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprinterpickercontroller/dismiss(animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/dismiss(animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterpickercontroller/dismiss%28animated%3A%29.json'
content_hash: 'sha256:a7698f5e931c5dd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinterPickerController](../uiprinterpickercontroller.md)

# dismiss(animated:)

<sub>Instance Method</sub>

Dismisses the picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func dismiss(animated: Bool)
```

## Parameters

- `animated` — [true](../../swift/true.md) to animate the dismissal of the picker or [false](../../swift/false.md) to remove it without animations.

## Discussion

This method dismisses a picker that you previously presented. When using this method to dismiss a picker, the picker does not call the [- printerPickerControllerWillDismiss:](<../uiprinterpickercontrollerdelegate/printerpickercontrollerwilldismiss(__).md>) or [- printerPickerControllerDidDismiss:](<../uiprinterpickercontrollerdelegate/printerpickercontrollerdiddismiss(__).md>) methods of your delegate object.

User interactions with the picker can also dismiss the picker automatically. For example, if the user selects a printer or cancels the picker, the picker dismisses itself automatically. Use this method to dismiss a picker programmatically in response to other events in your app.

## See Also

### Presenting and dismissing the picker

- [- presentAnimated:completionHandler:](<present(animated_completionhandler_).md>) — Presents the picker from a view controller of your app.
- [- presentFromBarButtonItem:animated:completionHandler:](<present(from_animated_completionhandler_).md>) — Presents the picker in a popover that anchors to the specified bar button item.
- [- presentFromRect:inView:animated:completionHandler:](<present(from_in_animated_completionhandler_).md>) — Presents the picker in a popover that anchors to a rectangle in the specified view.
