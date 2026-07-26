---
title: heightAnchor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilayoutsupport/heightanchor
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutsupport/heightanchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutsupport/heightanchor.json'
content_hash: 'sha256:1b8890d40580760a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILayoutSupport](../uilayoutsupport.md)

# heightAnchor

<sub>Instance Property</sub>

A layout anchor representing the guide’s height.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var heightAnchor: NSLayoutDimension { get }
```

## Discussion

Use this anchor to create constraints with the guide’s height. You can only combine this anchor with other [NSLayoutDimension](../nslayoutdimension.md) anchors. For more information, see [NSLayoutAnchor](../nslayoutanchor.md).

## See Also

### Creating constraints using layout anchors

- [bottomAnchor](bottomanchor.md) — A layout anchor representing the guide’s bottom edge.
- [topAnchor](topanchor.md) — A layout anchor representing the guide’s top edge.
