---
title: 'setToolbarHidden(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationcontroller/settoolbarhidden(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/settoolbarhidden(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/settoolbarhidden%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:723d52de10d71d46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# setToolbarHidden(_:animated:)

<sub>Instance Method</sub>

Changes the visibility of the navigation controller’s built-in toolbar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setToolbarHidden(_ hidden: Bool, animated: Bool)
```

## Parameters

- `hidden` — Specify [true](../../swift/true.md) to hide the toolbar or [false](../../swift/false.md) to show it.

- `animated` — Specify [true](../../swift/true.md) if you want the toolbar to be animated on or off the screen.

## Discussion

You can use this method to animate changes to the visibility of the built-in toolbar.

Calling this method with the `animated` parameter set to [false](../../swift/false.md) is equivalent to setting the value of the [toolbarHidden](istoolbarhidden.md) property directly. The toolbar simply appears or disappears depending on the value in the `hidden` parameter.

## See Also

### Configuring custom toolbars

- [toolbar](toolbar.md) — The custom toolbar associated with the navigation controller.
- [toolbarHidden](istoolbarhidden.md) — A Boolean indicating whether the navigation controller’s built-in toolbar is visible.
- [UINavigationControllerHideShowBarDuration](hideshowbarduration.md) — A variable that specifies the duration when animating the navigation bar.
