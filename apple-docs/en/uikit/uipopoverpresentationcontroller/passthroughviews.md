---
title: passthroughViews
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverpresentationcontroller/passthroughviews
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/passthroughviews'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontroller/passthroughviews.json'
content_hash: 'sha256:e5d8b69b48d67175'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationController](../uipopoverpresentationcontroller.md)

# passthroughViews

<sub>Instance Property</sub>

An array of views that the user can interact with while the popover is visible.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var passthroughViews: [UIView]? { get set }
```

## Discussion

When a popover is active, interactions with other views are normally disabled until the popover is dismissed. Assigning an array of [UIView](../uiview.md) objects to this property causes UIKit to continue dispatching touch event to the views you specified.

## See Also

### Configuring the popover appearance

- [popoverLayoutMargins](popoverlayoutmargins.md) — The margins that define the portion of the screen in which it is permissible to display the popover.
- [backgroundColor](backgroundcolor.md) — The color of the popover’s backdrop view.
- [popoverBackgroundViewClass](popoverbackgroundviewclass.md) — The class to use for displaying the popover background content.
- [canOverlapSourceViewRect](canoverlapsourceviewrect.md) — A Boolean value indicating whether the popover can overlap its view rectangle.
