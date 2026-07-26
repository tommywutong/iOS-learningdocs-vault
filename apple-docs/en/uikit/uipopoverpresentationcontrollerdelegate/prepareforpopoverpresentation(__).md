---
title: 'prepareForPopoverPresentation(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipopoverpresentationcontrollerdelegate/prepareforpopoverpresentation(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate/prepareforpopoverpresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontrollerdelegate/prepareforpopoverpresentation%28_%3A%29.json'
content_hash: 'sha256:c3bc08938ec57a1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationControllerDelegate](../uipopoverpresentationcontrollerdelegate.md)

# prepareForPopoverPresentation(_:)

<sub>Instance Method</sub>

Notifies the delegate that the popover is about to be presented.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func prepareForPopoverPresentation(_ popoverPresentationController: UIPopoverPresentationController)
```

## Parameters

- `popoverPresentationController` — The popover presentation controller that is about to display the popover.

## Discussion

Use this method to perform any last minute customizations of the popover appearance and behavior. At the time this method is called, the popover is not yet on the screen. You can use this method to modify the configuration of the popover presentation controller or perform any other actions that your app requires.

## See Also

### Presenting and dismissing the popover

- [- popoverPresentationControllerShouldDismissPopover:](<popoverpresentationcontrollershoulddismisspopover(__).md>) — Asks the delegate if the popover should be dismissed. _(deprecated)_
- [- popoverPresentationControllerDidDismissPopover:](<popoverpresentationcontrollerdiddismisspopover(__).md>) — Tells the delegate that the popover was dismissed. _(deprecated)_
