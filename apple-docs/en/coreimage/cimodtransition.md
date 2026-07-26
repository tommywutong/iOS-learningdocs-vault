---
title: CIModTransition
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cimodtransition
source_url: 'https://developer.apple.com/documentation/coreimage/cimodtransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cimodtransition.json'
content_hash: 'sha256:0ca97b2e7a21ebae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIModTransition

<sub>Protocol</sub>

The properties you use to configure a mod transition filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIModTransition : CITransitionFilter
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md), [CITransitionFilter](citransitionfilter.md)

## Topics

### Instance Properties

- [angle](cimodtransition/angle.md) — The angle of the mod hole pattern.
- [center](cimodtransition/center.md) — The x and y position to use as the center of the effect.
- [compression](cimodtransition/compression.md) — The amount of stretching applied to the mod hole pattern.
- [radius](cimodtransition/radius.md) — The radius of the undistorted mod holes in the pattern.

## See Also

### Related Documentation

- [+ modTransitionFilter](<cifilter-swift.class/modtransition().md>) — Transitions between two images by applying irregularly shaped holes.

### Protocols

- [CITransitionFilter](citransitionfilter.md) — The properties you use to configure a transition filter.
- [CIBarsSwipeTransition](cibarsswipetransition.md) — The properties you use to configure a bars swipe transition filter.
- [CIAccordionFoldTransition](ciaccordionfoldtransition.md) — The properties you use to configure an accordion fold transition filter.
- [CICopyMachineTransition](cicopymachinetransition.md) — The properties you use to configure a copy machine transition filter.
- [CIDisintegrateWithMaskTransition](cidisintegratewithmasktransition.md) — The properties you use to configure a disintegrate-with-mask transition filter.
- [CIDissolveTransition](cidissolvetransition.md) — The properties you use to configure a dissolve transition filter.
- [CIFlashTransition](ciflashtransition.md) — The properties you use to configure a flash transition filter.
- [CIPageCurlTransition](cipagecurltransition.md) — The properties you use to configure a page curl transition filter.
- [CIPageCurlWithShadowTransition](cipagecurlwithshadowtransition.md) — The properties you use to configure a page-curl-with-shadow transition filter.
- [CIRippleTransition](cirippletransition.md) — The properties you use to configure a ripple transition filter.
- [CISwipeTransition](ciswipetransition.md) — The properties you use to configure a swipe transition filter.
