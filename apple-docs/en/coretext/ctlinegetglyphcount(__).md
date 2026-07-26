---
title: 'CTLineGetGlyphCount(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinegetglyphcount(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinegetglyphcount(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinegetglyphcount%28_%3A%29.json'
content_hash: 'sha256:1f193d9e4f27a2a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineGetGlyphCount(_:)

<sub>Function</sub>

Returns the total glyph count for the line object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineGetGlyphCount(_ line: CTLine) -> CFIndex
```

## Parameters

- `line` — The line whose glyph count is returned.

## Return Value

The total glyph count for the line passed in.

## Discussion

The total glyph count is equal to the sum of all of the glyphs in the glyph runs forming the line.

## See Also

### Getting Line Data

- [CTLineGetGlyphRuns](<ctlinegetglyphruns(__).md>) — Returns the array of glyph runs that make up the line object.
- [CTLineGetStringRange](<ctlinegetstringrange(__).md>) — Gets the range of characters that originally spawned the glyphs in the line.
- [CTLineGetPenOffsetForFlush](<ctlinegetpenoffsetforflush(______).md>) — Gets the pen offset required to draw flush text.
