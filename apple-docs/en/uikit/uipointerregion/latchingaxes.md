---
title: latchingAxes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerregion/latchingaxes
source_url: 'https://developer.apple.com/documentation/uikit/uipointerregion/latchingaxes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerregion/latchingaxes.json'
content_hash: 'sha256:fc35c7aeabcaad11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerRegion](../uipointerregion.md)

# latchingAxes

<sub>Instance Property</sub>

Axes along which the region latches after a primary click.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var latchingAxes: UIAxis { get set }
```

## Discussion

If you set this property, the [UIPointerStyle](../uipointerstyle.md) associated with this region locks in and only allows freeform movement along the axes you specify.

## See Also

### Configuring a region

- [rect](rect.md) — The rectangle bounds of the region.
- [identifier](identifier-1tw1m.md) — An optional identifier for the region.
