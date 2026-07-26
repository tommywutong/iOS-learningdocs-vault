---
title: UIPrinterPickerController.CompletionHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinterpickercontroller/completionhandler
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/completionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterpickercontroller/completionhandler.json'
content_hash: 'sha256:0c3c8d573c6e46a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinterPickerController](../uiprinterpickercontroller.md)

# UIPrinterPickerController.CompletionHandler

<sub>Type Alias</sub>

The completion handler to execute when dismissing a printer picker controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
typealias CompletionHandler = (UIPrinterPickerController, Bool, (any Error)?) -> Void
```

## Discussion

A printer picker completion handler takes the following parameters:

- **printerPickerController** — The printer picker controller object that is being dismissed. This parameter contains information about the selected printer, if any.
- **userDidSelect** — [true](../../swift/true.md) if the user selected a printer or [false](../../swift/false.md) if the user canceled the selection process. When this parameter is [true](../../swift/true.md), use the `printerPickerController` object to retrieve the selected printer object.
- **error** — An [NSError](../../foundation/nserror.md) object if there was a problem with the printer picker or `nil` if a printer was selected or the user canceled the picker.
