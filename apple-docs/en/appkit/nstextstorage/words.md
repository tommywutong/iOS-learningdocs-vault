---
title: words
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstextstorage/words
source_url: 'https://developer.apple.com/documentation/appkit/nstextstorage/words'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextstorage/words.json'
content_hash: 'sha256:562ae88275d6cfeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextStorage](../nstextstorage.md)

# words

<sub>Instance Property</sub>

The text storage contents as an array of words.

<sub>macOS</sub>

```swift
var words: [NSTextStorage] { get set }
```

## Discussion

Unless you’re dealing with scriptability, you shouldn’t use or modify this property directly.

## See Also

### Accessing scriptable properties

- [attributeRuns](attributeruns.md) — The text storage contents as an array of attribute runs.
- [paragraphs](paragraphs.md) — The text storage contents as an array of paragraphs.
- [characters](characters.md) — The text storage contents as an array of characters.
- [font](font.md) — The font for the text storage.
- [foregroundColor](foregroundcolor.md) — The color for the text.
