---
title: 'CTLineGetStringRange(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinegetstringrange(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinegetstringrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinegetstringrange%28_%3A%29.json'
content_hash: 'sha256:55ccd3f11a39693e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineGetStringRange(_:)

<sub>Function</sub>

Gets the range of characters that originally spawned the glyphs in the line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineGetStringRange(_ line: CTLine) -> CFRange
```

## Parameters

- `line` — The line from which to obtain the string range.

## Return Value

A [CFRange](../corefoundation/cfrange.md) structure that contains the range over the backing store string that spawned the glyphs, or if the function fails for any reason, an empty range.

## See Also

### Getting Line Data

- [CTLineGetGlyphCount](<ctlinegetglyphcount(__).md>) — Returns the total glyph count for the line object.
- [CTLineGetGlyphRuns](<ctlinegetglyphruns(__).md>) — Returns the array of glyph runs that make up the line object.
- [CTLineGetPenOffsetForFlush](<ctlinegetpenoffsetforflush(______).md>) — Gets the pen offset required to draw flush text.
