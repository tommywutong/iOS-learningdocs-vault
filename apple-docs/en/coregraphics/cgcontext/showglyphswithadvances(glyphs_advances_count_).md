---
title: 'showGlyphsWithAdvances(glyphs:advances:count:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgcontext/showglyphswithadvances(glyphs:advances:count:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/showglyphswithadvances(glyphs:advances:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/showglyphswithadvances%28glyphs%3Aadvances%3Acount%3A%29.json'
content_hash: 'sha256:a124f0607fa1ff61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# showGlyphsWithAdvances(glyphs:advances:count:)

<sub>Instance Method</sub>

Draws an array of glyphs with varying offsets.

> [!warning] Deprecated
> Use [Core Text](../../coretext.md) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func showGlyphsWithAdvances(glyphs: UnsafePointer<CGGlyph>?, advances: UnsafePointer<CGSize>?, count: Int)
```

## Parameters

- `glyphs` — An array of glyphs.

- `advances` — An array of offset values associated with each glyph in the array. Each value specifies the offset from the previous glyph’s origin to the origin of the corresponding glyph. Offsets are specified in user space.

- `count` — The number of glyphs in the specified array.

## Discussion

This function draws an array of glyphs at the current point specified by the text matrix.

## See Also

### Related Documentation

- [CGContextShowText](<showtext(string_length_).md>) — Displays a character array at the current text position, a point specified by the current text matrix. _(deprecated)_
- [CGContextShowTextAtPoint](<showtextatpoint(x_y_string_length_).md>) — Displays a character string at a position you specify. _(deprecated)_

### Drawing Text

- [CGContextGetTextMatrix](textmatrix.md) — Returns the current text matrix.
- [textPosition](textposition.md)
- [CGContextSelectFont](<selectfont(name_size_textencoding_).md>) — Sets the font and font size in a graphics context. _(deprecated)_
- [CGContextSetCharacterSpacing](<setcharacterspacing(__).md>) — Sets the current character spacing.
- [CGContextSetFont](<setfont(__).md>) — Sets the platform font in a graphics context.
- [CGContextSetFontSize](<setfontsize(__).md>) — Sets the current font size.
- [CGContextSetTextDrawingMode](<settextdrawingmode(__).md>) — Sets the current text drawing mode.
- [CGContextSetAllowsFontSmoothing](<setallowsfontsmoothing(__).md>) — Sets whether or not to allow font smoothing for a graphics context.
- [CGContextSetAllowsFontSubpixelPositioning](<setallowsfontsubpixelpositioning(__).md>) — Sets whether or not to allow subpixel positioning for a graphics context.
- [CGContextSetAllowsFontSubpixelQuantization](<setallowsfontsubpixelquantization(__).md>) — Sets whether or not to allow subpixel quantization for a graphics context.
- [CGContextSetShouldSmoothFonts](<setshouldsmoothfonts(__).md>) — Enables or disables font smoothing in a graphics context.
- [CGContextSetShouldSubpixelPositionFonts](<setshouldsubpixelpositionfonts(__).md>) — Enables or disables subpixel positioning in a graphics context.
- [CGContextSetShouldSubpixelQuantizeFonts](<setshouldsubpixelquantizefonts(__).md>) — Enables or disables subpixel quantization in a graphics context.
- [CGContextShowGlyphs](<showglyphs(g_count_).md>) — Displays an array of glyphs at the current text position. _(deprecated)_
- [showGlyphs(_:at:)](<showglyphs(__at_).md>) — Draws a set of glyphs at a set of corresponding positions.
