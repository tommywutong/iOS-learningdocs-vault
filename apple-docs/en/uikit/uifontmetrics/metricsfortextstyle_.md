---
title: 'metricsForTextStyle:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontmetrics/metricsfortextstyle:'
source_url: 'https://developer.apple.com/documentation/uikit/uifontmetrics/metricsfortextstyle:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontmetrics/metricsfortextstyle%3A.json'
content_hash: 'sha256:055e74428bd07f9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontMetrics](../uifontmetrics.md)

# metricsForTextStyle:

<sub>Type Method</sub>

Creates and returns a font metrics object for the specified text style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) metricsForTextStyle:(UIFontTextStyle) textStyle;
```

## Parameters

- `textStyle` — The text style that you want to apply to the font. For example, you might specify [UIFontTextStyleBody](../uifont/textstyle/body.md) for your app’s main content.

## Return Value

An initialized font metrics object.

## See Also

### Creating a Font Metrics Object

- [- initForTextStyle:](<init(fortextstyle_).md>) — Creates a font metrics object for the specified text style.
- [defaultMetrics](default.md) — The default font metrics object for content.
- [TextStyle](../uifont/textstyle.md) — Constants that describe the preferred styles for fonts.
