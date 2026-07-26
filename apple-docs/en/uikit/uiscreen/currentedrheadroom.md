---
title: currentEDRHeadroom
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/currentedrheadroom
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/currentedrheadroom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/currentedrheadroom.json'
content_hash: 'sha256:4d176abe6e21bded'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# currentEDRHeadroom

<sub>Instance Property</sub>

The screen’s current headroom when displaying extended dynamic range content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var currentEDRHeadroom: CGFloat { get }
```

## Discussion

_Headroom_ is the ratio of the luminance of the screen’s brightest white to the luminance of standard dynamic range (SDR) white, in the screen’s native color space. The screen’s current headroom limits all rendered content, and can change depending on its configuration and whether it’s displaying extended dynamic range (EDR) content.

To display EDR content in a [CAMetalLayer](../../quartzcore/cametallayer.md), set the layer’s [wantsExtendedDynamicRangeContent](../../quartzcore/cametallayer/wantsextendeddynamicrangecontent.md) property to [true](../../swift/true.md).

## See Also

### Getting the reference display mode status

- [referenceDisplayModeStatus](referencedisplaymodestatus-swift.property.md) — The status of the screen’s reference display mode.
- [ReferenceDisplayModeStatus](referencedisplaymodestatus-swift.enum.md) — Describes a screen’s reference display mode status.
- [potentialEDRHeadroom](potentialedrheadroom.md) — The screen’s maximum headroom when displaying extended dynamic range content.
