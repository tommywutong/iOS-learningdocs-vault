---
title: interactivePopGestureRecognizer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontroller/interactivepopgesturerecognizer
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/interactivepopgesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/interactivepopgesturerecognizer.json'
content_hash: 'sha256:31ede5fa85d5e363'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# interactivePopGestureRecognizer

<sub>Instance Property</sub>

The gesture recognizer responsible for popping the top view controller off the navigation stack when a person swipes from the leading screen edge.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var interactivePopGestureRecognizer: UIGestureRecognizer? { get }
```

## Discussion

The navigation controller installs this gesture recognizer on its view and uses it to pop the topmost view controller off the navigation stack when a person swipes horizontally from the leading edge of the screen.

Use this property to retrieve the gesture recognizer and tie it to the behavior of other gesture recognizers in your user interface.

## See Also

### Related Documentation

- [- gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:](<../uigesturerecognizerdelegate/gesturerecognizer(__shouldrecognizesimultaneouslywith_).md>) — Asks the delegate if two gesture recognizers should be allowed to recognize gestures simultaneously.

### Pushing and popping stack items

- [- pushViewController:animated:](<pushviewcontroller(__animated_).md>) — Pushes a view controller onto the receiver’s stack and updates the display.
- [- popViewControllerAnimated:](<popviewcontroller(animated_).md>) — Pops the top view controller from the navigation stack and updates the display.
- [- popToRootViewControllerAnimated:](<poptorootviewcontroller(animated_).md>) — Pops all the view controllers on the stack except the root view controller and updates the display.
- [- popToViewController:animated:](<poptoviewcontroller(__animated_).md>) — Pops view controllers until the specified view controller is at the top of the navigation stack.
- [interactiveContentPopGestureRecognizer](interactivecontentpopgesturerecognizer.md) — The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person pans horizontally in the view.
