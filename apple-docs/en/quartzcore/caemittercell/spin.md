---
title: spin
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemittercell/spin
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell/spin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell/spin.json'
content_hash: 'sha256:cdb94e8fb372818d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterCell](../caemittercell.md)

# spin

<sub>Instance Property</sub>

The rotational velocity, measured in radians per second, to apply to the cell. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var spin: CGFloat { get set }
```

## Discussion

The spin of the cell will vary by a random amount with the range specified by [spinRange](spinrange.md).

The default value of this property is `0.0`.

## See Also

### Setting Emitter Cell Motion Attributes

- [spinRange](spinrange.md) — The amount by which the spin of the cell can vary over its lifetime. Animatable.
- [emissionLatitude](emissionlatitude.md) — The latitudinal orientation of the emission angle. Animatable.
- [emissionLongitude](emissionlongitude.md) — The longitudinal orientation of the emission angle. Animatable.
- [emissionRange](emissionrange.md) — The angle, in radians, defining a cone around the emission angle. Animatable.
