---
title: hidesBarsOnTap
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontroller/hidesbarsontap
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/hidesbarsontap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/hidesbarsontap.json'
content_hash: 'sha256:3b7658945a5a5b8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# hidesBarsOnTap

<sub>Instance Property</sub>

A Boolean value indicating whether the navigation controller allows hiding of its bars using a tap gesture.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hidesBarsOnTap: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the navigation controller toggles the hiding and showing of its navigation bar and toolbar in response to an otherwise unhandled tap in the content area. The default value of this property is [false](../../swift/false.md).

## See Also

### Hiding the navigation bar

- [hidesBarsOnSwipe](hidesbarsonswipe.md) — A Boolean value indicating whether the navigation bar hides its bars in response to a swipe gesture.
- [hidesBarsWhenVerticallyCompact](hidesbarswhenverticallycompact.md) — A Boolean value indicating whether the navigation controller hides its bars in a vertically compact environment.
- [hidesBarsWhenKeyboardAppears](hidesbarswhenkeyboardappears.md) — A Boolean value indicating whether the navigation controller hides its bars when the keyboard appears.
- [navigationBarHidden](isnavigationbarhidden.md) — A Boolean value that indicates whether the navigation bar is hidden.
- [barHideOnTapGestureRecognizer](barhideontapgesturerecognizer.md) — The gesture recognizer used to hide and show the navigation and toolbar.
- [barHideOnSwipeGestureRecognizer](barhideonswipegesturerecognizer.md) — The gesture recognizer used to hide the navigation bar and toolbar.
