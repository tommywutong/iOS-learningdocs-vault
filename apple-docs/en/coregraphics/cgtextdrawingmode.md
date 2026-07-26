---
title: CGTextDrawingMode
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgtextdrawingmode
source_url: 'https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgtextdrawingmode.json'
content_hash: 'sha256:b08db234958d29dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGTextDrawingMode

<sub>Enumeration</sub>

Modes for rendering text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGTextDrawingMode
```

## Overview

You provide a text drawing mode constant to the function [CGContextSetTextDrawingMode](<cgcontext/settextdrawingmode(__).md>) to set the current text drawing mode for a graphics context. Text drawing modes determine how Core Graphics renders individual glyphs onscreen. For example, you can set a text drawing mode to draw text filled in or outlined (stroked) or both. You can also create special effects with the text clipping drawing modes, such as clipping an image to a glyph shape.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGTextFill](cgtextdrawingmode/fill.md) — Perform a fill operation on the text.
- [kCGTextStroke](cgtextdrawingmode/stroke.md) — Perform a stroke operation on the text.
- [kCGTextFillStroke](cgtextdrawingmode/fillstroke.md) — Perform fill, then stroke operations on the text.
- [kCGTextInvisible](cgtextdrawingmode/invisible.md) — Do not draw the text, but do update the text position.
- [kCGTextFillClip](cgtextdrawingmode/fillclip.md) — Perform a fill operation, then intersect the text with the current clipping path.
- [kCGTextStrokeClip](cgtextdrawingmode/strokeclip.md) — Perform a stroke operation, then intersect the text with the current clipping path.
- [kCGTextFillStrokeClip](cgtextdrawingmode/fillstrokeclip.md) — Perform fill then stroke operations, then intersect the text with the current clipping path.
- [kCGTextClip](cgtextdrawingmode/clip.md) — Specifies to intersect the text with the current clipping path. This mode does not paint the text.

### Initializers

- [init(rawValue:)](<cgtextdrawingmode/init(rawvalue_).md>)

## See Also

### Drawing Text

- [CGContextGetTextMatrix](cgcontext/textmatrix.md) — Returns the current text matrix.
- [textPosition](cgcontext/textposition.md)
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
- [showGlyphs(_:at:)](<cgcontext/showglyphs(__at_).md>) — Draws a set of glyphs at a set of corresponding positions.
