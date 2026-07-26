---
title: CIDisintegrateWithMaskTransition
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidisintegratewithmasktransition
source_url: 'https://developer.apple.com/documentation/coreimage/cidisintegratewithmasktransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidisintegratewithmasktransition.json'
content_hash: 'sha256:8cd6551891c51054'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDisintegrateWithMaskTransition

<sub>Protocol</sub>

The properties you use to configure a disintegrate-with-mask transition filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIDisintegrateWithMaskTransition : CITransitionFilter
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md), [CITransitionFilter](citransitionfilter.md)

## Topics

### Instance Properties

- [maskImage](cidisintegratewithmasktransition/maskimage.md) — An image that defines the shape to use when disintegrating from the source to the target image.
- [shadowDensity](cidisintegratewithmasktransition/shadowdensity.md) — The density of the shadow the mask creates.
- [shadowOffset](cidisintegratewithmasktransition/shadowoffset.md) — The offset of the shadow the mask creates.
- [shadowRadius](cidisintegratewithmasktransition/shadowradius.md) — The radius of the shadow the mask creates.

## See Also

### Related Documentation

- [+ disintegrateWithMaskTransitionFilter](<cifilter-swift.class/disintegratewithmasktransition().md>) — Transitions between two images using a mask image.

### Protocols

- [CITransitionFilter](citransitionfilter.md) — The properties you use to configure a transition filter.
- [CIBarsSwipeTransition](cibarsswipetransition.md) — The properties you use to configure a bars swipe transition filter.
- [CIAccordionFoldTransition](ciaccordionfoldtransition.md) — The properties you use to configure an accordion fold transition filter.
- [CICopyMachineTransition](cicopymachinetransition.md) — The properties you use to configure a copy machine transition filter.
- [CIDissolveTransition](cidissolvetransition.md) — The properties you use to configure a dissolve transition filter.
- [CIFlashTransition](ciflashtransition.md) — The properties you use to configure a flash transition filter.
- [CIModTransition](cimodtransition.md) — The properties you use to configure a mod transition filter.
- [CIPageCurlTransition](cipagecurltransition.md) — The properties you use to configure a page curl transition filter.
- [CIPageCurlWithShadowTransition](cipagecurlwithshadowtransition.md) — The properties you use to configure a page-curl-with-shadow transition filter.
- [CIRippleTransition](cirippletransition.md) — The properties you use to configure a ripple transition filter.
- [CISwipeTransition](ciswipetransition.md) — The properties you use to configure a swipe transition filter.
