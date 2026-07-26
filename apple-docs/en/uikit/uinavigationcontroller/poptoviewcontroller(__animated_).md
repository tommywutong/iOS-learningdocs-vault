---
title: 'popToViewController(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationcontroller/poptoviewcontroller(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/poptoviewcontroller(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/poptoviewcontroller%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:a1de8c2a243c563b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# popToViewController(_:animated:)

<sub>Instance Method</sub>

Pops view controllers until the specified view controller is at the top of the navigation stack.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func popToViewController(_ viewController: UIViewController, animated: Bool) -> [UIViewController]?
```

## Parameters

- `viewController` — The view controller that you want to be at the top of the stack. This view controller must currently be on the navigation stack.

- `animated` — Set this value to [true](../../swift/true.md) to animate the transition. Pass [false](../../swift/false.md) if you are setting up a navigation controller before its view is displayed.

## Return Value

An array containing the view controllers that were popped from the stack.

## Discussion

For information on how the navigation bar is updated, see [Updating the navigation bar](../uinavigationcontroller.md#Updating-the-navigation-bar).

## See Also

### Pushing and popping stack items

- [- pushViewController:animated:](<pushviewcontroller(__animated_).md>) — Pushes a view controller onto the receiver’s stack and updates the display.
- [- popViewControllerAnimated:](<popviewcontroller(animated_).md>) — Pops the top view controller from the navigation stack and updates the display.
- [- popToRootViewControllerAnimated:](<poptorootviewcontroller(animated_).md>) — Pops all the view controllers on the stack except the root view controller and updates the display.
- [interactivePopGestureRecognizer](interactivepopgesturerecognizer.md) — The gesture recognizer responsible for popping the top view controller off the navigation stack when a person swipes from the leading screen edge.
- [interactiveContentPopGestureRecognizer](interactivecontentpopgesturerecognizer.md) — The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person pans horizontally in the view.
