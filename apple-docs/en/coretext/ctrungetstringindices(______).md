---
title: 'CTRunGetStringIndices(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctrungetstringindices(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctrungetstringindices(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrungetstringindices%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:406ef37f25f06c9d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunGetStringIndices(_:_:_:)

<sub>Function</sub>

Copies a range of string indices into a user-provided buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRunGetStringIndices(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CFIndex>)
```

## Parameters

- `run` — The run from which to copy the string indices.

- `range` — The range of string indices to copy. If the length of the range is set to `0`, then the copy operation continues from the range’s start index to the end of the run.

- `buffer` — The buffer to which the string indices are copied. The buffer must be allocated to at least the value specified by the range’s length.

## Discussion

The indices are the character indices that originally spawned the glyphs that make up the run. They can be used to map the glyphs in the run back to the characters in the backing store.

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
- [CTRunGetStringRange](<ctrungetstringrange(__).md>) — Gets the range of characters that originally spawned the glyphs in the run.
