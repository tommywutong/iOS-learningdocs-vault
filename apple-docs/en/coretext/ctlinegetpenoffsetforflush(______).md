---
title: 'CTLineGetPenOffsetForFlush(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinegetpenoffsetforflush(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinegetpenoffsetforflush(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinegetpenoffsetforflush%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:172169f4750758d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineGetPenOffsetForFlush(_:_:_:)

<sub>Function</sub>

Gets the pen offset required to draw flush text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineGetPenOffsetForFlush(_ line: CTLine, _ flushFactor: CGFloat, _ flushWidth: Double) -> Double
```

## Parameters

- `line` — The line from which to obtain a flush position.

- `flushFactor` — Determines the type of flushness. A `flushFactor` of `0` or less indicates left flush. A `flushFactor` of `1.0` or more indicates right flush. Flush factors between `0` and `1.0` indicate varying degrees of center flush, with a value of `0.5` being totally center flush.

- `flushWidth` — Specifies the width to which the flushness operation should apply.

## Return Value

The offset from the current pen position for the flush operation.

## See Also

### Getting Line Data

- [CTLineGetGlyphCount](<ctlinegetglyphcount(__).md>) — Returns the total glyph count for the line object.
- [CTLineGetGlyphRuns](<ctlinegetglyphruns(__).md>) — Returns the array of glyph runs that make up the line object.
- [CTLineGetStringRange](<ctlinegetstringrange(__).md>) — Gets the range of characters that originally spawned the glyphs in the line.
