---
title: 'setNavigationBarHidden(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationcontroller/setnavigationbarhidden(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/setnavigationbarhidden(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/setnavigationbarhidden%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:0eb2d174798fdef0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# setNavigationBarHidden(_:animated:)

<sub>Instance Method</sub>

Sets whether the navigation bar is hidden.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNavigationBarHidden(_ hidden: Bool, animated: Bool)
```

## Parameters

- `hidden` — Specify [true](../../swift/true.md) to hide the navigation bar or [false](../../swift/false.md) to show it.

- `animated` — Specify [true](../../swift/true.md) if you want to animate the change in visibility or [false](../../swift/false.md) if you want the navigation bar to appear immediately.

## Discussion

For animated transitions, the duration of the animation is specified by the value in the [UINavigationControllerHideShowBarDuration](hideshowbarduration.md) constant.

## See Also

### Related Documentation

- [navigationBarHidden](isnavigationbarhidden.md) — A Boolean value that indicates whether the navigation bar is hidden.

### Configuring navigation bars

- [navigationBar](navigationbar.md) — The navigation bar managed by the navigation controller.
- [Customizing your app’s navigation bar](../customizing-your-app-s-navigation-bar.md) — Create custom titles, prompts, and buttons in your app’s navigation bar.
