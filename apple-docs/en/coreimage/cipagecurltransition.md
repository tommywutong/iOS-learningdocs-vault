---
title: CIPageCurlTransition
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cipagecurltransition
source_url: 'https://developer.apple.com/documentation/coreimage/cipagecurltransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cipagecurltransition.json'
content_hash: 'sha256:82d0542808a5ead3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIPageCurlTransition

<sub>Protocol</sub>

The properties you use to configure a page curl transition filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIPageCurlTransition : CITransitionFilter
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md), [CITransitionFilter](citransitionfilter.md)

## Topics

### Instance Properties

- [angle](cipagecurltransition/angle.md) — The angle of the curling page.
- [backsideImage](cipagecurltransition/backsideimage.md) — The image that appears on the back of the source image as the page curls to reveal the target image.
- [extent](cipagecurltransition/extent.md) — The extent of the effect.
- [radius](cipagecurltransition/radius.md) — The radius of the curl.
- [shadingImage](cipagecurltransition/shadingimage.md) — An image that looks like a shaded sphere enclosed in a square.

## See Also

### Related Documentation

- [+ pageCurlTransitionFilter](<cifilter-swift.class/pagecurltransition().md>) — Simulates the curl of a page, revealing the target image.

### Protocols

- [CITransitionFilter](citransitionfilter.md) — The properties you use to configure a transition filter.
- [CIBarsSwipeTransition](cibarsswipetransition.md) — The properties you use to configure a bars swipe transition filter.
- [CIAccordionFoldTransition](ciaccordionfoldtransition.md) — The properties you use to configure an accordion fold transition filter.
- [CICopyMachineTransition](cicopymachinetransition.md) — The properties you use to configure a copy machine transition filter.
- [CIDisintegrateWithMaskTransition](cidisintegratewithmasktransition.md) — The properties you use to configure a disintegrate-with-mask transition filter.
- [CIDissolveTransition](cidissolvetransition.md) — The properties you use to configure a dissolve transition filter.
- [CIFlashTransition](ciflashtransition.md) — The properties you use to configure a flash transition filter.
- [CIModTransition](cimodtransition.md) — The properties you use to configure a mod transition filter.
- [CIPageCurlWithShadowTransition](cipagecurlwithshadowtransition.md) — The properties you use to configure a page-curl-with-shadow transition filter.
- [CIRippleTransition](cirippletransition.md) — The properties you use to configure a ripple transition filter.
- [CISwipeTransition](ciswipetransition.md) — The properties you use to configure a swipe transition filter.
