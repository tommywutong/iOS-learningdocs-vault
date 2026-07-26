---
title: potentialEDRHeadroom
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/potentialedrheadroom
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/potentialedrheadroom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/potentialedrheadroom.json'
content_hash: 'sha256:77c569bccf5cc5c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# potentialEDRHeadroom

<sub>Instance Property</sub>

The screen’s maximum headroom when displaying extended dynamic range content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var potentialEDRHeadroom: CGFloat { get }
```

## Discussion

_Headroom_ is the ratio of the luminance of the screen’s brightest white to the luminance of standard dynamic range (SDR) white, in the screen’s native color space. The screen’s maximum headroom can change depending on its configuration, such as when [referenceDisplayModeStatus](referencedisplaymodestatus-swift.property.md) changes.

You can query this property even when the screen isn’t displaying extended dynamic range (EDR) content.

## See Also

### Getting the reference display mode status

- [referenceDisplayModeStatus](referencedisplaymodestatus-swift.property.md) — The status of the screen’s reference display mode.
- [ReferenceDisplayModeStatus](referencedisplaymodestatus-swift.enum.md) — Describes a screen’s reference display mode status.
- [currentEDRHeadroom](currentedrheadroom.md) — The screen’s current headroom when displaying extended dynamic range content.
