---
title: bottomAnchor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilayoutsupport/bottomanchor
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutsupport/bottomanchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutsupport/bottomanchor.json'
content_hash: 'sha256:b9fa2129fee3fb81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILayoutSupport](../uilayoutsupport.md)

# bottomAnchor

<sub>Instance Property</sub>

A layout anchor representing the guide’s bottom edge.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var bottomAnchor: NSLayoutYAxisAnchor { get }
```

## Discussion

Use this anchor to create constraints with the guide’s bottom edge. You can only combine this anchor with other [NSLayoutYAxisAnchor](../nslayoutyaxisanchor.md) anchors. For more information, see [NSLayoutAnchor](../nslayoutanchor.md).

## See Also

### Creating constraints using layout anchors

- [heightAnchor](heightanchor.md) — A layout anchor representing the guide’s height.
- [topAnchor](topanchor.md) — A layout anchor representing the guide’s top edge.
