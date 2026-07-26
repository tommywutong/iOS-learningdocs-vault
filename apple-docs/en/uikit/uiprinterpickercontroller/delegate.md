---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinterpickercontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterpickercontroller/delegate.json'
content_hash: 'sha256:5c7e3a2c7949f183'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinterPickerController](../uiprinterpickercontroller.md)

# delegate

<sub>Instance Property</sub>

The delegate for the printer picker controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIPrinterPickerControllerDelegate)? { get set }
```

## Discussion

Use the delegate object to filter out printers from the displayed list and to respond to events that occur during the presentation of the printer picker. The object you assign to this property must conform to the [UIPrinterPickerControllerDelegate](../uiprinterpickercontrollerdelegate.md) protocol.

## See Also

### Managing the printer picker interface

- [UIPrinterPickerControllerDelegate](../uiprinterpickercontrollerdelegate.md) — A set of methods for managing the presentation and dismissal of a printer picker interface.
