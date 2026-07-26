---
title: haloOverlap
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cilenticularhalogenerator/halooverlap
source_url: 'https://developer.apple.com/documentation/coreimage/cilenticularhalogenerator/halooverlap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cilenticularhalogenerator/halooverlap.json'
content_hash: 'sha256:e28a0f273e3363c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CILenticularHaloGenerator](../cilenticularhalogenerator.md)

# haloOverlap

<sub>Instance Property</sub>

The separation of colors in the halo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var haloOverlap: Float { get set }
```

## Discussion

A value of `0` means the halo colors don’t overlap. A value of `1` means the halo colors fully overlap, creating a white halo.

## See Also

### Instance Properties

- [center](center.md) — The x and y position to use as the center of the halo.
- [color](color.md) — The color of the halo.
- [haloRadius](haloradius.md) — The radius of the halo.
- [haloWidth](halowidth.md) — The width of the halo, from its inner radius to its outer radius.
- [striationContrast](striationcontrast.md) — The contrast of the halo colors.
- [striationStrength](striationstrength.md) — The intensity of the halo colors.
- [time](time.md) — The current time of the effect.
