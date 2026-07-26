---
title: magnificationFilter
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemittercell/magnificationfilter
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell/magnificationfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell/magnificationfilter.json'
content_hash: 'sha256:342315f43c31649b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterCell](../caemittercell.md)

# magnificationFilter

<sub>Instance Property</sub>

The filter used when increasing the size of the content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var magnificationFilter: String { get set }
```

## Discussion

The possible values for this property are listed in Scaling Filters. The default value is [kCAFilterLinear](../calayercontentsfilter/linear.md).

## See Also

### Setting Emitter Cell Visual Attributes

- [enabled](isenabled.md) — A Boolean value indicating whether or not cells from this emitter are rendered.
- [color](color.md) — The color of each emitted object. Animatable.
- [redRange](redrange.md) — The amount by which the red color component of the cell can vary. Animatable.
- [greenRange](greenrange.md) — The amount by which the green color component of the cell can vary. Animatable.
- [blueRange](bluerange.md) — The amount by which the blue color component of the cell can vary. Animatable.
- [alphaRange](alpharange.md) — The amount by which the alpha component of the cell can vary. Animatable.
- [redSpeed](redspeed.md) — The speed, in seconds, at which the red color component changes over the lifetime of the cell. Animatable.
- [greenSpeed](greenspeed.md) — The speed, in seconds, at which the green color component changes over the lifetime of the cell. Animatable.
- [blueSpeed](bluespeed.md) — The speed, in seconds, at which the blue color component changes over the lifetime of the cell. Animatable.
- [alphaSpeed](alphaspeed.md) — The speed, in seconds, at which the alpha component changes over the lifetime of the cell. Animatable.
- [minificationFilter](minificationfilter.md) — The filter used when reducing the size of the content.
- [minificationFilterBias](minificationfilterbias.md) — The bias factor used by the minification filter to determine the levels of detail.
- [scale](scale.md) — Specifies the scale factor applied to the cell. Animatable.
- [scaleRange](scalerange.md) — Specifies the range over which the scale value can vary. Animatable.
- [contentsScale](contentsscale.md) — The scale factor of the cell contents.
