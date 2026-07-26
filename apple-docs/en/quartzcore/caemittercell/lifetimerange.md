---
title: lifetimeRange
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemittercell/lifetimerange
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell/lifetimerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell/lifetimerange.json'
content_hash: 'sha256:972e62873c4bf218'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterCell](../caemittercell.md)

# lifetimeRange

<sub>Instance Property</sub>

The mean value by which the [lifetime](lifetime.md) of the cell can vary. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var lifetimeRange: Float { get set }
```

## Discussion

If the [lifetimeRange](lifetimerange.md) is 3 seconds, and the [lifetime](lifetime.md) of the cell is 10 seconds, the cell’s actual lifetime will be between 7 and 13 seconds.

The default value of this property is `0.0`.

## See Also

### Setting Emitter Cell Temporal Attributes

- [lifetime](lifetime.md) — The lifetime of the cell, in seconds. Animatable.
- [birthRate](birthrate.md) — The number of emitted objects created every second. Animatable.
- [scaleSpeed](scalespeed.md) — The speed at which the scale changes over the lifetime of the cell. Animatable.
- [velocity](velocity.md) — The initial velocity of the cell. Animatable.
- [velocityRange](velocityrange.md) — The amount by which the velocity of the cell can vary. Animatable.
- [xAcceleration](xacceleration.md) — The x component of an acceleration vector applied to cell.
- [yAcceleration](yacceleration.md) — The y component of an acceleration vector applied to cell.
- [zAcceleration](zacceleration.md) — The z component of an acceleration vector applied to cell.
