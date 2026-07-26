---
title: rect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerregion/rect
source_url: 'https://developer.apple.com/documentation/uikit/uipointerregion/rect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerregion/rect.json'
content_hash: 'sha256:f20ff1f7f5fbd8b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerRegion](../uipointerregion.md)

# rect

<sub>Instance Property</sub>

The rectangle bounds of the region.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var rect: CGRect { get }
```

## Discussion

This rectangle must be in the [UIPointerInteraction](../uipointerinteraction.md) view’s coordinate space.

## See Also

### Configuring a region

- [identifier](identifier-1tw1m.md) — An optional identifier for the region.
- [latchingAxes](latchingaxes.md) — Axes along which the region latches after a primary click.
