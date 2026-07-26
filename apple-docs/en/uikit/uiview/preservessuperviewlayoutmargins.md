---
title: preservesSuperviewLayoutMargins
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/preservessuperviewlayoutmargins
source_url: 'https://developer.apple.com/documentation/uikit/uiview/preservessuperviewlayoutmargins'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/preservessuperviewlayoutmargins.json'
content_hash: 'sha256:3fd4bfaf31b5bca3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# preservesSuperviewLayoutMargins

<sub>Instance Property</sub>

A Boolean value indicating whether the current view also respects the margins of its superview.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preservesSuperviewLayoutMargins: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the superview’s margins are also considered when laying out content. This margin affects layouts where the distance between the edge of a view and its superview is smaller than the corresponding margin. For example, you might have a content view whose frame precisely matches the bounds of its superview. When any of the superview’s margins is inside the area represented by the content view and its own margins, UIKit adjusts the content view’s layout to respect the superview’s margins. The amount of the adjustment is the smallest amount needed to ensure that content is also inside the superview’s margins.

The default value of this property is [false](../../swift/false.md).

## See Also

### Configuring content margins

- [Positioning content within layout margins](../positioning-content-within-layout-margins.md) — Position views so that they aren’t crowded by other content.
- [directionalLayoutMargins](directionallayoutmargins.md) — The default spacing to use when laying out content in a view, taking into account the current language direction.
- [layoutMargins](layoutmargins.md) — The default spacing to use when laying out content in the view.
- [- layoutMarginsDidChange](<layoutmarginsdidchange().md>) — Notifies the view that the layout margins changed.
