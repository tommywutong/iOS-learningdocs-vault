---
title: 'CTFontDrawGlyphs(_:_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontdrawglyphs(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdrawglyphs(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdrawglyphs%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:1e4f30d672527dce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDrawGlyphs(_:_:_:_:_:)

<sub>Function</sub>

Renders the given glyphs of a font at the specified positions in the supplied graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontDrawGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>, _ positions: UnsafePointer<CGPoint>, _ count: Int, _ context: CGContext)
```

## Parameters

- `font` — The font with glyphs to render. If the font has a size or matrix attribute, `context` is set with these values.

- `glyphs` — The glyphs to be rendered. The glyphs should be the result of proper Unicode text layout operations (such as with `CTLine`). Functions such as [CTFontGetGlyphsForCharacters](<ctfontgetglyphsforcharacters(________).md>) do not perform any Unicode text layout.

- `positions` — The positions (origins) for each glyph in `glyphs`. The positions are in user space. The number of positions passed in must match the number of glyphs (in `glyphs`).

- `count` — The number of glyphs to be rendered from the `glyphs` array.

- `context` — The graphics context used to render the glyphs.

## Discussion

This function modifies graphics state including font, text size, and text matrix if these attributes are specified in `font`. These attributes are not restored.

## See Also

### Working with Glyphs

- [CTFontGetGlyphsForCharacters](<ctfontgetglyphsforcharacters(________).md>) — Performs basic character-to-glyph mapping.
- [CTFontGetLigatureCaretPositions](<ctfontgetligaturecaretpositions(________).md>) — Returns caret positions within a glyph.
