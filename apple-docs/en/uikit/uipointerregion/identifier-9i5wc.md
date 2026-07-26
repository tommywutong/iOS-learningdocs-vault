---
title: identifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerregion/identifier-9i5wc
source_url: 'https://developer.apple.com/documentation/uikit/uipointerregion/identifier-9i5wc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerregion/identifier-9i5wc.json'
content_hash: 'sha256:4aafa3b8a17e6fc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerRegion](../uipointerregion.md)

# identifier

<sub>Instance Property</sub>

An optional identifier for the region.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly, nullable) id<NSObject> identifier;
```

## Discussion

Use this value to identify the [UIPointerRegion](../uipointerregion.md) in subsequent pointer interaction delegate calls.

## See Also

### Configuring a region

- [rect](rect.md) — The rectangle bounds of the region.
- [latchingAxes](latchingaxes.md) — Axes along which the region latches after a primary click.
