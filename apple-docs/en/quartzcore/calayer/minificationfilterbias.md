---
title: minificationFilterBias
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/minificationfilterbias
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/minificationfilterbias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/minificationfilterbias.json'
content_hash: 'sha256:16edc6c6e486d090'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# minificationFilterBias

<sub>Instance Property</sub>

The bias factor used by the minification filter to determine the levels of detail.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var minificationFilterBias: Float { get set }
```

## Discussion

This value is used by the [minificationFilter](minificationfilter.md) when it is set to [kCAFilterTrilinear](../calayercontentsfilter/trilinear.md).

The default value of this property is `0.0`.

## See Also

### Layer filters

- [filters](filters.md) — An array of Core Image filters to apply to the contents of the layer and its sublayers. Animatable.
- [compositingFilter](compositingfilter.md) — A CoreImage filter used to composite the layer and the content behind it. Animatable.
- [backgroundFilters](backgroundfilters.md) — An array of Core Image filters to apply to the content immediately behind the layer. Animatable.
- [minificationFilter](minificationfilter.md) — The filter used when reducing the size of the content.
- [magnificationFilter](magnificationfilter.md) — The filter used when increasing the size of the content.
