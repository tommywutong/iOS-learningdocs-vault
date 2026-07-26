---
title: UIPrinterPickerControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinterpickercontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterpickercontrollerdelegate.json'
content_hash: 'sha256:4a38e00fc045ca3b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPrinterPickerControllerDelegate

<sub>Protocol</sub>

A set of methods for managing the presentation and dismissal of a printer picker interface.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIPrinterPickerControllerDelegate : NSObjectProtocol
```

## Overview

You also use the methods of this protocol to influence the content displayed in the picker and to respond when the user selects a printer. Implement the methods of this protocol in your own custom object and assign that object to the delegate property of your [UIPrinterPickerController](uiprinterpickercontroller.md) object before presenting it. When you present the picker, it calls the methods of your delegate at appropriate times to ask for information or provide you with information about the state of the picker interface. For more information about presenting a printer picker interface, see [UIPrinterPickerController](uiprinterpickercontroller.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Filtering the List of Printers

- [- printerPickerController:shouldShowPrinter:](<uiprinterpickercontrollerdelegate/printerpickercontroller(__shouldshow_).md>) — Asks the delegate if the specified printer should be included in the picker.

### Handling the Printer Selection

- [- printerPickerControllerDidSelectPrinter:](<uiprinterpickercontrollerdelegate/printerpickercontrollerdidselectprinter(__).md>) — Tells the delegate that a printer was selected.

### Responding to Printer Picker Events

- [- printerPickerControllerParentViewController:](<uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller(__).md>) — Asks the delegate to provide the view controller to act as the parent of the printer picker.
- [- printerPickerControllerWillPresent:](<uiprinterpickercontrollerdelegate/printerpickercontrollerwillpresent(__).md>) — Tells the delegate that the printer picker is about to be displayed.
- [- printerPickerControllerDidPresent:](<uiprinterpickercontrollerdelegate/printerpickercontrollerdidpresent(__).md>) — Tells the delegate that the printer picker was displayed and is now visible.
- [- printerPickerControllerWillDismiss:](<uiprinterpickercontrollerdelegate/printerpickercontrollerwilldismiss(__).md>) — Tells the delegate that the printer picker is about to be dismissed.
- [- printerPickerControllerDidDismiss:](<uiprinterpickercontrollerdelegate/printerpickercontrollerdiddismiss(__).md>) — Tells the delegate that the printer picker was dismissed.

## See Also

### Managing the printer picker interface

- [delegate](uiprinterpickercontroller/delegate.md) — The delegate for the printer picker controller.
