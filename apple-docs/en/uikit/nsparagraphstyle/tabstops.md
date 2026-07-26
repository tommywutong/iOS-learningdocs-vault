---
title: tabStops
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsparagraphstyle/tabstops
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/tabstops'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/tabstops.json'
content_hash: 'sha256:8481029e9ed8736f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# tabStops

<sub>Instance Property</sub>

The text tab objects that represent the paragraph’s tab stops.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var tabStops: [NSTextTab] { get }
```

## Discussion

The [NSTextTab](../nstexttab.md) objects, sorted by location, define the tab stops for the paragraph style. The default value is an array of 12 left-aligned tabs at 28-point intervals.

## See Also

### Accessing tab information

- [NSParagraphStyle.TextTabType](../../appkit/nsparagraphstyle/texttabtype.md) — Constants that specify the type of tab stop. _(deprecated)_
- [defaultTabInterval](defaulttabinterval.md) — The documentwide default tab interval.
