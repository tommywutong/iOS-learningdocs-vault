---
title: layoutMarginsDidChange()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/layoutmarginsdidchange()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/layoutmarginsdidchange()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/layoutmarginsdidchange%28%29.json'
content_hash: 'sha256:af062643f4b61549'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# layoutMarginsDidChange()

<sub>Instance Method</sub>

Notifies the view that the layout margins changed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func layoutMarginsDidChange()
```

## Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to respond when the value in the view’s [layoutMargins](layoutmargins.md) property changes. For example, you might override this method if your view subclass handles layout manually or uses the layout margins during drawing. In both cases, you could use this method to initiate a drawing or layout update.

## See Also

### Configuring content margins

- [Positioning content within layout margins](../positioning-content-within-layout-margins.md) — Position views so that they aren’t crowded by other content.
- [directionalLayoutMargins](directionallayoutmargins.md) — The default spacing to use when laying out content in a view, taking into account the current language direction.
- [layoutMargins](layoutmargins.md) — The default spacing to use when laying out content in the view.
- [preservesSuperviewLayoutMargins](preservessuperviewlayoutmargins.md) — A Boolean value indicating whether the current view also respects the margins of its superview.
