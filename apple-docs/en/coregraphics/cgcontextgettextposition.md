---
title: CGContextGetTextPosition
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextgettextposition
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextgettextposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextgettextposition.json'
content_hash: 'sha256:e45c1e6654d8feeb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextGetTextPosition

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGPoint CGContextGetTextPosition(CGContextRef c);
```

## See Also

### Drawing Text

- [CGContextGetTextMatrix](cgcontext/textmatrix.md) — Returns the current text matrix.
- [CGContextSetTextMatrix](cgcontextsettextmatrix.md) — Sets the current text matrix.
- [CGContextSetTextPosition](cgcontextsettextposition.md) — Sets the location at which text is drawn.
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
- [CGContextShowGlyphs](<cgcontext/showglyphs(g_count_).md>) — Displays an array of glyphs at the current text position. _(deprecated)_
