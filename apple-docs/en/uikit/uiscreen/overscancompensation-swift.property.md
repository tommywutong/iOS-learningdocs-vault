---
title: overscanCompensation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/overscancompensation-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/overscancompensation-swift.property.json'
content_hash: 'sha256:602cbcfddbbd6c05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# overscanCompensation

<sub>Instance Property</sub>

For an external screen, this property sets the desired technique to compensate for overscan.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var overscanCompensation: UIScreen.OverscanCompensation { get set }
```

## Discussion

Some external displays may be unable to reliably display all of the pixels to the user. To compensate, choose one of the techniques described in the  [OverscanCompensation](overscancompensation-swift.enum.md) enumeration.

## See Also

### Managing overscan compensation

- [overscanCompensationInsets](overscancompensationinsets.md) — The edge inset values needed to avoid clipping the rectangle.
- [OverscanCompensation](overscancompensation-swift.enum.md) — Describes different techniques for compensating for pixel loss at the edge of the screen.
