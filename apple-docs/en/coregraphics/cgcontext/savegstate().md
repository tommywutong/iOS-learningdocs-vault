---
title: saveGState()
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/savegstate()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/savegstate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/savegstate%28%29.json'
content_hash: 'sha256:e3164e47178541cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# saveGState()

<sub>Instance Method</sub>

Pushes a copy of the current graphics state onto the graphics state stack for the context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func saveGState()
```

## Discussion

Each graphics context maintains a stack of graphics states. Note that not all aspects of the current drawing environment are elements of the graphics state. For example, the current path is not considered part of the graphics state and is therefore not saved when you call this function. The graphics state parameters that _are_ saved are:

- CTM (current transformation matrix)
- clip region
- image interpolation quality
- line width
- line join
- miter limit
- line cap
- line dash
- flatness
- should anti-alias
- rendering intent
- fill color space
- stroke color space
- fill color
- stroke color
- alpha value
- font
- font size
- character spacing
- text drawing mode
- shadow parameters
- the pattern phase
- the font smoothing parameter
- blend mode

To restore your drawing environment to a previously saved state, you can use [CGContextRestoreGState](<restoregstate().md>).

## See Also

### Saving and Restoring Graphics State

- [CGContextRestoreGState](<restoregstate().md>) — Sets the current graphics state to the state most recently saved.
