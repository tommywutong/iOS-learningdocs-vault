---
title: UIViewInvalidating
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS, Swift 5.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewinvalidating
source_url: 'https://developer.apple.com/documentation/uikit/uiviewinvalidating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewinvalidating.json'
content_hash: 'sha256:ecec317cff6b4718'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewInvalidating

<sub>Protocol</sub>

Implements a type of invalidation that can occur on a view that requires an update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UIViewInvalidating
```

## Relationships

- **Conforming Types**: [Configuration](uiview/invalidations/configuration.md), [Constraints](uiview/invalidations/constraints.md), [Display](uiview/invalidations/display.md), [IntrinsicContentSize](uiview/invalidations/intrinsiccontentsize.md), [Layout](uiview/invalidations/layout.md), [Properties](uiview/invalidations/properties.md), [Tuple](uiview/invalidations/tuple.md)

## Topics

### Specifying invalidation types

- [configuration](uiviewinvalidating/configuration.md) — A change that invalidates a view’s configuration.
- [constraints](uiviewinvalidating/constraints.md) — A change that invalidates a view’s constraints.
- [display](uiviewinvalidating/display.md) — A change that requires the system to redraw a view’s content.
- [intrinsicContentSize](uiviewinvalidating/intrinsiccontentsize.md) — A change that invalidates a view’s intrinsic size.
- [layout](uiviewinvalidating/layout.md) — A change that invalidates the layout of the containing view’s subviews.

### Invalidating the view

- [invalidate(view:)](<uiviewinvalidating/invalidate(view_).md>) — Indicates to the system that an aspect of a view is invalid and triggers the necessary update.
- [Invalidations](uiview/invalidations.md) — Changes that cause an aspect of a view to be invalid and require an update.

### Type Properties

- [properties](uiviewinvalidating/properties.md)

## See Also

### Updating the view when property values change

- [Invalidating](uiview/invalidating.md) — A property wrapper that notifies the system that a property value change has invalidated an aspect of the containing view.
