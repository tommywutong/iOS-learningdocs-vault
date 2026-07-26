---
title: CGContextSetLineDash
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextsetlinedash
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextsetlinedash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextsetlinedash.json'
content_hash: 'sha256:c84ed85b7990a108'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextSetLineDash

<sub>Function</sub>

Sets the pattern for dashed lines in a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGContextSetLineDash(CGContextRef c, CGFloat phase, const CGFloat *lengths, size_t count);
```

## Parameters

- `c` — The graphics context to modify.

- `phase` — A value that specifies how far into the dash pattern the line starts, in units of the user space. For example, passing a value of `3` means the line is drawn with the dash pattern starting at three units from its beginning. Passing a value of `0` draws a line starting with the beginning of a dash pattern.

- `lengths` — An array of values that specify the lengths of the painted segments and unpainted segments, respectively, of the dash pattern—or `NULL` for no dash pattern. For example, passing an array with the values `[2,3]` sets a dash pattern that alternates between a 2-user-space-unit-long painted segment and a 3-user-space-unit-long unpainted segment. Passing the values `[1,3,4,2]` sets the pattern to a 1-unit painted segment, a 3-unit unpainted segment, a 4-unit painted segment, and a 2-unit unpainted segment.

- `count` — If the `lengths` parameter specifies an array, pass the number of elements in the array. Otherwise, pass `0`.

## See Also

### Setting Path Drawing Options

- [CGContextSetAllowsAntialiasing](<cgcontext/setallowsantialiasing(__).md>) — Sets whether or not to allow antialiasing for a graphics context.
- [CGContextSetFlatness](<cgcontext/setflatness(__).md>) — Sets the accuracy of curved paths in a graphics context.
- [CGContextSetLineCap](<cgcontext/setlinecap(__).md>) — Sets the style for the endpoints of lines drawn in a graphics context.
- [CGContextSetLineJoin](<cgcontext/setlinejoin(__).md>) — Sets the style for the joins of connected lines in a graphics context.
- [CGContextSetLineWidth](<cgcontext/setlinewidth(__).md>) — Sets the line width for a graphics context.
- [CGContextSetMiterLimit](<cgcontext/setmiterlimit(__).md>) — Sets the miter limit for the joins of connected lines in a graphics context.
- [CGContextSetPatternPhase](<cgcontext/setpatternphase(__).md>) — Sets the pattern phase of a context.
- [CGContextSetFillPattern](<cgcontext/setfillpattern(__colorcomponents_).md>) — Sets the fill pattern in the specified graphics context.
- [CGContextSetShouldAntialias](<cgcontext/setshouldantialias(__).md>) — Sets antialiasing on or off for a graphics context.
