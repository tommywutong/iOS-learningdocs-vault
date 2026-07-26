---
title: defaultTabInterval
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsmutableparagraphstyle/defaulttabinterval
source_url: 'https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/defaulttabinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsmutableparagraphstyle/defaulttabinterval.json'
content_hash: 'sha256:74b793d31774d969'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSMutableParagraphStyle](../nsmutableparagraphstyle.md)

# defaultTabInterval

<sub>Instance Property</sub>

A number used as the document’s default tab spacing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var defaultTabInterval: CGFloat { get set }
```

## Discussion

This property represents the default tab interval in points. The system places tabs after the last specified in [tabStops](<https://developer.apple.com/library/archive/#id(tabStops)>) at integer multiples of this distance (if positive). Default value is `0.0`.

## See Also

### Specifying tab information

- [- addTabStop:](<addtabstop(__).md>) — Adds the specified tab stop to the paragraph.
- [- removeTabStop:](<removetabstop(__).md>) — Removes the first text tab with a location and type equal to the specified tab stop.
- [tabStops](tabstops.md) — The text tab objects that represent the paragraph’s tab stops.
