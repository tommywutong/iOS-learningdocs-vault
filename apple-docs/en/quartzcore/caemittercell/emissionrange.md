---
title: emissionRange
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemittercell/emissionrange
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell/emissionrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell/emissionrange.json'
content_hash: 'sha256:1d60f88284f46ef3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterCell](../caemittercell.md)

# emissionRange

<sub>Instance Property</sub>

The angle, in radians, defining a cone around the emission angle. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var emissionRange: CGFloat { get set }
```

## Discussion

Cells are uniformly distributed across this cone.

The default value of this property is `0`.

## See Also

### Setting Emitter Cell Motion Attributes

- [spin](spin.md) — The rotational velocity, measured in radians per second, to apply to the cell. Animatable.
- [spinRange](spinrange.md) — The amount by which the spin of the cell can vary over its lifetime. Animatable.
- [emissionLatitude](emissionlatitude.md) — The latitudinal orientation of the emission angle. Animatable.
- [emissionLongitude](emissionlongitude.md) — The longitudinal orientation of the emission angle. Animatable.
