---
title: UIPrintInteractionController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinteractioncontroller
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller.json'
content_hash: 'sha256:c71413a574f1b593'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPrintInteractionController

<sub>Class</sub>

A user interface that manages the printing of documents, images, and other printable content in iOS.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPrintInteractionController
```

## Overview

[UIPrintInteractionController](uiprintinteractioncontroller.md) is the central class for printing in iOS. The shared instance of it represents a print job. A print job includes the content to print and information and options related to its printing, such as output type, job name, paper size, and orientation.

[UIPrintInteractionController](uiprintinteractioncontroller.md) has four mutually exclusive properties for giving it the content to print:

- [printingItem](uiprintinteractioncontroller/printingitem.md) takes a single print-ready object.
- [printingItems](uiprintinteractioncontroller/printingitems.md) takes an array of print-ready objects.
- [printFormatter](uiprintinteractioncontroller/printformatter.md) takes a print formatter, an object that knows how to lay out content of a certain type.
- [printPageRenderer](uiprintinteractioncontroller/printpagerenderer.md) takes a page renderer, a custom object that draws the content for printing.

If the [showsPageRange](uiprintinteractioncontroller/showspagerange.md) property is [true](../swift/true.md), the number of pages is more than 1, and you assign an object to any of these properties except for the [printingItems](uiprintinteractioncontroller/printingitems.md) property, the printing options include a control that allows users to select a page range.

When users tap a print button on the app’s user interface, a controller object of the app should respond to the action message by obtaining the shared instance of [UIPrintInteractionController](uiprintinteractioncontroller.md) and preparing it for the print job. When the app calls one of the `present...` methods (for example, [- presentAnimated:completionHandler:](<uiprintinteractioncontroller/present(animated_completionhandler_).md>)), [UIPrintInteractionController](uiprintinteractioncontroller.md) displays a view containing printing options. This interface is simple, allowing users to select a printer, specify the number of copies and possibly a range of pages, and choose single-sided or double-sided printing (if the printer supports duplex printing). When users make their selections and tap Print, the print job begins.

For design guidance, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/system-capabilities/printing/).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Getting the shared controller instance

- [sharedPrintController](uiprintinteractioncontroller/shared.md) — The shared print-interaction controller object.

### Assigning the delegate

- [delegate](uiprintinteractioncontroller/delegate.md) — The delegate of the print-interaction controller.
- [UIPrintInteractionControllerDelegate](uiprintinteractioncontrollerdelegate.md) — An optional set of methods that the delegate of the shared print-interaction controller implements.

### Determining printability

- [printingAvailable](uiprintinteractioncontroller/isprintingavailable.md) — A Boolean value that indicates whether the device supports printing.
- [+ canPrintData:](<uiprintinteractioncontroller/canprint(__)-4e0bs.md>) — Returns a Boolean value that indicates whether UIKit can print the contents of a data object.
- [+ canPrintURL:](<uiprintinteractioncontroller/canprint(__)-364vj.md>) — Returns a Boolean value that indicates whether UIKit can print the file that the specified URL references.
- [printableUTIs](uiprintinteractioncontroller/printableutis.md) — Returns a set of the Uniform Type Identifiers for the types of data that UIKit can print.

### Providing the source of printable content

- [printingItem](uiprintinteractioncontroller/printingitem.md) — A single ready-to-print object.
- [printingItems](uiprintinteractioncontroller/printingitems.md) — An array of ready-to-print objects.
- [printPageRenderer](uiprintinteractioncontroller/printpagerenderer.md) — An object that draws pages of printable content when UIKit requests it.
- [printFormatter](uiprintinteractioncontroller/printformatter.md) — An object that lays out the content of pages according to the kind of content.

### Presenting the printing user interface

- [- presentAnimated:completionHandler:](<uiprintinteractioncontroller/present(animated_completionhandler_).md>) — Presents the iPhone printing user interface in a sheet, optionally animating it to slide up from the bottom of the screen.
- [- presentFromBarButtonItem:animated:completionHandler:](<uiprintinteractioncontroller/present(from_animated_completionhandler_).md>) — Presents the iPad printing user interface in a popover view, optionally animating it from a bar-button item.
- [- presentFromRect:inView:animated:completionHandler:](<uiprintinteractioncontroller/present(from_in_animated_completionhandler_).md>) — Presents the iPad printing user interface in a popover view, optionally animating it from any area in a view.
- [- dismissAnimated:](<uiprintinteractioncontroller/dismiss(animated_).md>) — Dismisses the printing-options sheet or popover.

### Printing directly to a printer

- [- printToPrinter:completionHandler:](<uiprintinteractioncontroller/print(to_completionhandler_).md>) — Prints directly to the specified printer.
- [CompletionHandler](uiprintinteractioncontroller/completionhandler.md) — A completion handler for responding to the completion of a print job or for handling printing errors.

### Accessing print-job information

- [printInfo](uiprintinteractioncontroller/printinfo.md) — An object that encapsulates information about the print job.
- [printPaper](uiprintinteractioncontroller/printpaper.md) — An object that represents the paper size and printing area for the print job.
- [showsNumberOfCopies](uiprintinteractioncontroller/showsnumberofcopies.md) — A Boolean value that determines whether the printing options include the number of copies.
- [showsPaperSelectionForLoadedPapers](uiprintinteractioncontroller/showspaperselectionforloadedpapers.md) — A Boolean value that determines whether the paper selection menu displays.
- [showsPaperOrientation](uiprintinteractioncontroller/showspaperorientation.md) — A Boolean value that indicates whether the printing options include the paper-orientation control.
- [showsPageRange](uiprintinteractioncontroller/showspagerange.md) — A Boolean value that determines whether the printing options include a page-range control. _(deprecated)_

### Handling printing errors

- [UIPrintErrorDomain](uiprinterrordomain.md) — The string constant that defines the UIKit printing error domain.
- [UIPrintError](uiprinterror.md) — A structure that contains information about a printing error.
- [Code](uiprinterror/code.md) — Constants that specify the print error code.

## See Also

### Print panels

- [UIPrinterPickerController](uiprinterpickercontroller.md) — A view controller that displays the standard interface for selecting a printer.
