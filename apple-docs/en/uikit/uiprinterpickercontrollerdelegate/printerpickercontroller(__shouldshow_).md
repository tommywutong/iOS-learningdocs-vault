---
title: 'printerPickerController(_:shouldShow:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontroller(_:shouldshow:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontroller(_:shouldshow:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontroller%28_%3Ashouldshow%3A%29.json'
content_hash: 'sha256:54d2880f9f6831de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinterPickerControllerDelegate](../uiprinterpickercontrollerdelegate.md)

# printerPickerController(_:shouldShow:)

<sub>Instance Method</sub>

Asks the delegate if the specified printer should be included in the picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func printerPickerController(_ printerPickerController: UIPrinterPickerController, shouldShow printer: UIPrinter) -> Bool
```

## Parameters

- `printerPickerController` — The printer picker controller that is asking the delegate for information.

- `printer` — The printer object for the delegate to consider.

## Return Value

[true](../../swift/true.md) if the printer should be displayed or [false](../../swift/false.md) if it should not.

## Discussion

Implement this method in your delegate if you want to filter the list of printers displayed by the printer picker interface. You might use this method to display only printers with specific capabilities. The printer picker interface calls this method once for each printer it is preparing to display, so your implementation should perform any required checks and return as quickly as possible. Do not perform any lengthy operations in this method.

If you do not implement this method, the picker interface displays all of the printers that it finds.
