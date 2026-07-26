---
title: 'pushViewController(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationcontroller/pushviewcontroller(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/pushviewcontroller(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/pushviewcontroller%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:9ab940c7dc07a306'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# pushViewController(_:animated:)

<sub>Instance Method</sub>

Pushes a view controller onto the receiver’s stack and updates the display.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pushViewController(_ viewController: UIViewController, animated: Bool)
```

## Parameters

- `viewController` — The view controller to push onto the stack. This object cannot be a tab bar controller. If the view controller is already on the navigation stack, this method throws an exception.

- `animated` — Specify [true](../../swift/true.md) to animate the transition or [false](../../swift/false.md) if you do not want the transition to be animated. You might specify [false](../../swift/false.md) if you are setting up the navigation controller at launch time.

## Discussion

The object in the `viewController` parameter becomes the top view controller on the navigation stack. Pushing a view controller causes its view to be embedded in the navigation interface. If the `animated` parameter is [true](../../swift/true.md), the view is animated into position; otherwise, the view is simply displayed in its final location.

In addition to displaying the view associated with the new view controller at the top of the stack, this method also updates the navigation bar and tool bar accordingly. For information on how the navigation bar is updated, see [Updating the navigation bar](../uinavigationcontroller.md#Updating-the-navigation-bar).

## See Also

### Pushing and popping stack items

- [- popViewControllerAnimated:](<popviewcontroller(animated_).md>) — Pops the top view controller from the navigation stack and updates the display.
- [- popToRootViewControllerAnimated:](<poptorootviewcontroller(animated_).md>) — Pops all the view controllers on the stack except the root view controller and updates the display.
- [- popToViewController:animated:](<poptoviewcontroller(__animated_).md>) — Pops view controllers until the specified view controller is at the top of the navigation stack.
- [interactivePopGestureRecognizer](interactivepopgesturerecognizer.md) — The gesture recognizer responsible for popping the top view controller off the navigation stack when a person swipes from the leading screen edge.
- [interactiveContentPopGestureRecognizer](interactivecontentpopgesturerecognizer.md) — The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person pans horizontally in the view.
