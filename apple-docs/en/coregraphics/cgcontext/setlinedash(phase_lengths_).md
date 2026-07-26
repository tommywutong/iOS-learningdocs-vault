---
title: 'setLineDash(phase:lengths:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/setlinedash(phase:lengths:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/setlinedash(phase:lengths:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/setlinedash%28phase%3Alengths%3A%29.json'
content_hash: 'sha256:a576e0c79b4b47d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setLineDash(phase:lengths:)

<sub>Instance Method</sub>

Sets the pattern for drawing dashed lines.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setLineDash(phase: CGFloat, lengths: [CGFloat])
```

## Parameters

- `phase` — A value that specifies how far into the dash pattern the line starts, in units of the user space. For example, a value of `0` draws a line starting with the beginning of a dash pattern, and a value of `3` means the line is drawn with the dash pattern starting at three units from its beginning.

- `lengths` — An array of values that specify the lengths, in user space coordinates, of the painted and unpainted segments  of the dash pattern. For example, the array `[2,3]` sets a dash pattern that alternates between a 2-unit-long painted segment and a 3-unit-long unpainted segment. The array `[1,3,4,2]` sets the pattern to a 1-unit painted segment, a 3-unit unpainted segment, a 4-unit painted segment, and a 2-unit unpainted segment.Pass an empty array to clear the dash pattern so that all stroke drawing in the context uses solid lines.

## See Also

### Setting Path Drawing Options

- [CGContextSetAllowsAntialiasing](<setallowsantialiasing(__).md>) — Sets whether or not to allow antialiasing for a graphics context.
- [CGContextSetFlatness](<setflatness(__).md>) — Sets the accuracy of curved paths in a graphics context.
- [CGContextSetLineCap](<setlinecap(__).md>) — Sets the style for the endpoints of lines drawn in a graphics context.
- [CGContextSetLineJoin](<setlinejoin(__).md>) — Sets the style for the joins of connected lines in a graphics context.
- [CGContextSetLineWidth](<setlinewidth(__).md>) — Sets the line width for a graphics context.
- [CGContextSetMiterLimit](<setmiterlimit(__).md>) — Sets the miter limit for the joins of connected lines in a graphics context.
- [CGContextSetPatternPhase](<setpatternphase(__).md>) — Sets the pattern phase of a context.
- [CGContextSetFillPattern](<setfillpattern(__colorcomponents_).md>) — Sets the fill pattern in the specified graphics context.
- [CGContextSetShouldAntialias](<setshouldantialias(__).md>) — Sets antialiasing on or off for a graphics context.
