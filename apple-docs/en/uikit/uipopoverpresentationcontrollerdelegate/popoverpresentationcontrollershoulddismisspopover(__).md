---
title: 'popoverPresentationControllerShouldDismissPopover(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollershoulddismisspopover(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollershoulddismisspopover(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollershoulddismisspopover%28_%3A%29.json'
content_hash: 'sha256:5d53f8d80bd0c5ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationControllerDelegate](../uipopoverpresentationcontrollerdelegate.md)

# popoverPresentationControllerShouldDismissPopover(_:)

<sub>Instance Method</sub>

Asks the delegate if the popover should be dismissed.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func popoverPresentationControllerShouldDismissPopover(_ popoverPresentationController: UIPopoverPresentationController) -> Bool
```

## Parameters

- `popoverPresentationController` — The popover presentation controller that is managing the popover interface.

## Return Value

[true](../../swift/true.md) if the popover should be dismissed or [false](../../swift/false.md) if it should not.

## Discussion

The popover presentation controller calls this method in response to user-initiated attempts to dismiss the popover. It is not called when you dismiss the popover programmatically using the [dismissModalViewControllerAnimated:](../uiviewcontroller/dismissmodalviewcontrolleranimated_.md) method.

If you do not implement this method in your delegate, the default return value is assumed to be [true](../../swift/true.md).

## See Also

### Presenting and dismissing the popover

- [- prepareForPopoverPresentation:](<prepareforpopoverpresentation(__).md>) — Notifies the delegate that the popover is about to be presented.
- [- popoverPresentationControllerDidDismissPopover:](<popoverpresentationcontrollerdiddismisspopover(__).md>) — Tells the delegate that the popover was dismissed. _(deprecated)_
