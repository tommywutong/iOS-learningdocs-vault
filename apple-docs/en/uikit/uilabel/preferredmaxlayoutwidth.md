---
title: preferredMaxLayoutWidth
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/preferredmaxlayoutwidth
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/preferredmaxlayoutwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/preferredmaxlayoutwidth.json'
content_hash: 'sha256:3dbc1c55e00285ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# preferredMaxLayoutWidth

<sub>Instance Property</sub>

The preferred maximum width, in points, for a multiline label.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredMaxLayoutWidth: CGFloat { get set }
```

## Discussion

This property affects the size of the label when the system applies layout constraints to it. During layout, if the text extends beyond the width specified by this property, the additional text flows to one or more new lines, increasing the height of the label.
