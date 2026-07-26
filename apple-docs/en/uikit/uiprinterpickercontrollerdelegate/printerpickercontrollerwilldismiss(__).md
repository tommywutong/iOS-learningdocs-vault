---
title: 'printerPickerControllerWillDismiss(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerwilldismiss(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerwilldismiss(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerwilldismiss%28_%3A%29.json'
content_hash: 'sha256:ade68b6882605ff8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinterPickerControllerDelegate](../uiprinterpickercontrollerdelegate.md)

# printerPickerControllerWillDismiss(_:)

<sub>Instance Method</sub>

Tells the delegate that the printer picker is about to be dismissed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func printerPickerControllerWillDismiss(_ printerPickerController: UIPrinterPickerController)
```

## Parameters

- `printerPickerController` — The printer picker controller object being dismissed.

## Discussion

Use this method to perform any tasks associated with displaying the printer picker controller.

This method is called when the user dismisses the picker, either by selecting a printer or by canceling the picker interface. This method is not called when you dismiss the picker programmatically using the [- dismissAnimated:](<../uiprinterpickercontroller/dismiss(animated_).md>) method.

## See Also

### Responding to Printer Picker Events

- [- printerPickerControllerParentViewController:](<printerpickercontrollerparentviewcontroller(__).md>) — Asks the delegate to provide the view controller to act as the parent of the printer picker.
- [- printerPickerControllerWillPresent:](<printerpickercontrollerwillpresent(__).md>) — Tells the delegate that the printer picker is about to be displayed.
- [- printerPickerControllerDidPresent:](<printerpickercontrollerdidpresent(__).md>) — Tells the delegate that the printer picker was displayed and is now visible.
- [- printerPickerControllerDidDismiss:](<printerpickercontrollerdiddismiss(__).md>) — Tells the delegate that the printer picker was dismissed.
