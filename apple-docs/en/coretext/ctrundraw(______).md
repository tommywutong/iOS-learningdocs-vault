---
title: 'CTRunDraw(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctrundraw(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctrundraw(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrundraw%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:5214ddc49d8cd888'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunDraw(_:_:_:)

<sub>Function</sub>

Draws a complete run or part of one.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRunDraw(_ run: CTRun, _ context: CGContext, _ range: CFRange)
```

## Parameters

- `run` — The run to draw.

- `context` — The context into which to draw the run.

- `range` — The portion of the run to draw. If the length of the range is set to `0`, then the draw operation continues from the start index of the range to the end of the run.

## Discussion

This is a convenience call, because the run could be drawn by accessing the glyphs. This call can leave the graphics context in any state and does not flush the context after the draw operation.

## See Also

### Drawing the Glyph Run

- [CTRunGetTextMatrix](<ctrungettextmatrix(__).md>) — Returns the text matrix needed to draw this run.
