---
title: hidesBarsWhenKeyboardAppears
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontroller/hidesbarswhenkeyboardappears
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/hidesbarswhenkeyboardappears'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/hidesbarswhenkeyboardappears.json'
content_hash: 'sha256:9e8e7486093985c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# hidesBarsWhenKeyboardAppears

<sub>Instance Property</sub>

A Boolean value indicating whether the navigation controller hides its bars when the keyboard appears.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hidesBarsWhenKeyboardAppears: Bool { get set }
```

## Discussion

When this property is set to [true](../../swift/true.md), the appearance of the keyboard causes the navigation controller to hide its navigation bar and toolbar. The default value of this property is [false](../../swift/false.md).

## See Also

### Hiding the navigation bar

- [hidesBarsOnTap](hidesbarsontap.md) — A Boolean value indicating whether the navigation controller allows hiding of its bars using a tap gesture.
- [hidesBarsOnSwipe](hidesbarsonswipe.md) — A Boolean value indicating whether the navigation bar hides its bars in response to a swipe gesture.
- [hidesBarsWhenVerticallyCompact](hidesbarswhenverticallycompact.md) — A Boolean value indicating whether the navigation controller hides its bars in a vertically compact environment.
- [navigationBarHidden](isnavigationbarhidden.md) — A Boolean value that indicates whether the navigation bar is hidden.
- [barHideOnTapGestureRecognizer](barhideontapgesturerecognizer.md) — The gesture recognizer used to hide and show the navigation and toolbar.
- [barHideOnSwipeGestureRecognizer](barhideonswipegesturerecognizer.md) — The gesture recognizer used to hide the navigation bar and toolbar.
