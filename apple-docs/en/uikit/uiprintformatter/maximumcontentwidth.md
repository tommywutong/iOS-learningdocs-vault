---
title: maximumContentWidth
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintformatter/maximumcontentwidth
source_url: 'https://developer.apple.com/documentation/uikit/uiprintformatter/maximumcontentwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintformatter/maximumcontentwidth.json'
content_hash: 'sha256:4ba922c59b4682ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintFormatter](../uiprintformatter.md)

# maximumContentWidth

<sub>Instance Property</sub>

The maximum width of the content area.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var maximumContentWidth: CGFloat { get set }
```

## Discussion

`UIPrintFormatter` uses this value to determine the maximum width of the content rectangle. It compares the value of this property with the printing rectangle’s width minus the left and right inset values and uses the lower of the two. The default value of this property is the maximum float value.

## See Also

### Laying out the content

- [perPageContentInsets](perpagecontentinsets.md) — The margins for each printed page.
- [maximumContentHeight](maximumcontentheight.md) — The maximum height of the content area.
- [contentInsets](contentinsets.md) — The distances the edges of content are inset from the printing rectangle. _(deprecated)_
