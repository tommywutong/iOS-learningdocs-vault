---
title: attributedSubtitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/attributedsubtitle-4474c
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/attributedsubtitle-4474c'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/attributedsubtitle-4474c.json'
content_hash: 'sha256:18274f074aa51694'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# attributedSubtitle

<sub>Instance Property</sub>

An attributed string to display as the subtitle in the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) NSAttributedString * attributedSubtitle;
```

## Discussion

If non-nil, this property takes precedence over the `subtitle` property. If `subtitleView` is non-nil, this property is ignored. If `titleView` is non-nil, this property is ignored.

## See Also

### Configuring the subtitle

- [subtitle](subtitle.md) — A string to display as the subtitle in the navigation bar.
- [largeSubtitle](largesubtitle.md) — String to be rendered below the large title.
- [largeAttributedSubtitle](largeattributedsubtitle-2c0pk.md) — An attributed string to be rendered below the large title.
