---
title: 'CTRunGetAdvancesPtr(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctrungetadvancesptr(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctrungetadvancesptr(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrungetadvancesptr%28_%3A%29.json'
content_hash: 'sha256:6ee5417fd188595e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunGetAdvancesPtr(_:)

<sub>Function</sub>

Returns a direct pointer for the glyph advance array stored in the run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRunGetAdvancesPtr(_ run: CTRun) -> UnsafePointer<CGSize>?
```

## Parameters

- `run` — The run whose advances you wish to access.

## Return Value

A valid pointer to an array of `CGSize` structures representing the glyph advance array or `NULL`.

## Discussion

The advance array will have a length equal to the value returned by [CTRunGetGlyphCount](<ctrungetglyphcount(__).md>). The caller should be prepared for this function to return `NULL` even if there are glyphs in the stream. Should this function return `NULL`, the caller needs allocate its own buffer and call [CTRunGetAdvances](<ctrungetadvances(______).md>) to fetch the advances. Note that advances alone are not sufficient for correctly positioning glyphs in a line, as a run may have a non-identity matrix or the initial glyph in a line may have a non-zero origin; callers should consider using positions instead.

## See Also

### Getting Glyph Run Data

- [CTRunGetGlyphCount](<ctrungetglyphcount(__).md>) — Gets the glyph count for the run.
- [CTRunGetAttributes](<ctrungetattributes(__).md>) — Returns the attribute dictionary that was used to create the glyph run.
- [CTRunGetStatus](<ctrungetstatus(__).md>) — Returns the run’s status.
- [CTRunGetGlyphsPtr](<ctrungetglyphsptr(__).md>) — Returns a direct pointer for the glyph array stored in the run.
- [CTRunGetGlyphs](<ctrungetglyphs(______).md>) — Copies a range of glyphs into a user-provided buffer.
- [CTRunGetPositionsPtr](<ctrungetpositionsptr(__).md>) — Returns a direct pointer for the glyph position array stored in the run.
- [CTRunGetPositions](<ctrungetpositions(______).md>) — Copies a range of glyph positions into a user-provided buffer.
- [CTRunGetAdvances](<ctrungetadvances(______).md>) — Copies a range of glyph advances into a user-provided buffer.
- [CTRunGetStringIndicesPtr](<ctrungetstringindicesptr(__).md>) — Returns a direct pointer for the string indices stored in the run.
- [CTRunGetStringIndices](<ctrungetstringindices(______).md>) — Copies a range of string indices into a user-provided buffer.
- [CTRunGetStringRange](<ctrungetstringrange(__).md>) — Gets the range of characters that originally spawned the glyphs in the run.
