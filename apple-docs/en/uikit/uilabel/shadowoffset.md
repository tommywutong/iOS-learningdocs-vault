---
title: shadowOffset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/shadowoffset
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/shadowoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/shadowoffset.json'
content_hash: 'sha256:a69ce75e8f8600d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# shadowOffset

<sub>Instance Property</sub>

The shadow offset, in points, for the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var shadowOffset: CGSize { get set }
```

## Discussion

The shadow color must be not be `nil` for this property to have any effect. The default offset size is `(0, -1)`, which indicates a shadow one point above the text. A label draws its text shadows with the specified offset and color and no blurring.

## See Also

### Drawing a shadow

- [shadowColor](shadowcolor.md) — The shadow color of the text.
