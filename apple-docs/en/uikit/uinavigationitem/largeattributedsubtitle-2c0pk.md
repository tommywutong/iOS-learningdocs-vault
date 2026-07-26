---
title: largeAttributedSubtitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/largeattributedsubtitle-2c0pk
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/largeattributedsubtitle-2c0pk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/largeattributedsubtitle-2c0pk.json'
content_hash: 'sha256:5b1eeaa83620569c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# largeAttributedSubtitle

<sub>Instance Property</sub>

An attributed string to be rendered below the large title.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) NSAttributedString * largeAttributedSubtitle;
```

## Discussion

When `nil`, the navigation bar will fall back to the `largeSubtitle`. If a `largeSubtitleView` is set, this property is ignored.

## See Also

### Configuring the subtitle

- [subtitle](subtitle.md) — A string to display as the subtitle in the navigation bar.
- [attributedSubtitle](attributedsubtitle-4474c.md) — An attributed string to display as the subtitle in the navigation bar.
- [largeSubtitle](largesubtitle.md) — String to be rendered below the large title.
