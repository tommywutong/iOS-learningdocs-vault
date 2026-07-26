---
title: emissionLatitude
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemittercell/emissionlatitude
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell/emissionlatitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell/emissionlatitude.json'
content_hash: 'sha256:7f8fcafdad7f000a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterCell](../caemittercell.md)

# emissionLatitude

<sub>Instance Property</sub>

The latitudinal orientation of the emission angle. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var emissionLatitude: CGFloat { get set }
```

## Discussion

The emission latitude is the orientation of the emission angle from the z-axis. It is also referred to as the colatitude.

The default value of this property is `0.0`.

## See Also

### Setting Emitter Cell Motion Attributes

- [spin](spin.md) — The rotational velocity, measured in radians per second, to apply to the cell. Animatable.
- [spinRange](spinrange.md) — The amount by which the spin of the cell can vary over its lifetime. Animatable.
- [emissionLongitude](emissionlongitude.md) — The longitudinal orientation of the emission angle. Animatable.
- [emissionRange](emissionrange.md) — The angle, in radians, defining a cone around the emission angle. Animatable.
