---
title: 'init(forTextStyle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontmetrics/init(fortextstyle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontmetrics/init(fortextstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontmetrics/init%28fortextstyle%3A%29.json'
content_hash: 'sha256:3d8f0d32960ebc9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontMetrics](../uifontmetrics.md)

# init(forTextStyle:)

<sub>Initializer</sub>

Creates a font metrics object for the specified text style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(forTextStyle textStyle: UIFont.TextStyle)
```

## Parameters

- `textStyle` — The text style that you want to apply to the font. For example, you might specify [UIFontTextStyleBody](../uifont/textstyle/body.md) for your app’s main content.

## Return Value

An initialized font metrics object.

## See Also

### Creating a Font Metrics Object

- [defaultMetrics](default.md) — The default font metrics object for content.
- [TextStyle](../uifont/textstyle.md) — Constants that describe the preferred styles for fonts.
