---
title: paragraphs
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstextstorage/paragraphs
source_url: 'https://developer.apple.com/documentation/appkit/nstextstorage/paragraphs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextstorage/paragraphs.json'
content_hash: 'sha256:eb0211d738ada65b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextStorage](../nstextstorage.md)

# paragraphs

<sub>Instance Property</sub>

The text storage contents as an array of paragraphs.

<sub>macOS</sub>

```swift
var paragraphs: [NSTextStorage] { get set }
```

## Discussion

Unless you’re dealing with scriptability, you shouldn’t use or modify this property directly.

## See Also

### Accessing scriptable properties

- [attributeRuns](attributeruns.md) — The text storage contents as an array of attribute runs.
- [words](words.md) — The text storage contents as an array of words.
- [characters](characters.md) — The text storage contents as an array of characters.
- [font](font.md) — The font for the text storage.
- [foregroundColor](foregroundcolor.md) — The color for the text.
