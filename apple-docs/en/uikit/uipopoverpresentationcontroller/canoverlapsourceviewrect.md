---
title: canOverlapSourceViewRect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverpresentationcontroller/canoverlapsourceviewrect
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/canoverlapsourceviewrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontroller/canoverlapsourceviewrect.json'
content_hash: 'sha256:546de50dcb96e26e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationController](../uipopoverpresentationcontroller.md)

# canOverlapSourceViewRect

<sub>Instance Property</sub>

A Boolean value indicating whether the popover can overlap its view rectangle.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var canOverlapSourceViewRect: Bool { get set }
```

## Discussion

Setting this property to [true](../../swift/true.md) allows the popover to overlap the rectangle in the [sourceRect](sourcerect.md) property when space is constrained. The default value of this property is false, which prevents the popover from overlapping the source rectangle.

## See Also

### Configuring the popover appearance

- [popoverLayoutMargins](popoverlayoutmargins.md) — The margins that define the portion of the screen in which it is permissible to display the popover.
- [backgroundColor](backgroundcolor.md) — The color of the popover’s backdrop view.
- [passthroughViews](passthroughviews.md) — An array of views that the user can interact with while the popover is visible.
- [popoverBackgroundViewClass](popoverbackgroundviewclass.md) — The class to use for displaying the popover background content.
