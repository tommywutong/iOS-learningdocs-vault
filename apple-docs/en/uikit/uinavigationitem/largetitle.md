---
title: largeTitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/largetitle
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/largetitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/largetitle.json'
content_hash: 'sha256:232af615ecad6e9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# largeTitle

<sub>Instance Property</sub>

String to be used as the large title.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var largeTitle: String? { get set }
```

## Discussion

When `nil`, the navigation bar will use the navigation item’s current title.

## See Also

### Configuring the title

- [title](title.md) — The navigation item’s title that displays in the navigation bar.
- [attributedTitle](attributedtitle-25fxb.md)
- [largeTitleDisplayMode](largetitledisplaymode-swift.property.md) — The mode for displaying the title of the navigation bar.
- [LargeTitleDisplayMode](largetitledisplaymode-swift.enum.md) — Constants that indicate how to size the title of this item.
