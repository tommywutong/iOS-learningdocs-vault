---
title: 'CTRunGetStringIndicesPtr(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctrungetstringindicesptr(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctrungetstringindicesptr(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrungetstringindicesptr%28_%3A%29.json'
content_hash: 'sha256:a4023b3f8af1a646'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunGetStringIndicesPtr(_:)

<sub>Function</sub>

Returns a direct pointer for the string indices stored in the run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRunGetStringIndicesPtr(_ run: CTRun) -> UnsafePointer<CFIndex>?
```

## Parameters

- `run` — The run for which to return string indices.

## Return Value

A valid pointer to an array of [CFIndex](../corefoundation/cfindex.md) structures, or `NULL`.

## Discussion

The indices are the character indices that originally spawned the glyphs that make up the run. They can be used to map the glyphs in the run back to the characters in the backing store. The string indices array will have a length equal to the value returned by [CTRunGetGlyphCount](<ctrungetglyphcount(__).md>). The caller should be prepared for this function to return `NULL` even if there are glyphs in the stream. If this function returns `NULL`, the caller must allocate its own buffer and call [CTRunGetStringIndices](<ctrungetstringindices(______).md>) to fetch the indices.

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
- [CTRunGetStringIndices](<ctrungetstringindices(______).md>) — Copies a range of string indices into a user-provided buffer.
- [CTRunGetStringRange](<ctrungetstringrange(__).md>) — Gets the range of characters that originally spawned the glyphs in the run.
