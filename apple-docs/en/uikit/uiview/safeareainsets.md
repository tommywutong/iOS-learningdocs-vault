---
title: safeAreaInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/safeareainsets
source_url: 'https://developer.apple.com/documentation/uikit/uiview/safeareainsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/safeareainsets.json'
content_hash: 'sha256:74c87c6fe55012a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# safeAreaInsets

<sub>Instance Property</sub>

The insets that you use to determine the safe area for this view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var safeAreaInsets: UIEdgeInsets { get }
```

## Discussion

The safe area of a view reflects the area not covered by navigation bars, tab bars, toolbars, and other ancestors that obscure a view controller’s view. (In tvOS, the safe area reflects the area not covered by the screen’s bezel.) You obtain the safe area for a view by applying the insets in this property to the view’s bounds rectangle. If the view is not currently installed in a view hierarchy, or is not yet visible onscreen, the edge insets in this property are `0`.

For the view controller’s root view, the insets account for the status bar, other visible bars, and any additional insets that you specified using the [additionalSafeAreaInsets](../uiviewcontroller/additionalsafeareainsets.md) property of your view controller. For other views in the view hierarchy, the insets reflect only the portion of the view that is covered. For example, if a view is entirely within the safe area of its superview, the edge insets in this property are `0`.

You might use this property at runtime to adjust the position of your view’s content programmatically.

## See Also

### Related Documentation

- [overscanCompensationInsets](../uiscreen/overscancompensationinsets.md) — The edge inset values needed to avoid clipping the rectangle.

### Getting the safe area

- [Positioning content relative to the safe area](../positioning-content-relative-to-the-safe-area.md) — Position views so that they aren’t obstructed by other content.
- [safeAreaLayoutGuide](safearealayoutguide.md) — The layout guide representing the portion of your view that is unobscured by bars and other content.
- [- safeAreaInsetsDidChange](<safeareainsetsdidchange().md>) — Called when the safe area of the view changes.
- [insetsLayoutMarginsFromSafeArea](insetslayoutmarginsfromsafearea.md) — A Boolean value indicating whether the view’s layout margins are updated automatically to reflect the safe area.
