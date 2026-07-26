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
doc_path: /documentation/uikit/nsmutableparagraphstyle/tabstops
source_url: 'https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/tabstops'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsmutableparagraphstyle/tabstops.json'
content_hash: 'sha256:0e3fce56a09bfc1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSMutableParagraphStyle](../nsmutableparagraphstyle.md)

# tabStops

<sub>Instance Property</sub>

The text tab objects that represent the paragraph’s tab stops.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var tabStops: [NSTextTab]! { get set }
```

## Discussion

The [NSTextTab](../nstexttab.md) objects, sorted by location, define the tab stops for the paragraph style. The default value is an array of 12 left-aligned tabs at 28-point intervals.

## See Also

### Specifying tab information

- [- addTabStop:](<addtabstop(__).md>) — Adds the specified tab stop to the paragraph.
- [- removeTabStop:](<removetabstop(__).md>) — Removes the first text tab with a location and type equal to the specified tab stop.
- [defaultTabInterval](defaulttabinterval.md) — A number used as the document’s default tab spacing.
