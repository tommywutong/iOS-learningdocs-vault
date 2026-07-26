---
title: 'printInteractionControllerDidPresentPrinterOptions(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerdidpresentprinteroptions(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerdidpresentprinteroptions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerdidpresentprinteroptions%28_%3A%29.json'
content_hash: 'sha256:753a20e8f230bb67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionControllerDelegate](../uiprintinteractioncontrollerdelegate.md)

# printInteractionControllerDidPresentPrinterOptions(_:)

<sub>Instance Method</sub>

Tells the delegate that the device has presented the printing-options user interface.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func printInteractionControllerDidPresentPrinterOptions(_ printInteractionController: UIPrintInteractionController)
```

## Parameters

- `printInteractionController` — The shared instance of [UIPrintInteractionController](../uiprintinteractioncontroller.md) that is managing the print job.

## See Also

### Responding to the Presentation and Dismissal of the Printing Interface

- [- printInteractionControllerWillPresentPrinterOptions:](<printinteractioncontrollerwillpresentprinteroptions(__).md>) — Tells the delegate that the device is about to display the printing-options user interface.
- [- printInteractionControllerWillDismissPrinterOptions:](<printinteractioncontrollerwilldismissprinteroptions(__).md>) — Tells the delegate that the device is about to dismiss the printing-options user interface.
- [- printInteractionControllerDidDismissPrinterOptions:](<printinteractioncontrollerdiddismissprinteroptions(__).md>) — Tells the delegate that the device is dismissing the printing-options user interface.
