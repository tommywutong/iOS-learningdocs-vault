---
title: topAnchor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilayoutsupport/topanchor
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutsupport/topanchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutsupport/topanchor.json'
content_hash: 'sha256:8ad2df79f1c472cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILayoutSupport](../uilayoutsupport.md)

# topAnchor

<sub>Instance Property</sub>

A layout anchor representing the guide’s top edge.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var topAnchor: NSLayoutYAxisAnchor { get }
```

## Discussion

Use this anchor to create constraints with the guide’s top edge. You can only combine this anchor with other [NSLayoutYAxisAnchor](../nslayoutyaxisanchor.md) anchors. For more information, see [NSLayoutAnchor](../nslayoutanchor.md).

## See Also

### Creating constraints using layout anchors

- [bottomAnchor](bottomanchor.md) — A layout anchor representing the guide’s bottom edge.
- [heightAnchor](heightanchor.md) — A layout anchor representing the guide’s height.
