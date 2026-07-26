---
title: 'present(from:in:animated:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprinterpickercontroller/present(from:in:animated:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/present(from:in:animated:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterpickercontroller/present%28from%3Ain%3Aanimated%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:fc424bdfd4e5b2bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinterPickerController](../uiprinterpickercontroller.md)

# present(from:in:animated:completionHandler:)

<sub>Instance Method</sub>

Presents the picker in a popover that anchors to a rectangle in the specified view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func present(from rect: CGRect, in view: UIView, animated: Bool, completionHandler completion: UIPrinterPickerController.CompletionHandler? = nil) -> Bool
```

## Parameters

- `rect` — The rectangle to which to anchor the popover. Specify the rectangle using the coordinate system of the view in the `view` parameter.

- `view` — The view containing the specified rectangle.

- `animated` — [true](../../swift/true.md) to animate the display of the picker or [false](../../swift/false.md) to display it without animations.

- `completion` — A block to execute when the picker is dismissed. Use this block to receive information about the selected printer or information about any errors that occurred.

## Return Value

[true](../../swift/true.md) if the picker was displayed or [false](../../swift/false.md) if the picker was already visible.

## Discussion

This method presents the picker from a popover or from the view controller you specify using your delegate object. If you provide a delegate object and that object implements the [- printerPickerControllerParentViewController:](<../uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller(__).md>) method, UIKit presents the picker using the view controller you specify. If you do not provide a delegate, or your delegate object does not implement the [- printerPickerControllerParentViewController:](<../uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller(__).md>) method, UIKit presents the picker using a popover attached the view you specified.

After presenting the picker, the picker interface runs until the user or your app dismisses it. The picker interface provides ways for the user to cancel printing directly, all of which dismiss the picker. You can also dismiss the printer picker programmatically by calling the [- dismissAnimated:](<dismiss(animated_).md>) method.

Calling this method while the picker is currently displayed in a popover dismisses the popover.

## See Also

### Presenting and dismissing the picker

- [- presentAnimated:completionHandler:](<present(animated_completionhandler_).md>) — Presents the picker from a view controller of your app.
- [- presentFromBarButtonItem:animated:completionHandler:](<present(from_animated_completionhandler_).md>) — Presents the picker in a popover that anchors to the specified bar button item.
- [- dismissAnimated:](<dismiss(animated_).md>) — Dismisses the picker.
