---
title: attributeRuns
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstextstorage/attributeruns
source_url: 'https://developer.apple.com/documentation/appkit/nstextstorage/attributeruns'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextstorage/attributeruns.json'
content_hash: 'sha256:b0eaa3bda39b2c58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextStorage](../nstextstorage.md)

# attributeRuns

<sub>Instance Property</sub>

The text storage contents as an array of attribute runs.

<sub>macOS</sub>

```swift
var attributeRuns: [NSTextStorage] { get set }
```

## Discussion

Unless you’re dealing with scriptability, you shouldn’t use or modify this property directly.

## See Also

### Accessing scriptable properties

- [paragraphs](paragraphs.md) — The text storage contents as an array of paragraphs.
- [words](words.md) — The text storage contents as an array of words.
- [characters](characters.md) — The text storage contents as an array of characters.
- [font](font.md) — The font for the text storage.
- [foregroundColor](foregroundcolor.md) — The color for the text.
