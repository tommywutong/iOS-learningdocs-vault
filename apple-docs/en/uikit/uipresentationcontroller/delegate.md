---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/delegate.json'
content_hash: 'sha256:09e60a8e6a4da56f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# delegate

<sub>Instance Property</sub>

The delegate object for managing adaptive presentations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UIAdaptivePresentationControllerDelegate)? { get set }
```

## Discussion

When the app’s size changes, the presentation controller works with this delegate object to determine an appropriate response. View controllers presented using the [UIModalPresentationFormSheet](../uimodalpresentationstyle/formsheet.md), [UIModalPresentationPopover](../uimodalpresentationstyle/popover.md), or [UIModalPresentationCustom](../uimodalpresentationstyle/custom.md) style must change to use one of the full-screen presentation styles instead. The delegate can also opt to change the presented view controller entirely.

The object you assign to this property must conform to the [UIAdaptivePresentationControllerDelegate](../uiadaptivepresentationcontrollerdelegate.md) protocol.

## See Also

### Adapting your presentations dynamically

- [UIAdaptivePresentationControllerDelegate](../uiadaptivepresentationcontrollerdelegate.md) — A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
