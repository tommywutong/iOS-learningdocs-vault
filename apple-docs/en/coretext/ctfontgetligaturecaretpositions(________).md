---
title: 'CTFontGetLigatureCaretPositions(_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontgetligaturecaretpositions(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontgetligaturecaretpositions(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontgetligaturecaretpositions%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:48856679d0bc2e76'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontGetLigatureCaretPositions(_:_:_:_:)

<sub>Function</sub>

Returns caret positions within a glyph.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontGetLigatureCaretPositions(_ font: CTFont, _ glyph: CGGlyph, _ positions: UnsafeMutablePointer<CGFloat>?, _ maxPositions: CFIndex) -> CFIndex
```

## Parameters

- `font` — A reference to the font to use.

- `glyph` — A reference to the glyph.

- `positions` — A buffer of at least `maxPositions` to receive the ligature caret positions for `glyph`.

- `maxPositions` — The maximum number of positions to return.

## Return Value

The maximum number of caret positions for the specified glyph

## Discussion

This function is used to obtain caret positions for a specific glyph. The return value is the maximum number of positions possible, and the function will populate the caller’s `positions` buffer with available positions if possible. This function might not be able to produce positions if the font does not have the appropriate data, in which case it will return 0.

## See Also

### Working with Glyphs

- [CTFontGetGlyphsForCharacters](<ctfontgetglyphsforcharacters(________).md>) — Performs basic character-to-glyph mapping.
- [CTFontDrawGlyphs](<ctfontdrawglyphs(__________).md>) — Renders the given glyphs of a font at the specified positions in the supplied graphics context.
