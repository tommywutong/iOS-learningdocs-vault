---
title: safeAreaLayoutGuide
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/safearealayoutguide
source_url: 'https://developer.apple.com/documentation/uikit/uiview/safearealayoutguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/safearealayoutguide.json'
content_hash: 'sha256:5515a4d2bf30bdab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# safeAreaLayoutGuide

<sub>Instance Property</sub>

The layout guide representing the portion of your view that is unobscured by bars and other content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var safeAreaLayoutGuide: UILayoutGuide { get }
```

## Discussion

When the view is visible onscreen, this guide reflects the portion of the view that is not covered by navigation bars, tab bars, toolbars, and other ancestor views. (In tvOS, the safe area reflects the area not covered the screen’s bezel.) If the view is not currently installed in a view hierarchy, or is not yet visible onscreen, the layout guide edges are equal to the edges of the view.

For the view controller’s root view, the layout guide accommodates the status bar, other visible bars, and any additional insets that you specified using the [additionalSafeAreaInsets](../uiviewcontroller/additionalsafeareainsets.md) property of your view controller. For other views in the view hierarchy, the layout guide reflects only the portion of the view that is covered by other content. For example, if a view is entirely within the safe area of its superview, the layout guide edges are equal to the edges of the view.

## See Also

### Getting the safe area

- [Positioning content relative to the safe area](../positioning-content-relative-to-the-safe-area.md) — Position views so that they aren’t obstructed by other content.
- [safeAreaInsets](safeareainsets.md) — The insets that you use to determine the safe area for this view.
- [- safeAreaInsetsDidChange](<safeareainsetsdidchange().md>) — Called when the safe area of the view changes.
- [insetsLayoutMarginsFromSafeArea](insetslayoutmarginsfromsafearea.md) — A Boolean value indicating whether the view’s layout margins are updated automatically to reflect the safe area.
