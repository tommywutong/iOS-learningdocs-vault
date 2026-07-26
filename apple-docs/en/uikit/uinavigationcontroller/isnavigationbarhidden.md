---
title: isNavigationBarHidden
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontroller/isnavigationbarhidden
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/isnavigationbarhidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/isnavigationbarhidden.json'
content_hash: 'sha256:8f01fe482793c6f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# isNavigationBarHidden

<sub>Instance Property</sub>

A Boolean value that indicates whether the navigation bar is hidden.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isNavigationBarHidden: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the navigation bar is hidden. The default value is [false](../../swift/false.md). Setting this property changes the visibility of the navigation bar without animating the changes. If you want to animate the change, use the [- setNavigationBarHidden:animated:](<setnavigationbarhidden(__animated_).md>)method instead.

## See Also

### Hiding the navigation bar

- [hidesBarsOnTap](hidesbarsontap.md) — A Boolean value indicating whether the navigation controller allows hiding of its bars using a tap gesture.
- [hidesBarsOnSwipe](hidesbarsonswipe.md) — A Boolean value indicating whether the navigation bar hides its bars in response to a swipe gesture.
- [hidesBarsWhenVerticallyCompact](hidesbarswhenverticallycompact.md) — A Boolean value indicating whether the navigation controller hides its bars in a vertically compact environment.
- [hidesBarsWhenKeyboardAppears](hidesbarswhenkeyboardappears.md) — A Boolean value indicating whether the navigation controller hides its bars when the keyboard appears.
- [barHideOnTapGestureRecognizer](barhideontapgesturerecognizer.md) — The gesture recognizer used to hide and show the navigation and toolbar.
- [barHideOnSwipeGestureRecognizer](barhideonswipegesturerecognizer.md) — The gesture recognizer used to hide the navigation bar and toolbar.
