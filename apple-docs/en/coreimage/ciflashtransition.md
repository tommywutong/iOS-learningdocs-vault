---
title: CIFlashTransition
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciflashtransition
source_url: 'https://developer.apple.com/documentation/coreimage/ciflashtransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciflashtransition.json'
content_hash: 'sha256:4c6ecd881f9118c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIFlashTransition

<sub>Protocol</sub>

The properties you use to configure a flash transition filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIFlashTransition : CITransitionFilter
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md), [CITransitionFilter](citransitionfilter.md)

## Topics

### Instance Properties

- [center](ciflashtransition/center.md) — The x and y position to use as the center of the effect.
- [color](ciflashtransition/color.md) — The color of the light rays emanating from the flash.
- [extent](ciflashtransition/extent.md) — The extent of the flash.
- [fadeThreshold](ciflashtransition/fadethreshold.md) — The amount of fade between the flash and the target image.
- [maxStriationRadius](ciflashtransition/maxstriationradius.md) — The radius of the light rays emanating from the flash.
- [striationContrast](ciflashtransition/striationcontrast.md) — The contrast of the light rays emanating from the flash.
- [striationStrength](ciflashtransition/striationstrength.md) — The strength of the light rays emanating from the flash.

## See Also

### Related Documentation

- [+ flashTransitionFilter](<cifilter-swift.class/flashtransition().md>) — Creates a flash of light to transition between two images.

### Protocols

- [CITransitionFilter](citransitionfilter.md) — The properties you use to configure a transition filter.
- [CIBarsSwipeTransition](cibarsswipetransition.md) — The properties you use to configure a bars swipe transition filter.
- [CIAccordionFoldTransition](ciaccordionfoldtransition.md) — The properties you use to configure an accordion fold transition filter.
- [CICopyMachineTransition](cicopymachinetransition.md) — The properties you use to configure a copy machine transition filter.
- [CIDisintegrateWithMaskTransition](cidisintegratewithmasktransition.md) — The properties you use to configure a disintegrate-with-mask transition filter.
- [CIDissolveTransition](cidissolvetransition.md) — The properties you use to configure a dissolve transition filter.
- [CIModTransition](cimodtransition.md) — The properties you use to configure a mod transition filter.
- [CIPageCurlTransition](cipagecurltransition.md) — The properties you use to configure a page curl transition filter.
- [CIPageCurlWithShadowTransition](cipagecurlwithshadowtransition.md) — The properties you use to configure a page-curl-with-shadow transition filter.
- [CIRippleTransition](cirippletransition.md) — The properties you use to configure a ripple transition filter.
- [CISwipeTransition](ciswipetransition.md) — The properties you use to configure a swipe transition filter.
