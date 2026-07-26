---
title: 'setAllowsFontSubpixelQuantization(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/setallowsfontsubpixelquantization(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/setallowsfontsubpixelquantization(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/setallowsfontsubpixelquantization%28_%3A%29.json'
content_hash: 'sha256:c11ff891d235e250'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setAllowsFontSubpixelQuantization(_:)

<sub>Instance Method</sub>

Sets whether or not to allow subpixel quantization for a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setAllowsFontSubpixelQuantization(_ allowsFontSubpixelQuantization: Bool)
```

## Parameters

- `allowsFontSubpixelQuantization` — A Boolean value that specifies whether subpixel quantization of glyphs is allowed in the specified context.

## Discussion

Sub-pixel quantization is used by the graphics context if it is allowed, enabled, and if glyphs would be drawn at subpixel positions. For information on how to enable subpixel quantization, see the [CGContextSetShouldSubpixelQuantizeFonts](<setshouldsubpixelquantizefonts(__).md>) function.

This parameter is not part of the graphics state.

## See Also

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
- [CGContextSetShouldSmoothFonts](<setshouldsmoothfonts(__).md>) — Enables or disables font smoothing in a graphics context.
- [CGContextSetShouldSubpixelPositionFonts](<setshouldsubpixelpositionfonts(__).md>) — Enables or disables subpixel positioning in a graphics context.
- [CGContextSetShouldSubpixelQuantizeFonts](<setshouldsubpixelquantizefonts(__).md>) — Enables or disables subpixel quantization in a graphics context.
- [CGContextShowGlyphs](<showglyphs(g_count_).md>) — Displays an array of glyphs at the current text position. _(deprecated)_
- [showGlyphs(_:at:)](<showglyphs(__at_).md>) — Draws a set of glyphs at a set of corresponding positions.
- [CGContextShowGlyphsAtPoint](<showglyphsatpoint(x_y_glyphs_count_).md>) — Displays an array of glyphs at a position you specify. _(deprecated)_
