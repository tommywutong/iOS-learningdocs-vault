---
title: subtitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/subtitle
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/subtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/subtitle.json'
content_hash: 'sha256:db7791c07088cbb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# subtitle

<sub>Instance Property</sub>

A string to display as the subtitle in the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var subtitle: String? { get set }
```

## Discussion

If `attributedSubtitle` is `non-nil`, this property just returns the `String` representation of the `attributedString`. If `subtitleView` is non-nil, this property is ignored.

## See Also

### Configuring the subtitle

- [attributedSubtitle](attributedsubtitle-wrjk.md)
- [largeSubtitle](largesubtitle.md) — String to be rendered below the large title.
- [largeAttributedSubtitle](largeattributedsubtitle-4z2gx.md)
