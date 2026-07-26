---
title: barHideOnTapGestureRecognizer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontroller/barhideontapgesturerecognizer
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/barhideontapgesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/barhideontapgesturerecognizer.json'
content_hash: 'sha256:9d7bf0a208dc0bb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# barHideOnTapGestureRecognizer

<sub>Instance Property</sub>

The gesture recognizer used to hide and show the navigation and toolbar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
unowned(unsafe) var barHideOnTapGestureRecognizer: UITapGestureRecognizer { get }
```

## Discussion

This property contains the gesture recognizer used to hide or show the bars. The gesture recognizer is inactive unless the [hidesBarsOnTap](hidesbarsontap.md) property is [true](../../swift/true.md). You can make changes to the gesture recognizer as needed but must not change its delegate and you must not remove the default target object and action that come configured with it. Do not try to replace this gesture recognizer by overriding the property.

If you tie this gesture recognizer to one of your own, make sure both recognize their gestures simultaneously to ensure that each has a chance to handle the event.

## See Also

### Hiding the navigation bar

- [hidesBarsOnTap](hidesbarsontap.md) — A Boolean value indicating whether the navigation controller allows hiding of its bars using a tap gesture.
- [hidesBarsOnSwipe](hidesbarsonswipe.md) — A Boolean value indicating whether the navigation bar hides its bars in response to a swipe gesture.
- [hidesBarsWhenVerticallyCompact](hidesbarswhenverticallycompact.md) — A Boolean value indicating whether the navigation controller hides its bars in a vertically compact environment.
- [hidesBarsWhenKeyboardAppears](hidesbarswhenkeyboardappears.md) — A Boolean value indicating whether the navigation controller hides its bars when the keyboard appears.
- [navigationBarHidden](isnavigationbarhidden.md) — A Boolean value that indicates whether the navigation bar is hidden.
- [barHideOnSwipeGestureRecognizer](barhideonswipegesturerecognizer.md) — The gesture recognizer used to hide the navigation bar and toolbar.
