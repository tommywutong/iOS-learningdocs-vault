---
title: 'printInteractionController(_:chooseCutterBehavior:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:choosecutterbehavior:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:choosecutterbehavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontroller%28_%3Achoosecutterbehavior%3A%29.json'
content_hash: 'sha256:74308463f2e16b3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionControllerDelegate](../uiprintinteractioncontrollerdelegate.md)

# printInteractionController(_:chooseCutterBehavior:)

<sub>Instance Method</sub>

Asks the delegate for the cutter behavior for the print job.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, chooseCutterBehavior availableBehaviors: [Any]) -> UIPrinter.CutterBehavior
```

## Parameters

- `printInteractionController` — The shared instance of [UIPrintInteractionController](../uiprintinteractioncontroller.md) that is managing the print job.

- `availableBehaviors` — An array of [NSNumber](../../foundation/nsnumber.md) objects identifying the printer’s available cutter behaviors. Each number corresponds to one of the constants defined in [CutterBehavior](../uiprinter/cutterbehavior.md).

## Return Value

The cutter behavior to use for the print job. The value must correspond to one of the constants in the `availableBehaviors` parameter.

## Discussion

Some roll-fed printers support different options for cutting the paper. If you implement this method in your delegate, then it may be called during a print job. Your delegate method should determine when to make cuts and return the appropriate value.

## See Also

### Choosing a Paper Size for the Print Job

- [- printInteractionController:choosePaper:](<printinteractioncontroller(__choosepaper_).md>) — Asks the delegate for an object that encapsulates the paper size and printing area for the print job.
- [- printInteractionController:cutLengthForPaper:](<printinteractioncontroller(__cutlengthfor_).md>) — Asks the delegate for a length to use when cutting the page.
