---
title: attributedTitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/attributedtitle-9l8p2
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/attributedtitle-9l8p2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/attributedtitle-9l8p2.json'
content_hash: 'sha256:2fd6daa19897a736'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# attributedTitle

<sub>Instance Property</sub>

An attributed string that is rendered as the title in the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) NSAttributedString * attributedTitle;
```

## Discussion

If `titleView` is non-nil, this property is ignored.

## See Also

### Configuring the title

- [title](title.md) — The navigation item’s title that displays in the navigation bar.
- [largeTitle](largetitle.md) — String to be used as the large title.
- [largeTitleDisplayMode](largetitledisplaymode-swift.property.md) — The mode for displaying the title of the navigation bar.
- [LargeTitleDisplayMode](largetitledisplaymode-swift.enum.md) — Constants that indicate how to size the title of this item.
