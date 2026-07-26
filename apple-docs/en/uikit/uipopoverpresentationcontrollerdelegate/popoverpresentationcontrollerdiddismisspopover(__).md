---
title: 'popoverPresentationControllerDidDismissPopover(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollerdiddismisspopover(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollerdiddismisspopover(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollerdiddismisspopover%28_%3A%29.json'
content_hash: 'sha256:00174c350292e302'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationControllerDelegate](../uipopoverpresentationcontrollerdelegate.md)

# popoverPresentationControllerDidDismissPopover(_:)

<sub>Instance Method</sub>

Tells the delegate that the popover was dismissed.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func popoverPresentationControllerDidDismissPopover(_ popoverPresentationController: UIPopoverPresentationController)
```

## Parameters

- `popoverPresentationController` — The popover presentation controller that is managing the popover interface.

## Discussion

The popover presentation controller calls this method after dismissing the popover to let you know that it is no longer onscreen. The presentation controller calls this method only in response to user actions. It does not call this method if you dismiss the popover programmatically.

Use this method to incorporate any changes from the popover’s content view controller back into your app.

## See Also

### Presenting and dismissing the popover

- [- prepareForPopoverPresentation:](<prepareforpopoverpresentation(__).md>) — Notifies the delegate that the popover is about to be presented.
- [- popoverPresentationControllerShouldDismissPopover:](<popoverpresentationcontrollershoulddismisspopover(__).md>) — Asks the delegate if the popover should be dismissed. _(deprecated)_
