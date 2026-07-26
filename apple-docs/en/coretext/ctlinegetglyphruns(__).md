---
title: 'CTLineGetGlyphRuns(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinegetglyphruns(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinegetglyphruns(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinegetglyphruns%28_%3A%29.json'
content_hash: 'sha256:eb41ba5839929837'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineGetGlyphRuns(_:)

<sub>Function</sub>

Returns the array of glyph runs that make up the line object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineGetGlyphRuns(_ line: CTLine) -> CFArray
```

## Parameters

- `line` — The line whose glyph run array is returned.

## Return Value

A [CFArray](../corefoundation/cfarray.md) containing the CTRun objects that make up the line.

## See Also

### Getting Line Data

- [CTLineGetGlyphCount](<ctlinegetglyphcount(__).md>) — Returns the total glyph count for the line object.
- [CTLineGetStringRange](<ctlinegetstringrange(__).md>) — Gets the range of characters that originally spawned the glyphs in the line.
- [CTLineGetPenOffsetForFlush](<ctlinegetpenoffsetforflush(______).md>) — Gets the pen offset required to draw flush text.
