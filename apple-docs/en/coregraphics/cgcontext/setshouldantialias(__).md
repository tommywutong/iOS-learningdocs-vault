---
title: 'setShouldAntialias(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/setshouldantialias(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/setshouldantialias(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/setshouldantialias%28_%3A%29.json'
content_hash: 'sha256:c4344d30681b9dfe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setShouldAntialias(_:)

<sub>Instance Method</sub>

Sets antialiasing on or off for a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setShouldAntialias(_ shouldAntialias: Bool)
```

## Parameters

- `shouldAntialias` — A Boolean value that specifies whether antialiasing should be turned on. Antialiasing is turned on by default when a window or bitmap context is created. It is turned off for other types of contexts.

## Discussion

Antialiasing is a graphics state parameter.

## See Also

### Setting Path Drawing Options

- [CGContextSetAllowsAntialiasing](<setallowsantialiasing(__).md>) — Sets whether or not to allow antialiasing for a graphics context.
- [CGContextSetFlatness](<setflatness(__).md>) — Sets the accuracy of curved paths in a graphics context.
- [CGContextSetLineCap](<setlinecap(__).md>) — Sets the style for the endpoints of lines drawn in a graphics context.
- [setLineDash(phase:lengths:)](<setlinedash(phase_lengths_).md>) — Sets the pattern for drawing dashed lines.
- [CGContextSetLineJoin](<setlinejoin(__).md>) — Sets the style for the joins of connected lines in a graphics context.
- [CGContextSetLineWidth](<setlinewidth(__).md>) — Sets the line width for a graphics context.
- [CGContextSetMiterLimit](<setmiterlimit(__).md>) — Sets the miter limit for the joins of connected lines in a graphics context.
- [CGContextSetPatternPhase](<setpatternphase(__).md>) — Sets the pattern phase of a context.
- [CGContextSetFillPattern](<setfillpattern(__colorcomponents_).md>) — Sets the fill pattern in the specified graphics context.
