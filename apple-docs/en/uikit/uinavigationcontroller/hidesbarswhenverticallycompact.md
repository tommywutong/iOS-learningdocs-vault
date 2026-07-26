---
title: hidesBarsWhenVerticallyCompact
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontroller/hidesbarswhenverticallycompact
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/hidesbarswhenverticallycompact'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/hidesbarswhenverticallycompact.json'
content_hash: 'sha256:93a53171a3957857'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# hidesBarsWhenVerticallyCompact

<sub>Instance Property</sub>

A Boolean value indicating whether the navigation controller hides its bars in a vertically compact environment.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hidesBarsWhenVerticallyCompact: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the navigation controller hides its navigation bar and toolbar when it transitions to a vertically compact environment. Upon returning to a vertically regular environment, the navigation controller automatically shows both bars again. In addition, unhandled taps in the content area cause the navigation controller to show both bars again. The default value of this property is [false](../../swift/false.md).

## See Also

### Hiding the navigation bar

- [hidesBarsOnTap](hidesbarsontap.md) — A Boolean value indicating whether the navigation controller allows hiding of its bars using a tap gesture.
- [hidesBarsOnSwipe](hidesbarsonswipe.md) — A Boolean value indicating whether the navigation bar hides its bars in response to a swipe gesture.
- [hidesBarsWhenKeyboardAppears](hidesbarswhenkeyboardappears.md) — A Boolean value indicating whether the navigation controller hides its bars when the keyboard appears.
- [navigationBarHidden](isnavigationbarhidden.md) — A Boolean value that indicates whether the navigation bar is hidden.
- [barHideOnTapGestureRecognizer](barhideontapgesturerecognizer.md) — The gesture recognizer used to hide and show the navigation and toolbar.
- [barHideOnSwipeGestureRecognizer](barhideonswipegesturerecognizer.md) — The gesture recognizer used to hide the navigation bar and toolbar.
