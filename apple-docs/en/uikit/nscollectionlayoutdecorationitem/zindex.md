---
title: zIndex
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutdecorationitem/zindex
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutdecorationitem/zindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutdecorationitem/zindex.json'
content_hash: 'sha256:20228df808e934e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSCollectionLayoutDecorationItem](../nscollectionlayoutdecorationitem.md)

# zIndex

<sub>Instance Property</sub>

The vertical stacking order of the decoration item in relation to other items in the section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var zIndex: Int { get set }
```

## Discussion

The default value of this property is `0`, which means the decoration item appears below all other items in the section.
