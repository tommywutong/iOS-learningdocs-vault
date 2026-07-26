---
title: preferredFocusedView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（10.0 起废弃）, iPadOS 9.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（10.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uifocusguide/preferredfocusedview
source_url: 'https://developer.apple.com/documentation/uikit/uifocusguide/preferredfocusedview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusguide/preferredfocusedview.json'
content_hash: 'sha256:9bfa784e0e01a8c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusGuide](../uifocusguide.md)

# preferredFocusedView

<sub>Instance Property</sub>

The view that the focus will be redirected to if this guide is focused.

> [!warning] Deprecated
> Use [preferredFocusEnvironments](preferredfocusenvironments.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
weak var preferredFocusedView: UIView? { get set }
```

## Discussion

If the guide is focused, it indirects the focus to this view. This view, or at least one view along its [preferredFocusedView](preferredfocusedview.md) chain, must be focusable in order for the guide to be focusable. Otherwise, it’s effectively disabled.

## See Also

### Enabling focus

- [enabled](isenabled.md) — A Boolean value that indicates whether the guide is focusable.
- [preferredFocusEnvironments](preferredfocusenvironments.md) — An array of focus environments to which the guide directs focus, ordered by priority.
