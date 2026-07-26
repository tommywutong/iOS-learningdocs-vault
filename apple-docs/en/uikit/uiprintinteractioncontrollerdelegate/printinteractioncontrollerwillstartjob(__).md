---
title: 'printInteractionControllerWillStartJob(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob%28_%3A%29.json'
content_hash: 'sha256:057c42920246be92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionControllerDelegate](../uiprintinteractioncontrollerdelegate.md)

# printInteractionControllerWillStartJob(_:)

<sub>Instance Method</sub>

Tells the delegate that the print job is about to start.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func printInteractionControllerWillStartJob(_ printInteractionController: UIPrintInteractionController)
```

## Parameters

- `printInteractionController` — The shared instance of [UIPrintInteractionController](../uiprintinteractioncontroller.md) that is managing the print job.

## Discussion

You can implement this method to do set-up tasks related to the print job. For example, an application that needs to do intensive rendering could implement this method to pause animations. This method is called before drawing begins but after the printing user interface is dismissed.

## See Also

### Related Documentation

- [- printInteractionControllerDidDismissPrinterOptions:](<printinteractioncontrollerdiddismissprinteroptions(__).md>) — Tells the delegate that the device is dismissing the printing-options user interface.

### Responding to the Start and End of a Print Job

- [- printInteractionControllerDidFinishJob:](<printinteractioncontrollerdidfinishjob(__).md>) — Tells the delegate that the print job has ended.
