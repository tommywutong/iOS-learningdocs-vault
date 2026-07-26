---
title: 'navigationController(_:didShow:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller(_:didshow:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller(_:didshow:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller%28_%3Adidshow%3Aanimated%3A%29.json'
content_hash: 'sha256:f33885ac7e2e41a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationControllerDelegate](../uinavigationcontrollerdelegate.md)

# navigationController(_:didShow:animated:)

<sub>Instance Method</sub>

Notifies the delegate after the navigation controller displays a view controller’s view and navigation item properties.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func navigationController(_ navigationController: UINavigationController, didShow viewController: UIViewController, animated: Bool)
```

## Parameters

- `navigationController` — The navigation controller that is showing the view and properties of a view controller.

- `viewController` — The view controller whose view and navigation item properties are being shown.

- `animated` — [true](../../swift/true.md) to animate the transition; otherwise, [false](../../swift/false.md).

## See Also

### Responding to a view controller being shown

- [- navigationController:willShowViewController:animated:](<navigationcontroller(__willshow_animated_).md>) — Notifies the delegate before the navigation controller displays a view controller’s view and navigation item properties.
