---
title: 'setCharacterSpacing(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/setcharacterspacing(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/setcharacterspacing(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/setcharacterspacing%28_%3A%29.json'
content_hash: 'sha256:b2da9de538884815'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setCharacterSpacing(_:)

<sub>Instance Method</sub>

Sets the current character spacing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setCharacterSpacing(_ spacing: CGFloat)
```

## Parameters

- `spacing` — A value that represents the amount of additional space to place between glyphs, in text space coordinates.

## Discussion

Core Graphics adds the additional space to the advance between the origin of one character and the origin of the next character. For information about the text coordinate system, see [CGContextSetTextMatrix](../cgcontextsettextmatrix.md).

## See Also

### Drawing Text

- [CGContextGetTextMatrix](textmatrix.md) — Returns the current text matrix.
- [textPosition](textposition.md)
- [CGContextSelectFont](<selectfont(name_size_textencoding_).md>) — Sets the font and font size in a graphics context. _(deprecated)_
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
- [CGContextShowGlyphsAtPoint](<showglyphsatpoint(x_y_glyphs_count_).md>) — Displays an array of glyphs at a position you specify. _(deprecated)_
