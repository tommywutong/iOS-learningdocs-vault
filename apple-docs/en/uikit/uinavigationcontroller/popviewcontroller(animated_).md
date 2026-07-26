---
title: 'popViewController(animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationcontroller/popviewcontroller(animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/popviewcontroller(animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/popviewcontroller%28animated%3A%29.json'
content_hash: 'sha256:9f36524ec1f6f14e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# popViewController(animated:)

<sub>Instance Method</sub>

Pops the top view controller from the navigation stack and updates the display.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func popViewController(animated: Bool) -> UIViewController?
```

## Parameters

- `animated` — Set this value to [true](../../swift/true.md) to animate the transition. Pass [false](../../swift/false.md) if you are setting up a navigation controller before its view is displayed.

## Return Value

The view controller that was popped from the stack.

## Discussion

This method removes the top view controller from the stack and makes the new top of the stack the active view controller. If the view controller at the top of the stack is the root view controller, this method does nothing. In other words, you cannot pop the last item on the stack.

In addition to displaying the view associated with the new view controller at the top of the stack, this method also updates the navigation bar and tool bar accordingly. For information on how the navigation bar is updated, see [Updating the navigation bar](../uinavigationcontroller.md#Updating-the-navigation-bar).

## See Also

### Pushing and popping stack items

- [- pushViewController:animated:](<pushviewcontroller(__animated_).md>) — Pushes a view controller onto the receiver’s stack and updates the display.
- [- popToRootViewControllerAnimated:](<poptorootviewcontroller(animated_).md>) — Pops all the view controllers on the stack except the root view controller and updates the display.
- [- popToViewController:animated:](<poptoviewcontroller(__animated_).md>) — Pops view controllers until the specified view controller is at the top of the navigation stack.
- [interactivePopGestureRecognizer](interactivepopgesturerecognizer.md) — The gesture recognizer responsible for popping the top view controller off the navigation stack when a person swipes from the leading screen edge.
- [interactiveContentPopGestureRecognizer](interactivecontentpopgesturerecognizer.md) — The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person pans horizontally in the view.
