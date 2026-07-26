---
title: UIView.Invalidations
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS, Swift 5.1+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/invalidations
source_url: 'https://developer.apple.com/documentation/uikit/uiview/invalidations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/invalidations.json'
content_hash: 'sha256:331fbd7837090b80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# UIView.Invalidations

<sub>Enumeration</sub>

Changes that cause an aspect of a view to be invalid and require an update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Invalidations
```

## Topics

### Invalidation types

- [Configuration](invalidations/configuration.md) — A change that invalidates a view’s configuration.
- [Constraints](invalidations/constraints.md) — A change that invalidates a view’s constraints.
- [Display](invalidations/display.md) — A change that requires the system to redraw a view’s content.
- [IntrinsicContentSize](invalidations/intrinsiccontentsize.md) — A change that invalidates a view’s intrinsic size.
- [Layout](invalidations/layout.md) — A change that invalidates the layout of the containing view’s subviews.
- [Tuple](invalidations/tuple.md) — A change that invalidates a combination of factors covered by the other invalidation types.

### Structures

- [Properties](invalidations/properties.md)

## See Also

### Invalidating the view

- [invalidate(view:)](<../uiviewinvalidating/invalidate(view_).md>) — Indicates to the system that an aspect of a view is invalid and triggers the necessary update.
