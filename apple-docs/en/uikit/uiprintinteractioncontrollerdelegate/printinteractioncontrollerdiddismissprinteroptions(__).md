---
title: 'printInteractionControllerDidDismissPrinterOptions(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerdiddismissprinteroptions(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerdiddismissprinteroptions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerdiddismissprinteroptions%28_%3A%29.json'
content_hash: 'sha256:62f6d873a87dd37d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionControllerDelegate](../uiprintinteractioncontrollerdelegate.md)

# printInteractionControllerDidDismissPrinterOptions(_:)

<sub>Instance Method</sub>

Tells the delegate that the device is dismissing the printing-options user interface.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func printInteractionControllerDidDismissPrinterOptions(_ printInteractionController: UIPrintInteractionController)
```

## Parameters

- `printInteractionController` — The shared instance of [UIPrintInteractionController](../uiprintinteractioncontroller.md) that is managing the print job.

## Discussion

This message is sent both when the user taps Print on the printing-options view and when the user dismisses the view by tapping outside it.

## See Also

### Responding to the Presentation and Dismissal of the Printing Interface

- [- printInteractionControllerWillPresentPrinterOptions:](<printinteractioncontrollerwillpresentprinteroptions(__).md>) — Tells the delegate that the device is about to display the printing-options user interface.
- [- printInteractionControllerDidPresentPrinterOptions:](<printinteractioncontrollerdidpresentprinteroptions(__).md>) — Tells the delegate that the device has presented the printing-options user interface.
- [- printInteractionControllerWillDismissPrinterOptions:](<printinteractioncontrollerwilldismissprinteroptions(__).md>) — Tells the delegate that the device is about to dismiss the printing-options user interface.
