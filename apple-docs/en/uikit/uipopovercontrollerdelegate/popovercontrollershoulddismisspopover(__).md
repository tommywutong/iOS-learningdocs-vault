---
title: 'popoverControllerShouldDismissPopover(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipopovercontrollerdelegate/popovercontrollershoulddismisspopover(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/popovercontrollershoulddismisspopover(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontrollerdelegate/popovercontrollershoulddismisspopover%28_%3A%29.json'
content_hash: 'sha256:ac39e18ee2037989'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverControllerDelegate](../uipopovercontrollerdelegate.md)

# popoverControllerShouldDismissPopover(_:)

<sub>Instance Method</sub>

Asks the delegate if the popover should be dismissed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func popoverControllerShouldDismissPopover(_ popoverController: UIPopoverController) -> Bool
```

## Parameters

- `popoverController` — The popover controller to be dismissed.

## Return Value

[true](../../swift/true.md) if the popover should be dismissed or [false](../../swift/false.md) if it should remain visible.

## Discussion

This method is called in response to user-initiated attempts to dismiss the popover. It is not called when you dismiss the popover using the [- dismissPopoverAnimated:](<../uipopovercontroller/dismiss(animated_).md>) method of the popover controller.

If you do not implement this method in your delegate, the default return value is assumed to be [true](../../swift/true.md).

## See Also

### Managing the popover’s dismissal

- [- popoverControllerDidDismissPopover:](<popovercontrollerdiddismisspopover(__).md>) — Tells the delegate that the popover was dismissed. _(deprecated)_
