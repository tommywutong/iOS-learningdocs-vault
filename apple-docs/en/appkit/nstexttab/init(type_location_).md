---
title: 'init(type:location:)'
framework: AppKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nstexttab/init(type:location:)'
source_url: 'https://developer.apple.com/documentation/appkit/nstexttab/init(type:location:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstexttab/init%28type%3Alocation%3A%29.json'
content_hash: 'sha256:f8fd23c1c48272bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextTab](../nstexttab.md)

# init(type:location:)

<sub>Initializer</sub>

Initializes a newly allocated text tab with the specified alignment and location.

<sub>macOS</sub>

```swift
convenience init(type: NSParagraphStyle.TextTabType, location loc: CGFloat)
```

## Discussion

The location is relative to the back margin, based on the line sweep direction of the paragraph. The value in the `type` parameter can be any of the values described in [TextTabType](../nsparagraphstyle/texttabtype.md).

## See Also

### Deprecated

- [tabStopType](tabstoptype.md) — The text tab’s type of tab stop. _(deprecated)_
