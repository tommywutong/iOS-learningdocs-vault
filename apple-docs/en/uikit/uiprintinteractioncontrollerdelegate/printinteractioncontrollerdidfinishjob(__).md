---
title: 'printInteractionControllerDidFinishJob(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerdidfinishjob(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerdidfinishjob(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerdidfinishjob%28_%3A%29.json'
content_hash: 'sha256:583ecdb720b67331'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionControllerDelegate](../uiprintinteractioncontrollerdelegate.md)

# printInteractionControllerDidFinishJob(_:)

<sub>Instance Method</sub>

Tells the delegate that the print job has ended.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func printInteractionControllerDidFinishJob(_ printInteractionController: UIPrintInteractionController)
```

## Parameters

- `printInteractionController` — The shared instance of [UIPrintInteractionController](../uiprintinteractioncontroller.md) that is managing the print job.

## Discussion

You can implement this method to do clean-up tasks related to the print job. This method is called after the last page of the print job is generated but before the completion handler (a block handler of type [CompletionHandler](../uiprintinteractioncontroller/completionhandler.md)) is called.

## See Also

### Responding to the Start and End of a Print Job

- [- printInteractionControllerWillStartJob:](<printinteractioncontrollerwillstartjob(__).md>) — Tells the delegate that the print job is about to start.
