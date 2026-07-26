---
title: 'CTFontGetGlyphsForCharacters(_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontgetglyphsforcharacters(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontgetglyphsforcharacters(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontgetglyphsforcharacters%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:2b55fc83df0f7823'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontGetGlyphsForCharacters(_:_:_:_:)

<sub>Function</sub>

Performs basic character-to-glyph mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontGetGlyphsForCharacters(_ font: CTFont, _ characters: UnsafePointer<UniChar>, _ glyphs: UnsafeMutablePointer<CGGlyph>, _ count: CFIndex) -> Bool
```

## Parameters

- `font` — The font reference.

- `characters` — An array of Unicode characters.

- `glyphs` — On output, points to an array of glyph values.

- `count` — The capacity of the character and glyph arrays.

## Return Value

`True` if the font could encode all Unicode characters; otherwise `False`.

## Discussion

Provides basic Unicode encoding for the given font, returning by reference an array of [CGGlyph](../coregraphics/cgglyph.md) values corresponding to a given array of Unicode characters for the given font.

If a glyph could not be encoded, a value of `0` is passed back at the corresponding index in the `glyphs` array and the function returns `False`. It is the responsibility of the caller to handle the Unicode properties of the input characters.

## See Also

### Working with Glyphs

- [CTFontDrawGlyphs](<ctfontdrawglyphs(__________).md>) — Renders the given glyphs of a font at the specified positions in the supplied graphics context.
- [CTFontGetLigatureCaretPositions](<ctfontgetligaturecaretpositions(________).md>) — Returns caret positions within a glyph.
