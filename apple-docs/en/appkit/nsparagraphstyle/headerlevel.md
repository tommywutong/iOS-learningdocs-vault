---
title: headerLevel
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsparagraphstyle/headerlevel
source_url: 'https://developer.apple.com/documentation/appkit/nsparagraphstyle/headerlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsparagraphstyle/headerlevel.json'
content_hash: 'sha256:1ab6d1d20c15c569'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# headerLevel

<sub>Instance Property</sub>

The paragraph’s header level for HTML generation.

<sub>macOS</sub>

```swift
var headerLevel: Int { get }
```

## Discussion

If the paragraph isn’t a header, the value is `0`. If the paragraph is a header, the value ranges from `1` to `6`, depending on the header’s level.

The default value is `0`.
