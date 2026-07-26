---
title: perPageContentInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintformatter/perpagecontentinsets
source_url: 'https://developer.apple.com/documentation/uikit/uiprintformatter/perpagecontentinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintformatter/perpagecontentinsets.json'
content_hash: 'sha256:0894302fffd499e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintFormatter](../uiprintformatter.md)

# perPageContentInsets

<sub>Instance Property</sub>

The margins for each printed page.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var perPageContentInsets: UIEdgeInsets { get set }
```

## Discussion

This property specifies the margins to apply to each printed page. All margins are respected, so the top inset value represents the top margin of every page, the left inset value represents the left margin of every page, and so on. If the per-page insets are smaller than the printable area of the page, or smaller than the printable area after the values in the [contentInsets](contentinsets.md) property are applied, the value in this property is effectively ignored.

The default value of this property is [UIEdgeInsetsZero](../uiedgeinsets/zero.md).

## See Also

### Laying out the content

- [maximumContentHeight](maximumcontentheight.md) — The maximum height of the content area.
- [maximumContentWidth](maximumcontentwidth.md) — The maximum width of the content area.
- [contentInsets](contentinsets.md) — The distances the edges of content are inset from the printing rectangle. _(deprecated)_
