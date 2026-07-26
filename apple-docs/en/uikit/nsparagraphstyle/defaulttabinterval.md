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
doc_path: /documentation/uikit/nsparagraphstyle/defaulttabinterval
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/defaulttabinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/defaulttabinterval.json'
content_hash: 'sha256:00ac93c10d315d07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# defaultTabInterval

<sub>Instance Property</sub>

The documentwide default tab interval.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var defaultTabInterval: CGFloat { get }
```

## Discussion

This property represents the default tab interval in points. Tabs after the last specified in [tabStops](tabstops.md) are placed at integer multiples of this distance (if positive). Default value is 0.0.

## See Also

### Accessing tab information

- [tabStops](tabstops.md) — The text tab objects that represent the paragraph’s tab stops.
- [NSParagraphStyle.TextTabType](../../appkit/nsparagraphstyle/texttabtype.md) — Constants that specify the type of tab stop. _(deprecated)_
