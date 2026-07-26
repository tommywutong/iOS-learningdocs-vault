---
title: 'setAllowsAntialiasing(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/setallowsantialiasing(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/setallowsantialiasing(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/setallowsantialiasing%28_%3A%29.json'
content_hash: 'sha256:71bf094f1af988ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setAllowsAntialiasing(_:)

<sub>Instance Method</sub>

Sets whether or not to allow antialiasing for a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setAllowsAntialiasing(_ allowsAntialiasing: Bool)
```

## Parameters

- `allowsAntialiasing` — A Boolean value that specifies whether or not to allow antialiasing. Pass `true` to allow antialiasing; `false` otherwise. This parameter is not part of the graphics state.

## Discussion

Core Graphics performs antialiasing for a graphics context if both the `allowsAntialiasing` parameter and the graphics state parameter `shouldAntialias` are `true`.

This parameter is not part of the graphics state.

## See Also

### Setting Path Drawing Options

- [CGContextSetFlatness](<setflatness(__).md>) — Sets the accuracy of curved paths in a graphics context.
- [CGContextSetLineCap](<setlinecap(__).md>) — Sets the style for the endpoints of lines drawn in a graphics context.
- [setLineDash(phase:lengths:)](<setlinedash(phase_lengths_).md>) — Sets the pattern for drawing dashed lines.
- [CGContextSetLineJoin](<setlinejoin(__).md>) — Sets the style for the joins of connected lines in a graphics context.
- [CGContextSetLineWidth](<setlinewidth(__).md>) — Sets the line width for a graphics context.
- [CGContextSetMiterLimit](<setmiterlimit(__).md>) — Sets the miter limit for the joins of connected lines in a graphics context.
- [CGContextSetPatternPhase](<setpatternphase(__).md>) — Sets the pattern phase of a context.
- [CGContextSetFillPattern](<setfillpattern(__colorcomponents_).md>) — Sets the fill pattern in the specified graphics context.
- [CGContextSetShouldAntialias](<setshouldantialias(__).md>) — Sets antialiasing on or off for a graphics context.
