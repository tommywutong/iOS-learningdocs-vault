---
title: 'print(to:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontroller/print(to:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/print(to:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/print%28to%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:57f3c5877b203ec8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# print(to:completionHandler:)

<sub>Instance Method</sub>

Prints directly to the specified printer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func print(to printer: UIPrinter, completionHandler completion: UIPrintInteractionController.CompletionHandler? = nil) -> Bool
```

## Parameters

- `printer` — The printer to use for printing. You can obtain a list of available printers using a [UIPrinterPickerController](../uiprinterpickercontroller.md) object.

- `completion` — The block to execute when the print operation finishes.

## Return Value

[true](../../swift/true.md) if printing was successful or [false](../../swift/false.md) if there was a problem.

## Discussion

This method starts the print job and displays the printing progress indicator to the user. This method associates the current printing information (available in the [printInfo](printinfo.md) property) with the job but disables duplex printing. Upon completion of the print job, the print interaction controller executes the block in the `completion` parameter.

## See Also

### Printing directly to a printer

- [CompletionHandler](completionhandler.md) — A completion handler for responding to the completion of a print job or for handling printing errors.
