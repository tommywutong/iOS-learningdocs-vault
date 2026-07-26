---
title: 'printerPickerControllerParentViewController(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller%28_%3A%29.json'
content_hash: 'sha256:15e90761548c9861'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinterPickerControllerDelegate](../uiprinterpickercontrollerdelegate.md)

# printerPickerControllerParentViewController(_:)

<sub>Instance Method</sub>

Asks the delegate to provide the view controller to act as the parent of the printer picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func printerPickerControllerParentViewController(_ printerPickerController: UIPrinterPickerController) -> UIViewController?
```

## Parameters

- `printerPickerController` — The printer picker controller object that made the request.

## Return Value

A view controller from your app’s interface.

## Discussion

Use this method when you want the printer picker controller to be presented from a specific view controller in your app’s interface. When you specify a navigation controller as the parent, UIKit pushes the printer picker onto your navigation stack. For other types of view controllers, UIKit presents the picker interface from the view controller you specify.

If you do not implement this method or your implementation returns `nil`, UIKit presents the printer picker from the root view controller of your app’s main window.

## See Also

### Responding to Printer Picker Events

- [- printerPickerControllerWillPresent:](<printerpickercontrollerwillpresent(__).md>) — Tells the delegate that the printer picker is about to be displayed.
- [- printerPickerControllerDidPresent:](<printerpickercontrollerdidpresent(__).md>) — Tells the delegate that the printer picker was displayed and is now visible.
- [- printerPickerControllerWillDismiss:](<printerpickercontrollerwilldismiss(__).md>) — Tells the delegate that the printer picker is about to be dismissed.
- [- printerPickerControllerDidDismiss:](<printerpickercontrollerdiddismiss(__).md>) — Tells the delegate that the printer picker was dismissed.
