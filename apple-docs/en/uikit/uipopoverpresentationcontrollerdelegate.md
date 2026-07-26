---
title: UIPopoverPresentationControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverpresentationcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontrollerdelegate.json'
content_hash: 'sha256:7e7a36ae0b0995f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPopoverPresentationControllerDelegate

<sub>Protocol</sub>

The interface for a popover presentation delegate, which lets you customize the behavior of a popover-based presentation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIPopoverPresentationControllerDelegate : UIAdaptivePresentationControllerDelegate
```

## Overview

A popover presentation controller notifies your delegate at appropriate points during the presentation process. You can use the delegate methods to customize this process and respond to changes dynamically.

After defining an object that adopts this protocol, assign that object to the [delegate](uipopoverpresentationcontroller/delegate.md) property of a [UIPopoverPresentationController](uipopoverpresentationcontroller.md) object. You must present a view controller using the [UIModalPresentationPopover](uimodalpresentationstyle/popover.md) style before you can obtain such an object. For more information about popover presentation controllers, see [UIPopoverPresentationController](uipopoverpresentationcontroller.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md)

## Topics

### Presenting and dismissing the popover

- [- prepareForPopoverPresentation:](<uipopoverpresentationcontrollerdelegate/prepareforpopoverpresentation(__).md>) — Notifies the delegate that the popover is about to be presented.
- [- popoverPresentationControllerShouldDismissPopover:](<uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollershoulddismisspopover(__).md>) — Asks the delegate if the popover should be dismissed. _(deprecated)_
- [- popoverPresentationControllerDidDismissPopover:](<uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollerdiddismisspopover(__).md>) — Tells the delegate that the popover was dismissed. _(deprecated)_

### Repositioning the popover

- [- popoverPresentationController:willRepositionPopoverToRect:inView:](<uipopoverpresentationcontrollerdelegate/popoverpresentationcontroller(__willrepositionpopoverto_in_).md>) — Tells the delegate that UIKit needs to reposition the popover’s location.

## See Also

### Customizing the popover behavior

- [delegate](uipopoverpresentationcontroller/delegate.md) — The delegate that handles popover-related messages.
