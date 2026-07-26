---
title: UIPrintInteractionControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinteractioncontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontrollerdelegate.json'
content_hash: 'sha256:1e1288bd51597a6b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPrintInteractionControllerDelegate

<sub>Protocol</sub>

An optional set of methods that the delegate of the shared print-interaction controller implements.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIPrintInteractionControllerDelegate : NSObjectProtocol
```

## Overview

If the application has special requirements for content sizes, it can implement [- printInteractionController:choosePaper:](<uiprintinteractioncontrollerdelegate/printinteractioncontroller(__choosepaper_).md>) to return a [UIPrintPaper](uiprintpaper.md) object encapsulating the page size and the printing area to use for a print job. If you want more control of the presentation of the printing options, the delegate can return a view controller that owns the printing-options view in an implementation of [- printInteractionControllerParentViewController:](<uiprintinteractioncontrollerdelegate/printinteractioncontrollerparentviewcontroller(__).md>). The delegate can also implement methods that are invoked when the printing user interface is presented and when it is dismissed, and when the print job begins and ends.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Returning a Parent View Controller

- [- printInteractionControllerParentViewController:](<uiprintinteractioncontrollerdelegate/printinteractioncontrollerparentviewcontroller(__).md>) — Returns a parent view controller for managing the printing-options view.

### Choosing a Paper Size for the Print Job

- [- printInteractionController:choosePaper:](<uiprintinteractioncontrollerdelegate/printinteractioncontroller(__choosepaper_).md>) — Asks the delegate for an object that encapsulates the paper size and printing area for the print job.
- [- printInteractionController:cutLengthForPaper:](<uiprintinteractioncontrollerdelegate/printinteractioncontroller(__cutlengthfor_).md>) — Asks the delegate for a length to use when cutting the page.
- [- printInteractionController:chooseCutterBehavior:](<uiprintinteractioncontrollerdelegate/printinteractioncontroller(__choosecutterbehavior_).md>) — Asks the delegate for the cutter behavior for the print job.

### Responding to the Presentation and Dismissal of the Printing Interface

- [- printInteractionControllerWillPresentPrinterOptions:](<uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillpresentprinteroptions(__).md>) — Tells the delegate that the device is about to display the printing-options user interface.
- [- printInteractionControllerDidPresentPrinterOptions:](<uiprintinteractioncontrollerdelegate/printinteractioncontrollerdidpresentprinteroptions(__).md>) — Tells the delegate that the device has presented the printing-options user interface.
- [- printInteractionControllerWillDismissPrinterOptions:](<uiprintinteractioncontrollerdelegate/printinteractioncontrollerwilldismissprinteroptions(__).md>) — Tells the delegate that the device is about to dismiss the printing-options user interface.
- [- printInteractionControllerDidDismissPrinterOptions:](<uiprintinteractioncontrollerdelegate/printinteractioncontrollerdiddismissprinteroptions(__).md>) — Tells the delegate that the device is dismissing the printing-options user interface.

### Responding to the Start and End of a Print Job

- [- printInteractionControllerWillStartJob:](<uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob(__).md>) — Tells the delegate that the print job is about to start.
- [- printInteractionControllerDidFinishJob:](<uiprintinteractioncontrollerdelegate/printinteractioncontrollerdidfinishjob(__).md>) — Tells the delegate that the print job has ended.

### Constants

- [CutterBehavior](uiprinter/cutterbehavior.md) — Constants that specify the cutter behavior of a roll-fed printer.

## See Also

### Assigning the delegate

- [delegate](uiprintinteractioncontroller/delegate.md) — The delegate of the print-interaction controller.
