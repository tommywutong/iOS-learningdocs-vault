---
title: tabStopType
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/appkit/nstexttab/tabstoptype
source_url: 'https://developer.apple.com/documentation/appkit/nstexttab/tabstoptype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstexttab/tabstoptype.json'
content_hash: 'sha256:e0cb650843c68009'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextTab](../nstexttab.md)

# tabStopType

<sub>Instance Property</sub>

The text tab’s type of tab stop.

> [!warning] Deprecated
> Use -alignment and -options.

<sub>macOS</sub>

```swift
var tabStopType: NSParagraphStyle.TextTabType { get }
```

## Discussion

Possible values are listed in [TextTabType](../nsparagraphstyle/texttabtype.md).

## See Also

### Deprecated

- [- initWithType:location:](<init(type_location_).md>) — Initializes a newly allocated text tab with the specified alignment and location. _(deprecated)_
