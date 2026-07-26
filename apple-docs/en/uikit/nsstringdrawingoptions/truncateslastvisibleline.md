---
title: truncatesLastVisibleLine
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsstringdrawingoptions/truncateslastvisibleline
source_url: 'https://developer.apple.com/documentation/uikit/nsstringdrawingoptions/truncateslastvisibleline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringdrawingoptions/truncateslastvisibleline.json'
content_hash: 'sha256:81bc27766acd0898'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSStringDrawingOptions](../nsstringdrawingoptions.md)

# truncatesLastVisibleLine

<sub>Type Property</sub>

Truncates and adds the ellipsis character to the last visible line if the text doesn’t fit into the specified bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static var truncatesLastVisibleLine: NSStringDrawingOptions { get }
```

## Discussion

This option is ignored if `NSStringDrawingUsesLineFragmentOrigin` is not also set. In addition, the line break mode must be either `NSLineBreakByWordWrapping` or `NSLineBreakByCharWrapping` for this option to take effect. The line break mode can be specified in a paragraph style passed in the attributes dictionary argument of the drawing methods.

## See Also

### Constants

- [NSStringDrawingUsesLineFragmentOrigin](useslinefragmentorigin.md) — Uses the line fragment origin instead of the baseline origin.
- [NSStringDrawingUsesFontLeading](usesfontleading.md) — Uses the font leading for calculating line heights.
- [NSStringDrawingUsesDeviceMetrics](usesdevicemetrics.md) — Uses image glyph bounds instead of typographic bounds.
