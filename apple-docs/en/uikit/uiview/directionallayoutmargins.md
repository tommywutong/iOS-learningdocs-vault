---
title: directionalLayoutMargins
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/directionallayoutmargins
source_url: 'https://developer.apple.com/documentation/uikit/uiview/directionallayoutmargins'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/directionallayoutmargins.json'
content_hash: 'sha256:d2dbb1ba191eb757'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# directionalLayoutMargins

<sub>Instance Property</sub>

The default spacing to use when laying out content in a view, taking into account the current language direction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var directionalLayoutMargins: NSDirectionalEdgeInsets { get set }
```

## Discussion

Use this property to specify the desired amount of space (measured in points) between the edges of this view and its subviews. The leading and trailing margins are applied appropriately to the left or right margins based on the current layout direction. For example, the leading margin is applied to the right edge of the view in right-to-left layouts. For most views, the default layout margins are 8 points on each side. You can change these values as needed for your interface.

For the root view of a view controller, the default value of this property reflects the system minimum margins and safe area insets. For other subviews in your view hierarchy, the default layout margins are normally 8 points on each side, but the values may be greater if the view is not fully inside the safe area or if the [preservesSuperviewLayoutMargins](preservessuperviewlayoutmargins.md) property is [true](../../swift/true.md).

Auto layout uses your margins as a cue for placing content. For example, if you specify a set of horizontal constraints using the format string “`|-[subview]-|`”, the leading and trailing edges of the subview are inset from the edge of the superview by the corresponding layout margins. When the edge of your view is close to the edge of the superview and the [preservesSuperviewLayoutMargins](preservessuperviewlayoutmargins.md) property is true, the actual layout margins may be increased to prevent content from overlapping the superview’s margins.

## See Also

### Configuring content margins

- [Positioning content within layout margins](../positioning-content-within-layout-margins.md) — Position views so that they aren’t crowded by other content.
- [layoutMargins](layoutmargins.md) — The default spacing to use when laying out content in the view.
- [preservesSuperviewLayoutMargins](preservessuperviewlayoutmargins.md) — A Boolean value indicating whether the current view also respects the margins of its superview.
- [- layoutMarginsDidChange](<layoutmarginsdidchange().md>) — Notifies the view that the layout margins changed.
