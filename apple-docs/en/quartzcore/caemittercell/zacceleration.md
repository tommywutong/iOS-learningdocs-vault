---
title: zAcceleration
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemittercell/zacceleration
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell/zacceleration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell/zacceleration.json'
content_hash: 'sha256:ff9df56d44d42c06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterCell](../caemittercell.md)

# zAcceleration

<sub>Instance Property</sub>

The z component of an acceleration vector applied to cell.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var zAcceleration: CGFloat { get set }
```

## Discussion

The default value of this property is `0.0`.

## See Also

### Setting Emitter Cell Temporal Attributes

- [lifetime](lifetime.md) — The lifetime of the cell, in seconds. Animatable.
- [lifetimeRange](lifetimerange.md) — The mean value by which the [lifetime](lifetime.md) of the cell can vary. Animatable.
- [birthRate](birthrate.md) — The number of emitted objects created every second. Animatable.
- [scaleSpeed](scalespeed.md) — The speed at which the scale changes over the lifetime of the cell. Animatable.
- [velocity](velocity.md) — The initial velocity of the cell. Animatable.
- [velocityRange](velocityrange.md) — The amount by which the velocity of the cell can vary. Animatable.
- [xAcceleration](xacceleration.md) — The x component of an acceleration vector applied to cell.
- [yAcceleration](yacceleration.md) — The y component of an acceleration vector applied to cell.
