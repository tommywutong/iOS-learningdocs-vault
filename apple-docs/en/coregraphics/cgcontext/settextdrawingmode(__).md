---
title: 'setTextDrawingMode(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/settextdrawingmode(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/settextdrawingmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/settextdrawingmode%28_%3A%29.json'
content_hash: 'sha256:5b0fddbdb92f2011'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setTextDrawingMode(_:)

<sub>Instance Method</sub>

Sets the current text drawing mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setTextDrawingMode(_ mode: CGTextDrawingMode)
```

## Parameters

- `mode` — A text drawing mode (such as [kCGTextFill](../cgtextdrawingmode/fill.md) or [kCGTextStroke](../cgtextdrawingmode/stroke.md)) that specifies how Core Graphics renders individual glyphs in a graphics context. See [CGTextDrawingMode](../cgtextdrawingmode.md) for a complete list.

## See Also

### Drawing Text

- [CGContextGetTextMatrix](textmatrix.md) — Returns the current text matrix.
- [textPosition](textposition.md)
- [CGContextSelectFont](<selectfont(name_size_textencoding_).md>) — Sets the font and font size in a graphics context. _(deprecated)_
- [CGContextSetCharacterSpacing](<setcharacterspacing(__).md>) — Sets the current character spacing.
- [CGContextSetFont](<setfont(__).md>) — Sets the platform font in a graphics context.
- [CGContextSetFontSize](<setfontsize(__).md>) — Sets the current font size.
- [CGContextSetAllowsFontSmoothing](<setallowsfontsmoothing(__).md>) — Sets whether or not to allow font smoothing for a graphics context.
- [CGContextSetAllowsFontSubpixelPositioning](<setallowsfontsubpixelpositioning(__).md>) — Sets whether or not to allow subpixel positioning for a graphics context.
- [CGContextSetAllowsFontSubpixelQuantization](<setallowsfontsubpixelquantization(__).md>) — Sets whether or not to allow subpixel quantization for a graphics context.
- [CGContextSetShouldSmoothFonts](<setshouldsmoothfonts(__).md>) — Enables or disables font smoothing in a graphics context.
- [CGContextSetShouldSubpixelPositionFonts](<setshouldsubpixelpositionfonts(__).md>) — Enables or disables subpixel positioning in a graphics context.
- [CGContextSetShouldSubpixelQuantizeFonts](<setshouldsubpixelquantizefonts(__).md>) — Enables or disables subpixel quantization in a graphics context.
- [CGContextShowGlyphs](<showglyphs(g_count_).md>) — Displays an array of glyphs at the current text position. _(deprecated)_
- [showGlyphs(_:at:)](<showglyphs(__at_).md>) — Draws a set of glyphs at a set of corresponding positions.
- [CGContextShowGlyphsAtPoint](<showglyphsatpoint(x_y_glyphs_count_).md>) — Displays an array of glyphs at a position you specify. _(deprecated)_
