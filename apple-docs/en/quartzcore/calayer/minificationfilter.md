---
title: minificationFilter
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/minificationfilter
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/minificationfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/minificationfilter.json'
content_hash: 'sha256:600a93cfb2fc8718'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# minificationFilter

<sub>Instance Property</sub>

The filter used when reducing the size of the content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var minificationFilter: CALayerContentsFilter { get set }
```

## Discussion

The possible values for this property are listed in [Scaling Filters](../scaling-filters.md).

The default value of this property is [kCAFilterLinear](../calayercontentsfilter/linear.md).

## See Also

### Layer filters

- [filters](filters.md) — An array of Core Image filters to apply to the contents of the layer and its sublayers. Animatable.
- [compositingFilter](compositingfilter.md) — A CoreImage filter used to composite the layer and the content behind it. Animatable.
- [backgroundFilters](backgroundfilters.md) — An array of Core Image filters to apply to the content immediately behind the layer. Animatable.
- [minificationFilterBias](minificationfilterbias.md) — The bias factor used by the minification filter to determine the levels of detail.
- [magnificationFilter](magnificationfilter.md) — The filter used when increasing the size of the content.
