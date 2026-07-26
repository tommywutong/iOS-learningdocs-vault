---
title: backgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverpresentationcontroller/backgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/backgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontroller/backgroundcolor.json'
content_hash: 'sha256:e083d38e68722069'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationController](../uipopoverpresentationcontroller.md)

# backgroundColor

<sub>Instance Property</sub>

The color of the popover’s backdrop view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@NSCopying var backgroundColor: UIColor? { get set }
```

## Discussion

Use this property to customize the background color of your popover. Changing the value of this property while the popover is visible triggers an animated change to the new color. The default value of this property is `nil`, which corresponds to the default background color.

## See Also

### Configuring the popover appearance

- [popoverLayoutMargins](popoverlayoutmargins.md) — The margins that define the portion of the screen in which it is permissible to display the popover.
- [passthroughViews](passthroughviews.md) — An array of views that the user can interact with while the popover is visible.
- [popoverBackgroundViewClass](popoverbackgroundviewclass.md) — The class to use for displaying the popover background content.
- [canOverlapSourceViewRect](canoverlapsourceviewrect.md) — A Boolean value indicating whether the popover can overlap its view rectangle.
