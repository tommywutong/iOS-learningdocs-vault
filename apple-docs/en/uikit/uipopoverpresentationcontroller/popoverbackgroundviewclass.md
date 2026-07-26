---
title: popoverBackgroundViewClass
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverpresentationcontroller/popoverbackgroundviewclass
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/popoverbackgroundviewclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontroller/popoverbackgroundviewclass.json'
content_hash: 'sha256:370e173319ec7708'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationController](../uipopoverpresentationcontroller.md)

# popoverBackgroundViewClass

<sub>Instance Property</sub>

The class to use for displaying the popover background content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var popoverBackgroundViewClass: (any UIPopoverBackgroundViewMethods.Type)? { get set }
```

## Discussion

The default value of this property is `nil`, which causes the presentation controller to use the default popover appearance. Setting this property to a value other than `nil` causes the presentation controller to use the specified class to draw the popover’s background content. The class you specify must be a subclass of [UIPopoverBackgroundView](../uipopoverbackgroundview.md).

## See Also

### Configuring the popover appearance

- [popoverLayoutMargins](popoverlayoutmargins.md) — The margins that define the portion of the screen in which it is permissible to display the popover.
- [backgroundColor](backgroundcolor.md) — The color of the popover’s backdrop view.
- [passthroughViews](passthroughviews.md) — An array of views that the user can interact with while the popover is visible.
- [canOverlapSourceViewRect](canoverlapsourceviewrect.md) — A Boolean value indicating whether the popover can overlap its view rectangle.
