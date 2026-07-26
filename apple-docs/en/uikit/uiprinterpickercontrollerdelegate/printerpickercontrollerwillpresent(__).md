---
title: 'printerPickerControllerWillPresent(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerwillpresent(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerwillpresent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerwillpresent%28_%3A%29.json'
content_hash: 'sha256:ced81d7a161bbad1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinterPickerControllerDelegate](../uiprinterpickercontrollerdelegate.md)

# printerPickerControllerWillPresent(_:)

<sub>Instance Method</sub>

Tells the delegate that the printer picker is about to be displayed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func printerPickerControllerWillPresent(_ printerPickerController: UIPrinterPickerController)
```

## Parameters

- `printerPickerController` — The printer picker controller object being displayed.

## Discussion

Use this method to perform any tasks associated with displaying the printer picker controller.

## See Also

### Responding to Printer Picker Events

- [- printerPickerControllerParentViewController:](<printerpickercontrollerparentviewcontroller(__).md>) — Asks the delegate to provide the view controller to act as the parent of the printer picker.
- [- printerPickerControllerDidPresent:](<printerpickercontrollerdidpresent(__).md>) — Tells the delegate that the printer picker was displayed and is now visible.
- [- printerPickerControllerWillDismiss:](<printerpickercontrollerwilldismiss(__).md>) — Tells the delegate that the printer picker is about to be dismissed.
- [- printerPickerControllerDidDismiss:](<printerpickercontrollerdiddismiss(__).md>) — Tells the delegate that the printer picker was dismissed.
