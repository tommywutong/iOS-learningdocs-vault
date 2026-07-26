---
title: emissionLongitude
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemittercell/emissionlongitude
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell/emissionlongitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell/emissionlongitude.json'
content_hash: 'sha256:27014034e51bb621'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterCell](../caemittercell.md)

# emissionLongitude

<sub>Instance Property</sub>

The longitudinal orientation of the emission angle. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var emissionLongitude: CGFloat { get set }
```

## Discussion

The emission longitude is the orientation of the emission angle in the xy-plane. it is also often referred to as the azimuth.

The default value of this property is `0.0`.

## See Also

### Setting Emitter Cell Motion Attributes

- [spin](spin.md) — The rotational velocity, measured in radians per second, to apply to the cell. Animatable.
- [spinRange](spinrange.md) — The amount by which the spin of the cell can vary over its lifetime. Animatable.
- [emissionLatitude](emissionlatitude.md) — The latitudinal orientation of the emission angle. Animatable.
- [emissionRange](emissionrange.md) — The angle, in radians, defining a cone around the emission angle. Animatable.
