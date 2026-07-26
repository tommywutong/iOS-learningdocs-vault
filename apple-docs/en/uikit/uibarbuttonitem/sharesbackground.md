---
title: sharesBackground
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitem/sharesbackground
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/sharesbackground'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/sharesbackground.json'
content_hash: 'sha256:8c1473baa1de998c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# sharesBackground

<sub>Instance Property</sub>

A boolean value indicating whether this bar button item can share a background with other items in a navigation bar or a toolbar.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var sharesBackground: Bool { get set }
```

## Discussion

When `NO`, This item will not be visually grouped with any other items.

This property is ignored if the item is in a `UIBarButtonItemGroup` with more than one item. The default value is `YES`.

## See Also

### Customizing placement in a toolbar

- [hidesSharedBackground](hidessharedbackground.md) — A boolean value indicating whether the background this item may share with other items in the bar should be hidden.
