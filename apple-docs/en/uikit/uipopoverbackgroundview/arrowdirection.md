---
title: arrowDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverbackgroundview/arrowdirection
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverbackgroundview/arrowdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverbackgroundview/arrowdirection.json'
content_hash: 'sha256:64f3d5b1ffab6814'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverBackgroundView](../uipopoverbackgroundview.md)

# arrowDirection

<sub>Instance Property</sub>

The direction in which the popover arrow is pointing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var arrowDirection: UIPopoverArrowDirection { get set }
```

## Discussion

The default implementation of this method raises an exception. You must override it and implement the appropriate setter and getter methods yourself. Your methods must not call `super`.

You should use this value during layout to configure the images to use for your view’s content. In your setter method, you should update to your view’s content and potentially update the layout as well.

Use this value to determine which stretchable images to use for your view. Normally, you would have different sets of images depending on whether the arrow was pointing up, down, left, or right. (You could also use the same image for up and down, or left and right, and use a transform to flip the images so that they point in the appropriate direction.)  The popover controller sets this value prior to displaying the popover initially, and it may change the value after your popover is displayed on screen.

## See Also

### Accessing the arrow metrics

- [arrowOffset](arrowoffset.md) — The distance (measured in points) from the center of the view to the center line of the arrow.
