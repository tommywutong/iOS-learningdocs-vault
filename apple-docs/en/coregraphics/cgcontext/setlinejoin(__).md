---
title: 'setLineJoin(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/setlinejoin(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/setlinejoin(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/setlinejoin%28_%3A%29.json'
content_hash: 'sha256:9de090131ab706ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setLineJoin(_:)

<sub>Instance Method</sub>

Sets the style for the joins of connected lines in a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setLineJoin(_ join: CGLineJoin)
```

## Parameters

- `join` — A line join value—[kCGLineJoinMiter](../cglinejoin/miter.md) (the default), [kCGLineJoinRound](../cglinejoin/round.md), or [kCGLineJoinBevel](../cglinejoin/bevel.md). See [CGPath](../cgpath.md).

## See Also

### Setting Path Drawing Options

- [CGContextSetAllowsAntialiasing](<setallowsantialiasing(__).md>) — Sets whether or not to allow antialiasing for a graphics context.
- [CGContextSetFlatness](<setflatness(__).md>) — Sets the accuracy of curved paths in a graphics context.
- [CGContextSetLineCap](<setlinecap(__).md>) — Sets the style for the endpoints of lines drawn in a graphics context.
- [setLineDash(phase:lengths:)](<setlinedash(phase_lengths_).md>) — Sets the pattern for drawing dashed lines.
- [CGContextSetLineWidth](<setlinewidth(__).md>) — Sets the line width for a graphics context.
- [CGContextSetMiterLimit](<setmiterlimit(__).md>) — Sets the miter limit for the joins of connected lines in a graphics context.
- [CGContextSetPatternPhase](<setpatternphase(__).md>) — Sets the pattern phase of a context.
- [CGContextSetFillPattern](<setfillpattern(__colorcomponents_).md>) — Sets the fill pattern in the specified graphics context.
- [CGContextSetShouldAntialias](<setshouldantialias(__).md>) — Sets antialiasing on or off for a graphics context.
