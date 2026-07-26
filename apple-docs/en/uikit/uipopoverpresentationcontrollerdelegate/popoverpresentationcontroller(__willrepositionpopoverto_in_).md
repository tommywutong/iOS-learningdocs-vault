---
title: 'popoverPresentationController(_:willRepositionPopoverTo:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipopoverpresentationcontrollerdelegate/popoverpresentationcontroller(_:willrepositionpopoverto:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate/popoverpresentationcontroller(_:willrepositionpopoverto:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontrollerdelegate/popoverpresentationcontroller%28_%3Awillrepositionpopoverto%3Ain%3A%29.json'
content_hash: 'sha256:d5be479fc7546248'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationControllerDelegate](../uipopoverpresentationcontrollerdelegate.md)

# popoverPresentationController(_:willRepositionPopoverTo:in:)

<sub>Instance Method</sub>

Tells the delegate that UIKit needs to reposition the popover’s location.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func popoverPresentationController(_ popoverPresentationController: UIPopoverPresentationController, willRepositionPopoverTo rect: UnsafeMutablePointer<CGRect>, in view: AutoreleasingUnsafeMutablePointer<UIView>)
```

## Parameters

- `popoverPresentationController` — The popover presentation controller that’s managing the popover interface.

- `rect` — On input, the new rectangle for the popover. This popover is in the coordinate space of the view in the `view` parameter. If you want to propose a different rectangle for the popover, put the new value in this parameter.

- `view` — On input, the new view for containing the popover. If you want to propose a different view for the popover, put that view in this parameter.

## Discussion

The popover presentation controller calls this method in response to interface changes that require a new size for the popover. For example, UIKit calls this method when the popover must be resized to make room for the keyboard. You can use this method to obtain the new size of the popover and optionally to make changes to the proposed view and rectangle.

If you don’t implement this method in your delegate, UIKit resizes the popover to the specified rectangle and moves it (as needed) to the specified view.
