---
title: 'glyphRange(forBoundingRectWithoutAdditionalLayout:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/glyphrange(forboundingrectwithoutadditionallayout:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/glyphrange(forboundingrectwithoutadditionallayout:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/glyphrange%28forboundingrectwithoutadditionallayout%3Ain%3A%29.json'
content_hash: 'sha256:2804c8edd22ae72a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# glyphRange(forBoundingRectWithoutAdditionalLayout:in:)

<sub>Instance Method</sub>

Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func glyphRange(forBoundingRectWithoutAdditionalLayout bounds: CGRect, in container: NSTextContainer) -> NSRange
```

## Parameters

- `bounds` — The bounding rectangle for which to return glyphs.

- `container` — The text container in which the glyphs are laid out.

## Return Value

The range of glyphs that would need to be displayed in order to draw all glyphs that fall (even partially) within the given bounding rectangle. The range returned can include glyphs that don’t fall inside or intersect `bounds`, although the first and last glyphs in the range always do. At most this method returns the glyph range for the whole container.

## Discussion

Unlike [- glyphRangeForBoundingRect:inTextContainer:](<glyphrange(forboundingrect_in_).md>), this variant of the method doesn’t perform glyph generation or layout. Its results, though faster, can be incorrect. This method is primarily for use by `NSTextView`; you should rarely need to use it yourself.

Bounding rectangles are always in container coordinates.

## See Also

### Performing advanced layout queries

- [- boundingRectForGlyphRange:inTextContainer:](<boundingrect(forglyphrange_in_).md>) — Returns the bounding rectangle for the specified glyphs in a container.
- [- characterIndexForPoint:inTextContainer:fractionOfDistanceBetweenInsertionPoints:](<characterindex(for_in_fractionofdistancebetweeninsertionpoints_).md>) — Returns the index of the character that lies beneath the specified point using the specified container’s coordinate system.
- [- characterRangeForGlyphRange:actualGlyphRange:](<characterrange(forglyphrange_actualglyphrange_).md>) — Returns the range of characters that correspond to the glyphs in the specified glyph range.
- [- enumerateEnclosingRectsForGlyphRange:withinSelectedGlyphRange:inTextContainer:usingBlock:](<enumerateenclosingrects(forglyphrange_withinselectedglyphrange_in_using_).md>) — Enumerates enclosing rectangles for the specified glyph range in a text container.
- [- enumerateLineFragmentsForGlyphRange:usingBlock:](<enumeratelinefragments(forglyphrange_using_).md>) — Enumerates line fragments intersecting with the specified glyph range.
- [- fractionOfDistanceThroughGlyphForPoint:inTextContainer:](<fractionofdistancethroughglyph(for_in_).md>) — Returns the fraction of the distance between the glyph at the specified point and the next glyph.
- [- getLineFragmentInsertionPointsForCharacterAtIndex:alternatePositions:inDisplayOrder:positions:characterIndexes:](<getlinefragmentinsertionpoints(forcharacterat_alternatepositions_indisplayorder_positions_characterindexes_).md>) — Returns insertion points in bulk for a specified line fragment.
- [- glyphIndexForPoint:inTextContainer:](<glyphindex(for_in_).md>) — Returns the index of the glyph at the specified location in a text container.
- [- glyphIndexForPoint:inTextContainer:fractionOfDistanceThroughGlyph:](<glyphindex(for_in_fractionofdistancethroughglyph_).md>) — Returns the index of the glyph at the specified point using the container’s coordinate system.
- [- glyphRangeForBoundingRect:inTextContainer:](<glyphrange(forboundingrect_in_).md>) — Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [- glyphRangeForTextContainer:](<glyphrange(for_).md>) — Returns the range of glyphs lying within the specified text container.
- [- glyphRangeForCharacterRange:actualCharacterRange:](<glyphrange(forcharacterrange_actualcharacterrange_).md>) — Returns the range of glyphs that the specified range of characters generates.
- [- rangeOfNominallySpacedGlyphsContainingIndex:](<range(ofnominallyspacedglyphscontaining_).md>) — Returns the range of displayable glyphs that surround the glyph at the specified index.
