---
title: CIRippleTransition
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirippletransition
source_url: 'https://developer.apple.com/documentation/coreimage/cirippletransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirippletransition.json'
content_hash: 'sha256:444c11a1311db2a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIRippleTransition

<sub>Protocol</sub>

The properties you use to configure a ripple transition filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIRippleTransition : CITransitionFilter
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md), [CITransitionFilter](citransitionfilter.md)

## Topics

### Instance Properties

- [center](cirippletransition/center.md) — The x and y position to use as the center of the effect.
- [extent](cirippletransition/extent.md) — A rectangle that defines the extent of the effect.
- [scale](cirippletransition/scale.md) — A value that determines whether the ripple starts as a bulge (a higher value) or a dimple (a lower value).
- [shadingImage](cirippletransition/shadingimage.md) — An image that looks like a shaded sphere enclosed in a square.
- [width](cirippletransition/width.md) — The width of the ripple.

## See Also

### Related Documentation

- [+ rippleTransitionFilter](<cifilter-swift.class/rippletransition().md>) — Simulates a ripple in a pond to transiton from one image to another.

### Protocols

- [CITransitionFilter](citransitionfilter.md) — The properties you use to configure a transition filter.
- [CIBarsSwipeTransition](cibarsswipetransition.md) — The properties you use to configure a bars swipe transition filter.
- [CIAccordionFoldTransition](ciaccordionfoldtransition.md) — The properties you use to configure an accordion fold transition filter.
- [CICopyMachineTransition](cicopymachinetransition.md) — The properties you use to configure a copy machine transition filter.
- [CIDisintegrateWithMaskTransition](cidisintegratewithmasktransition.md) — The properties you use to configure a disintegrate-with-mask transition filter.
- [CIDissolveTransition](cidissolvetransition.md) — The properties you use to configure a dissolve transition filter.
- [CIFlashTransition](ciflashtransition.md) — The properties you use to configure a flash transition filter.
- [CIModTransition](cimodtransition.md) — The properties you use to configure a mod transition filter.
- [CIPageCurlTransition](cipagecurltransition.md) — The properties you use to configure a page curl transition filter.
- [CIPageCurlWithShadowTransition](cipagecurlwithshadowtransition.md) — The properties you use to configure a page-curl-with-shadow transition filter.
- [CISwipeTransition](ciswipetransition.md) — The properties you use to configure a swipe transition filter.
