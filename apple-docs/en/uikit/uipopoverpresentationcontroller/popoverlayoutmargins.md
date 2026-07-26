---
title: popoverLayoutMargins
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverpresentationcontroller/popoverlayoutmargins
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/popoverlayoutmargins'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontroller/popoverlayoutmargins.json'
content_hash: 'sha256:1187aeb3e6e05d37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationController](../uipopoverpresentationcontroller.md)

# popoverLayoutMargins

<sub>Instance Property</sub>

The margins that define the portion of the screen in which it is permissible to display the popover.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var popoverLayoutMargins: UIEdgeInsets { get set }
```

## Discussion

The edge inset values are measured in points from the edges of the screen, relative to the current device orientation. Thus, the top-edge inset always reflects the top edge of the device from the user’s perspective, which changes depending on whether the user is holding the device in a portrait or landscape orientation. Remember that the device orientation is not always the same as the interface orientation—that is, the orientation of your window and views. Window orientations are typically fixed and view orientations are controlled by the owning view controller. In addition, if the rotation lock option is engaged, the interface does not change orientation at all, even when the device orientation changes.

The default edge insets are 10 points along each edge. The popover presentation controller automatically subtracts the status bar from the viable area when determining where to display the popover, so you do not need to factor the status bar height into your insets.

## See Also

### Configuring the popover appearance

- [backgroundColor](backgroundcolor.md) — The color of the popover’s backdrop view.
- [passthroughViews](passthroughviews.md) — An array of views that the user can interact with while the popover is visible.
- [popoverBackgroundViewClass](popoverbackgroundviewclass.md) — The class to use for displaying the popover background content.
- [canOverlapSourceViewRect](canoverlapsourceviewrect.md) — A Boolean value indicating whether the popover can overlap its view rectangle.
