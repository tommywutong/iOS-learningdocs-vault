---
title: font
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstextstorage/font
source_url: 'https://developer.apple.com/documentation/appkit/nstextstorage/font'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextstorage/font.json'
content_hash: 'sha256:a124725f5d421512'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextStorage](../nstextstorage.md)

# font

<sub>Instance Property</sub>

The font for the text storage.

<sub>macOS</sub>

```swift
var font: NSFont? { get set }
```

## Discussion

Unless you’re dealing with scriptability, you shouldn’t use or modify this property directly.

## See Also

### Accessing scriptable properties

- [attributeRuns](attributeruns.md) — The text storage contents as an array of attribute runs.
- [paragraphs](paragraphs.md) — The text storage contents as an array of paragraphs.
- [words](words.md) — The text storage contents as an array of words.
- [characters](characters.md) — The text storage contents as an array of characters.
- [foregroundColor](foregroundcolor.md) — The color for the text.
