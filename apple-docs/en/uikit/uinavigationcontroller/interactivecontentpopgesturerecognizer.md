---
title: interactiveContentPopGestureRecognizer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontroller/interactivecontentpopgesturerecognizer
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/interactivecontentpopgesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/interactivecontentpopgesturerecognizer.json'
content_hash: 'sha256:a05e5322917fa8d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# interactiveContentPopGestureRecognizer

<sub>Instance Property</sub>

The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person pans horizontally in the view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var interactiveContentPopGestureRecognizer: UIGestureRecognizer? { get }
```

## Overview

The navigation controller installs this gesture recognizer on its view and uses it to interactively pop the topmost view controller off the navigation stack when a person initially pans horizontally in a leading to trailing direction in the view. It recognizes a gesture on the entire content area of the navigation controller in cases that are not covered by [interactivePopGestureRecognizer](interactivepopgesturerecognizer.md) and initiates an interactive pop.

Use this property to retrieve the gesture recognizer and tie it to the behavior of other gesture recognizers in your user interface.

## See Also

### Pushing and popping stack items

- [- pushViewController:animated:](<pushviewcontroller(__animated_).md>) — Pushes a view controller onto the receiver’s stack and updates the display.
- [- popViewControllerAnimated:](<popviewcontroller(animated_).md>) — Pops the top view controller from the navigation stack and updates the display.
- [- popToRootViewControllerAnimated:](<poptorootviewcontroller(animated_).md>) — Pops all the view controllers on the stack except the root view controller and updates the display.
- [- popToViewController:animated:](<poptoviewcontroller(__animated_).md>) — Pops view controllers until the specified view controller is at the top of the navigation stack.
- [interactivePopGestureRecognizer](interactivepopgesturerecognizer.md) — The gesture recognizer responsible for popping the top view controller off the navigation stack when a person swipes from the leading screen edge.
