---
title: CGContextShowGlyphsAtPositions
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextshowglyphsatpositions
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextshowglyphsatpositions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextshowglyphsatpositions.json'
content_hash: 'sha256:4fe7873af4f628eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextShowGlyphsAtPositions

<sub>Function</sub>

Draws glyphs at the provided position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGContextShowGlyphsAtPositions(CGContextRef c, const CGGlyph *glyphs, const CGPoint *Lpositions, size_t count);
```

## Parameters

- `c` — The graphics context in which to display the glyphs.

- `glyphs` — An array of glyphs.

- `Lpositions` — The positions for the glyphs. Each item in this array matches with the glyph at the corresponding index in the `glyphs` array. The position of each glyph is specified in text space, and, as a consequence, is transformed through the text matrix to user space.

- `count` — The number of items in the `glyphs` array.

## See Also

### Drawing Text

- [CGContextGetTextMatrix](cgcontext/textmatrix.md) — Returns the current text matrix.
- [CGContextSetTextMatrix](cgcontextsettextmatrix.md) — Sets the current text matrix.
- [CGContextSetTextPosition](cgcontextsettextposition.md) — Sets the location at which text is drawn.
- [CGContextGetTextPosition](cgcontextgettextposition.md)
- [CGContextSelectFont](<cgcontext/selectfont(name_size_textencoding_).md>) — Sets the font and font size in a graphics context. _(deprecated)_
- [CGContextSetCharacterSpacing](<cgcontext/setcharacterspacing(__).md>) — Sets the current character spacing.
- [CGContextSetFont](<cgcontext/setfont(__).md>) — Sets the platform font in a graphics context.
- [CGContextSetFontSize](<cgcontext/setfontsize(__).md>) — Sets the current font size.
- [CGContextSetTextDrawingMode](<cgcontext/settextdrawingmode(__).md>) — Sets the current text drawing mode.
- [CGContextSetAllowsFontSmoothing](<cgcontext/setallowsfontsmoothing(__).md>) — Sets whether or not to allow font smoothing for a graphics context.
- [CGContextSetAllowsFontSubpixelPositioning](<cgcontext/setallowsfontsubpixelpositioning(__).md>) — Sets whether or not to allow subpixel positioning for a graphics context.
- [CGContextSetAllowsFontSubpixelQuantization](<cgcontext/setallowsfontsubpixelquantization(__).md>) — Sets whether or not to allow subpixel quantization for a graphics context.
- [CGContextSetShouldSmoothFonts](<cgcontext/setshouldsmoothfonts(__).md>) — Enables or disables font smoothing in a graphics context.
- [CGContextSetShouldSubpixelPositionFonts](<cgcontext/setshouldsubpixelpositionfonts(__).md>) — Enables or disables subpixel positioning in a graphics context.
- [CGContextSetShouldSubpixelQuantizeFonts](<cgcontext/setshouldsubpixelquantizefonts(__).md>) — Enables or disables subpixel quantization in a graphics context.
