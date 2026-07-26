---
title: 'setPatternPhase(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/setpatternphase(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/setpatternphase(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/setpatternphase%28_%3A%29.json'
content_hash: 'sha256:62e296e995581be5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setPatternPhase(_:)

<sub>Instance Method</sub>

Sets the pattern phase of a context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setPatternPhase(_ phase: CGSize)
```

## Parameters

- `phase` — A pattern phase, specified in user space.

## Discussion

The pattern phase is a translation that Core Graphics applies prior to drawing a pattern in the context. The pattern phase is part of the graphics state of a context, and the default pattern phase is `(0,0)`. Setting the pattern phase has the effect of temporarily changing the pattern matrix of any pattern you draw. For example, setting the context’s pattern phase to `(2,3)` has the effect of moving the start of pattern cell tiling to the point `(2,3)` in default user space.

## See Also

### Setting Path Drawing Options

- [CGContextSetAllowsAntialiasing](<setallowsantialiasing(__).md>) — Sets whether or not to allow antialiasing for a graphics context.
- [CGContextSetFlatness](<setflatness(__).md>) — Sets the accuracy of curved paths in a graphics context.
- [CGContextSetLineCap](<setlinecap(__).md>) — Sets the style for the endpoints of lines drawn in a graphics context.
- [setLineDash(phase:lengths:)](<setlinedash(phase_lengths_).md>) — Sets the pattern for drawing dashed lines.
- [CGContextSetLineJoin](<setlinejoin(__).md>) — Sets the style for the joins of connected lines in a graphics context.
- [CGContextSetLineWidth](<setlinewidth(__).md>) — Sets the line width for a graphics context.
- [CGContextSetMiterLimit](<setmiterlimit(__).md>) — Sets the miter limit for the joins of connected lines in a graphics context.
- [CGContextSetFillPattern](<setfillpattern(__colorcomponents_).md>) — Sets the fill pattern in the specified graphics context.
- [CGContextSetShouldAntialias](<setshouldantialias(__).md>) — Sets antialiasing on or off for a graphics context.
