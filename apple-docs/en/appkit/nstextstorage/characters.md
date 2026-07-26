---
title: characters
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstextstorage/characters
source_url: 'https://developer.apple.com/documentation/appkit/nstextstorage/characters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextstorage/characters.json'
content_hash: 'sha256:6dbb51bf2160ca48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextStorage](../nstextstorage.md)

# characters

<sub>Instance Property</sub>

The text storage contents as an array of characters.

<sub>macOS</sub>

```swift
var characters: [NSTextStorage] { get set }
```

## Discussion

Unless you’re dealing with scriptability, you shouldn’t use or modify this property directly. For indexed access to characters, use `NSAttributedString`’s [length](../../foundation/nsattributedstring/length.md) method to access the string, and `NSString`’s [character(at:)](<../../foundation/nsstring/character(at_).md>) method to access the individual characters.

## See Also

### Accessing scriptable properties

- [attributeRuns](attributeruns.md) — The text storage contents as an array of attribute runs.
- [paragraphs](paragraphs.md) — The text storage contents as an array of paragraphs.
- [words](words.md) — The text storage contents as an array of words.
- [font](font.md) — The font for the text storage.
- [foregroundColor](foregroundcolor.md) — The color for the text.
