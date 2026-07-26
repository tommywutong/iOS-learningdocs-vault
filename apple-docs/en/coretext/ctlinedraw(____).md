---
title: 'CTLineDraw(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinedraw(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinedraw(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinedraw%28_%3A_%3A%29.json'
content_hash: 'sha256:0d413e4edbd485a5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineDraw(_:_:)

<sub>Function</sub>

Draws a complete line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineDraw(_ line: CTLine, _ context: CGContext)
```

## Parameters

- `line` — The line to draw.

- `context` — The context into which the line is drawn.

## Discussion

This is a convenience function because the line could be drawn run-by-run by getting the glyph runs, getting the glyphs out of them, and calling a function such as [CGContextShowGlyphsAtPositions](../coregraphics/cgcontextshowglyphsatpositions.md). This call can leave the graphics context in any state and does not flush the context after the draw operation.
