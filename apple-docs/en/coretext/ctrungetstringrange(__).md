---
title: 'CTRunGetStringRange(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctrungetstringrange(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctrungetstringrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrungetstringrange%28_%3A%29.json'
content_hash: 'sha256:18dad470f41edecf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunGetStringRange(_:)

<sub>Function</sub>

Gets the range of characters that originally spawned the glyphs in the run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRunGetStringRange(_ run: CTRun) -> CFRange
```

## Parameters

- `run` — The run for which to access the string range.

## Return Value

The range of characters that originally spawned the glyphs, of if `run` is invalid, an empty range.

## See Also

### Getting Glyph Run Data

- [CTRunGetGlyphCount](<ctrungetglyphcount(__).md>) — Gets the glyph count for the run.
- [CTRunGetAttributes](<ctrungetattributes(__).md>) — Returns the attribute dictionary that was used to create the glyph run.
- [CTRunGetStatus](<ctrungetstatus(__).md>) — Returns the run’s status.
- [CTRunGetGlyphsPtr](<ctrungetglyphsptr(__).md>) — Returns a direct pointer for the glyph array stored in the run.
- [CTRunGetGlyphs](<ctrungetglyphs(______).md>) — Copies a range of glyphs into a user-provided buffer.
- [CTRunGetPositionsPtr](<ctrungetpositionsptr(__).md>) — Returns a direct pointer for the glyph position array stored in the run.
- [CTRunGetPositions](<ctrungetpositions(______).md>) — Copies a range of glyph positions into a user-provided buffer.
- [CTRunGetAdvancesPtr](<ctrungetadvancesptr(__).md>) — Returns a direct pointer for the glyph advance array stored in the run.
- [CTRunGetAdvances](<ctrungetadvances(______).md>) — Copies a range of glyph advances into a user-provided buffer.
- [CTRunGetStringIndicesPtr](<ctrungetstringindicesptr(__).md>) — Returns a direct pointer for the string indices stored in the run.
- [CTRunGetStringIndices](<ctrungetstringindices(______).md>) — Copies a range of string indices into a user-provided buffer.
