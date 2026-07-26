---
title: 'CTRunGetStatus(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctrungetstatus(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctrungetstatus(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrungetstatus%28_%3A%29.json'
content_hash: 'sha256:c93b86857a2d0659'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunGetStatus(_:)

<sub>Function</sub>

Returns the run’s status.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRunGetStatus(_ run: CTRun) -> CTRunStatus
```

## Parameters

- `run` — The run for which to return the status.

## Return Value

The run’s status.

## Discussion

Runs have status that can be used to expedite certain operations. Knowing the direction and ordering of a run’s glyphs can aid in string index analysis, whereas knowing whether the positions reference the identity text matrix can avoid expensive comparisons. This status is provided as a convenience, because this information is not strictly necessary but can be helpful in some circumstances.

## See Also

### Getting Glyph Run Data

- [CTRunGetGlyphCount](<ctrungetglyphcount(__).md>) — Gets the glyph count for the run.
- [CTRunGetAttributes](<ctrungetattributes(__).md>) — Returns the attribute dictionary that was used to create the glyph run.
- [CTRunGetGlyphsPtr](<ctrungetglyphsptr(__).md>) — Returns a direct pointer for the glyph array stored in the run.
- [CTRunGetGlyphs](<ctrungetglyphs(______).md>) — Copies a range of glyphs into a user-provided buffer.
- [CTRunGetPositionsPtr](<ctrungetpositionsptr(__).md>) — Returns a direct pointer for the glyph position array stored in the run.
- [CTRunGetPositions](<ctrungetpositions(______).md>) — Copies a range of glyph positions into a user-provided buffer.
- [CTRunGetAdvancesPtr](<ctrungetadvancesptr(__).md>) — Returns a direct pointer for the glyph advance array stored in the run.
- [CTRunGetAdvances](<ctrungetadvances(______).md>) — Copies a range of glyph advances into a user-provided buffer.
- [CTRunGetStringIndicesPtr](<ctrungetstringindicesptr(__).md>) — Returns a direct pointer for the string indices stored in the run.
- [CTRunGetStringIndices](<ctrungetstringindices(______).md>) — Copies a range of string indices into a user-provided buffer.
- [CTRunGetStringRange](<ctrungetstringrange(__).md>) — Gets the range of characters that originally spawned the glyphs in the run.
