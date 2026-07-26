---
title: largeContentImageInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilargecontentvieweritem/largecontentimageinsets
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentvieweritem/largecontentimageinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentvieweritem/largecontentimageinsets.json'
content_hash: 'sha256:460703c923a98fe9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILargeContentViewerItem](../uilargecontentvieweritem.md)

# largeContentImageInsets

<sub>Instance Property</sub>

Insets to adjust the position of the item’s image so it appears visually centered in the large content viewer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var largeContentImageInsets: UIEdgeInsets { get }
```

## Discussion

This property defaults to [UIEdgeInsetsZero](../uiedgeinsets/zero.md).

## See Also

### Configuring display properties

- [largeContentTitle](largecontenttitle.md) — A string that describes an item to display in the large content viewer.
- [largeContentImage](largecontentimage.md) — An image that represents an item to display in the large content viewer.
- [scalesLargeContentImage](scaleslargecontentimage.md) — A Boolean value that indicates whether the view scales the item’s image to a larger size or not.
