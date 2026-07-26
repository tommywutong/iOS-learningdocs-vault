---
title: contentInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+（10.0 起废弃）, iPadOS 4.2+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiprintformatter/contentinsets
source_url: 'https://developer.apple.com/documentation/uikit/uiprintformatter/contentinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintformatter/contentinsets.json'
content_hash: 'sha256:aa00beb5b75b74af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintFormatter](../uiprintformatter.md)

# contentInsets

<sub>Instance Property</sub>

The distances the edges of content are inset from the printing rectangle.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var contentInsets: UIEdgeInsets { get set }
```

## Discussion

This property adjusts the margins for content printed by the formatter. The printing rectangle defines the area the printer is capable of printing in; each inset is an inward distance, in points, from a side of the printing area. The top inset is used only on the first page that the formatter draws. The bottom inset is not used. You can use the [UIEdgeInsetsMake](<../uiedgeinsets/init(top_left_bottom_right_)-1s1t9.md>) macro to create a [UIEdgeInsets](../uiedgeinsets.md) structure.

The default value of this property is [UIEdgeInsetsZero](../uiedgeinsets/zero.md).

## See Also

### Laying out the content

- [perPageContentInsets](perpagecontentinsets.md) — The margins for each printed page.
- [maximumContentHeight](maximumcontentheight.md) — The maximum height of the content area.
- [maximumContentWidth](maximumcontentwidth.md) — The maximum width of the content area.
