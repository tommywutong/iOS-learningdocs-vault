---
title: CIPageCurlWithShadowTransition
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cipagecurlwithshadowtransition
source_url: 'https://developer.apple.com/documentation/coreimage/cipagecurlwithshadowtransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cipagecurlwithshadowtransition.json'
content_hash: 'sha256:e2729890ebe8dc05'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIPageCurlWithShadowTransition

<sub>Protocol</sub>

The properties you use to configure a page-curl-with-shadow transition filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIPageCurlWithShadowTransition : CITransitionFilter
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md), [CITransitionFilter](citransitionfilter.md)

## Topics

### Instance Properties

- [angle](cipagecurlwithshadowtransition/angle.md) — The angle of the curling page.
- [backsideImage](cipagecurlwithshadowtransition/backsideimage.md) — The image that appears on the back of the source image as the page curls to reveal the target image.
- [extent](cipagecurlwithshadowtransition/extent.md) — The extent of the effect.
- [radius](cipagecurlwithshadowtransition/radius.md) — The radius of the curl.
- [shadowAmount](cipagecurlwithshadowtransition/shadowamount.md) — The strength of the shadow.
- [shadowExtent](cipagecurlwithshadowtransition/shadowextent.md) — The rectagular portion of input image that casts a shadow.
- [shadowSize](cipagecurlwithshadowtransition/shadowsize.md) — The maximum size, in pixels, of the shadow.

## See Also

### Related Documentation

- [+ pageCurlWithShadowTransitionFilter](<cifilter-swift.class/pagecurlwithshadowtransition().md>) — Simulates the curl of a page, revealing the target image with added shadow.

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
- [CIRippleTransition](cirippletransition.md) — The properties you use to configure a ripple transition filter.
- [CISwipeTransition](ciswipetransition.md) — The properties you use to configure a swipe transition filter.
