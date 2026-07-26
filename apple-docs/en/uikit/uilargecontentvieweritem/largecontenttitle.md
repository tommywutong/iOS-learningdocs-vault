---
title: largeContentTitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilargecontentvieweritem/largecontenttitle
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentvieweritem/largecontenttitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentvieweritem/largecontenttitle.json'
content_hash: 'sha256:9c17702a374d5aa5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILargeContentViewerItem](../uilargecontentvieweritem.md)

# largeContentTitle

<sub>Instance Property</sub>

A string that describes an item to display in the large content viewer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var largeContentTitle: String? { get }
```

## Discussion

To present content in the large content viewer, you can provide either [largeContentTitle](largecontenttitle.md) or [largeContentImage](largecontentimage.md), or both.

This property defaults to an appropriate value for UIKit classes, otherwise `nil`.

## See Also

### Configuring display properties

- [largeContentImage](largecontentimage.md) — An image that represents an item to display in the large content viewer.
- [largeContentImageInsets](largecontentimageinsets.md) — Insets to adjust the position of the item’s image so it appears visually centered in the large content viewer.
- [scalesLargeContentImage](scaleslargecontentimage.md) — A Boolean value that indicates whether the view scales the item’s image to a larger size or not.
