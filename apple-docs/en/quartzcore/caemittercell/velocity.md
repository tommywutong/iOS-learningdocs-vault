---
title: velocity
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemittercell/velocity
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell/velocity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell/velocity.json'
content_hash: 'sha256:73fe372e7fc4edf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterCell](../caemittercell.md)

# velocity

<sub>Instance Property</sub>

The initial velocity of the cell. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var velocity: CGFloat { get set }
```

## Discussion

The velocity of the cell will vary by a random amount within the range specified by [velocityRange](velocityrange.md).

## See Also

### Setting Emitter Cell Temporal Attributes

- [lifetime](lifetime.md) — The lifetime of the cell, in seconds. Animatable.
- [lifetimeRange](lifetimerange.md) — The mean value by which the [lifetime](lifetime.md) of the cell can vary. Animatable.
- [birthRate](birthrate.md) — The number of emitted objects created every second. Animatable.
- [scaleSpeed](scalespeed.md) — The speed at which the scale changes over the lifetime of the cell. Animatable.
- [velocityRange](velocityrange.md) — The amount by which the velocity of the cell can vary. Animatable.
- [xAcceleration](xacceleration.md) — The x component of an acceleration vector applied to cell.
- [yAcceleration](yacceleration.md) — The y component of an acceleration vector applied to cell.
- [zAcceleration](zacceleration.md) — The z component of an acceleration vector applied to cell.
