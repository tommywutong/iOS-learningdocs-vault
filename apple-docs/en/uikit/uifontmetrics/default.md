---
title: default
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontmetrics/default
source_url: 'https://developer.apple.com/documentation/uikit/uifontmetrics/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontmetrics/default.json'
content_hash: 'sha256:b89d0882b296bc81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontMetrics](../uifontmetrics.md)

# default

<sub>Type Property</sub>

The default font metrics object for content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class var `default`: UIFontMetrics { get }
```

## Discussion

The font metrics object in this property uses the [UIFontTextStyleBody](../uifont/textstyle/body.md) style.

## See Also

### Creating a Font Metrics Object

- [- initForTextStyle:](<init(fortextstyle_).md>) — Creates a font metrics object for the specified text style.
- [TextStyle](../uifont/textstyle.md) — Constants that describe the preferred styles for fonts.
