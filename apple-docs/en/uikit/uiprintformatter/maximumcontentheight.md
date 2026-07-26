---
title: maximumContentHeight
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintformatter/maximumcontentheight
source_url: 'https://developer.apple.com/documentation/uikit/uiprintformatter/maximumcontentheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintformatter/maximumcontentheight.json'
content_hash: 'sha256:2d7f98e4274b7720'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintFormatter](../uiprintformatter.md)

# maximumContentHeight

<sub>Instance Property</sub>

The maximum height of the content area.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var maximumContentHeight: CGFloat { get set }
```

## Discussion

`UIPrintFormatter` uses this value to determine where the content rectangle begins on the first page. It compares the value of this property with the printing rectangle’s height minus the header and footer heights and the top inset value (of [contentInsets](contentinsets.md)); it uses the lower of the two values. The default value of this property is the maximum float value.

## See Also

### Laying out the content

- [perPageContentInsets](perpagecontentinsets.md) — The margins for each printed page.
- [maximumContentWidth](maximumcontentwidth.md) — The maximum width of the content area.
- [contentInsets](contentinsets.md) — The distances the edges of content are inset from the printing rectangle. _(deprecated)_
