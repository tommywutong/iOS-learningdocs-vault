---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverpresentationcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontroller/delegate.json'
content_hash: 'sha256:86d9fb53c4f5d57d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationController](../uipopoverpresentationcontroller.md)

# delegate

<sub>Instance Property</sub>

The delegate that handles popover-related messages.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIPopoverPresentationControllerDelegate)? { get set }
```

## Discussion

At various points during the presentation process, the popover presentation controller calls methods of its delegate to give that object a chance to respond. You might use a delegate to further configure the popover presentation controller or to respond to user-initiated actions relating to the popover. For example, immediately prior to displaying the popover, the presentation controller calls the [- prepareForPopoverPresentation:](<../uipopoverpresentationcontrollerdelegate/prepareforpopoverpresentation(__).md>) method of the delegate object.

For more information about the methods that you can implement in your delegate object, see [UIPopoverPresentationControllerDelegate](../uipopoverpresentationcontrollerdelegate.md).

## See Also

### Customizing the popover behavior

- [UIPopoverPresentationControllerDelegate](../uipopoverpresentationcontrollerdelegate.md) — The interface for a popover presentation delegate, which lets you customize the behavior of a popover-based presentation.
