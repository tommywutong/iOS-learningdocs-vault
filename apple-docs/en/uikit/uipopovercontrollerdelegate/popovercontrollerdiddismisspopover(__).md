---
title: 'popoverControllerDidDismissPopover(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipopovercontrollerdelegate/popovercontrollerdiddismisspopover(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/popovercontrollerdiddismisspopover(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontrollerdelegate/popovercontrollerdiddismisspopover%28_%3A%29.json'
content_hash: 'sha256:dc46730d409a9616'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverControllerDelegate](../uipopovercontrollerdelegate.md)

# popoverControllerDidDismissPopover(_:)

<sub>Instance Method</sub>

Tells the delegate that the popover was dismissed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func popoverControllerDidDismissPopover(_ popoverController: UIPopoverController)
```

## Parameters

- `popoverController` — The popover controller that was dismissed.

## Discussion

The popover controller does not call this method in response to programmatic calls to the [- dismissPopoverAnimated:](<../uipopovercontroller/dismiss(animated_).md>) method. If you dismiss the popover programmatically, you should perform any cleanup actions immediately after calling the [- dismissPopoverAnimated:](<../uipopovercontroller/dismiss(animated_).md>) method.

You can use this method to incorporate any changes from the popover’s content view controller back into your application. If you do not plan to use the object in the `popoverController` parameter again, it is safe to release it from this method.

## See Also

### Managing the popover’s dismissal

- [- popoverControllerShouldDismissPopover:](<popovercontrollershoulddismisspopover(__).md>) — Asks the delegate if the popover should be dismissed. _(deprecated)_
