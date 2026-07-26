---
title: UIPrinterPickerController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinterpickercontroller
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterpickercontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterpickercontroller.json'
content_hash: 'sha256:777c13bef72f1a55'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPrinterPickerController

<sub>Class</sub>

A view controller that displays the standard interface for selecting a printer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPrinterPickerController
```

## Overview

You can use a printer picker controller to display a list of printers to the user prior to printing a document, photo, or other content. Printer pickers display all pickers normally but you can filter out printers by assigning an appropriate delegate object to the picker before displaying it.

A printer picker controller coordinates the presentation and dismissal of its interface with its associated delegate object. The delegate object is an object that you provide and that conforms to the [UIPrinterPickerControllerDelegate](uiprinterpickercontrollerdelegate.md) protocol. When the user selects a printer, the picker also notifies the delegate of the selection.

A printer picker controller isn’t a view controller, so you don’t present it the way you do other view controllers. You present the picker using one of the presentation methods of this class. Those methods work with the picker’s delegate object to determine the most appropriate way to present the picker. If the delegate implements the [- printerPickerControllerParentViewController:](<uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller(__).md>) method, the picker presents itself using the view controller returned by that method. Some presentation methods may present the picker using a popover instead.

For more information about the picker delegate methods, see [UIPrinterPickerControllerDelegate](uiprinterpickercontrollerdelegate.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a picker controller

- [+ printerPickerControllerWithInitiallySelectedPrinter:](<uiprinterpickercontroller/init(initiallyselectedprinter_).md>) — Creates and returns a printer picker with an initially selected printer object.

### Managing the printer picker interface

- [delegate](uiprinterpickercontroller/delegate.md) — The delegate for the printer picker controller.
- [UIPrinterPickerControllerDelegate](uiprinterpickercontrollerdelegate.md) — A set of methods for managing the presentation and dismissal of a printer picker interface.

### Presenting and dismissing the picker

- [- presentAnimated:completionHandler:](<uiprinterpickercontroller/present(animated_completionhandler_).md>) — Presents the picker from a view controller of your app.
- [- presentFromBarButtonItem:animated:completionHandler:](<uiprinterpickercontroller/present(from_animated_completionhandler_).md>) — Presents the picker in a popover that anchors to the specified bar button item.
- [- presentFromRect:inView:animated:completionHandler:](<uiprinterpickercontroller/present(from_in_animated_completionhandler_).md>) — Presents the picker in a popover that anchors to a rectangle in the specified view.
- [- dismissAnimated:](<uiprinterpickercontroller/dismiss(animated_).md>) — Dismisses the picker.

### Getting the selected printer

- [selectedPrinter](uiprinterpickercontroller/selectedprinter.md) — The selected printer.

### Constants

- [CompletionHandler](uiprinterpickercontroller/completionhandler.md) — The completion handler to execute when dismissing a printer picker controller.

## See Also

### Print panels

- [UIPrintInteractionController](uiprintinteractioncontroller.md) — A user interface that manages the printing of documents, images, and other printable content in iOS.
