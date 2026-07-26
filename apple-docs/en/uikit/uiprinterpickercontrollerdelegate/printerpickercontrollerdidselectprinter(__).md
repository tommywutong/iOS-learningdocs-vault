---
title: 'printerPickerControllerDidSelectPrinter(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerdidselectprinter(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerdidselectprinter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerdidselectprinter%28_%3A%29.json'
content_hash: 'sha256:f587e90ac741684e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinterPickerControllerDelegate](../uiprinterpickercontrollerdelegate.md)

# printerPickerControllerDidSelectPrinter(_:)

<sub>Instance Method</sub>

Tells the delegate that a printer was selected.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func printerPickerControllerDidSelectPrinter(_ printerPickerController: UIPrinterPickerController)
```

## Parameters

- `printerPickerController` — The printer picker controller that is providing your delegate with information.

## Discussion

Implement this method if you want your delegate to be notified of the selected printer. The selected printer can be either one that the user selected or the initially selected printer that you specified when creating your [UIPrinterPickerController](../uiprinterpickercontroller.md) object.
