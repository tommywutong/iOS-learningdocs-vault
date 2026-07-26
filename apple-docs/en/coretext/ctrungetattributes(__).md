---
title: 'CTRunGetAttributes(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctrungetattributes(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctrungetattributes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrungetattributes%28_%3A%29.json'
content_hash: 'sha256:abca950b72436c20'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunGetAttributes(_:)

<sub>Function</sub>

Returns the attribute dictionary that was used to create the glyph run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRunGetAttributes(_ run: CTRun) -> CFDictionary
```

## Parameters

- `run` — The run for which to return attributes.

## Return Value

A valid [CFDictionary](../corefoundation/cfdictionary.md) or `NULL` on error or if the run has no attributes.

## Discussion

The dictionary returned is either the same one that was set as an attribute dictionary on the original attributed string or a dictionary that has been manufactured by the layout engine. Attribute dictionaries can be manufactured in the case of font substitution or if the run is missing critical attributes.

## See Also

### Getting Glyph Run Data

- [CTRunGetGlyphCount](<ctrungetglyphcount(__).md>) — Gets the glyph count for the run.
- [CTRunGetStatus](<ctrungetstatus(__).md>) — Returns the run’s status.
- [CTRunGetGlyphsPtr](<ctrungetglyphsptr(__).md>) — Returns a direct pointer for the glyph array stored in the run.
- [CTRunGetGlyphs](<ctrungetglyphs(______).md>) — Copies a range of glyphs into a user-provided buffer.
- [CTRunGetPositionsPtr](<ctrungetpositionsptr(__).md>) — Returns a direct pointer for the glyph position array stored in the run.
- [CTRunGetPositions](<ctrungetpositions(______).md>) — Copies a range of glyph positions into a user-provided buffer.
- [CTRunGetAdvancesPtr](<ctrungetadvancesptr(__).md>) — Returns a direct pointer for the glyph advance array stored in the run.
- [CTRunGetAdvances](<ctrungetadvances(______).md>) — Copies a range of glyph advances into a user-provided buffer.
- [CTRunGetStringIndicesPtr](<ctrungetstringindicesptr(__).md>) — Returns a direct pointer for the string indices stored in the run.
- [CTRunGetStringIndices](<ctrungetstringindices(______).md>) — Copies a range of string indices into a user-provided buffer.
- [CTRunGetStringRange](<ctrungetstringrange(__).md>) — Gets the range of characters that originally spawned the glyphs in the run.
