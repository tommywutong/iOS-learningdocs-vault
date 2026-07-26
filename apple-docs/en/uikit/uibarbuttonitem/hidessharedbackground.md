---
title: hidesSharedBackground
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitem/hidessharedbackground
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/hidessharedbackground'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/hidessharedbackground.json'
content_hash: 'sha256:91b46511bfbec9dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# hidesSharedBackground

<sub>Instance Property</sub>

A boolean value indicating whether the background this item may share with other items in the bar should be hidden.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var hidesSharedBackground: Bool { get set }
```

## Discussion

Set this property to `YES` to prevent the standard shared background (typically using the Glass effect) from being drawn behind this bar button item.

This item will not be visually grouped with any other items, without the standard shared background. This property is ignored if the item is in a `UIBarButtonItemGroup` with more than one item. The default value is `NO`.

## See Also

### Customizing placement in a toolbar

- [sharesBackground](sharesbackground.md) — A boolean value indicating whether this bar button item can share a background with other items in a navigation bar or a toolbar.
