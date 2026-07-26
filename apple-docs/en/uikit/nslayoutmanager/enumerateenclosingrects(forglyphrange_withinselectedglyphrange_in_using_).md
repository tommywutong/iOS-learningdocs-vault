---
title: 'enumerateEnclosingRects(forGlyphRange:withinSelectedGlyphRange:in:using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/enumerateenclosingrects(forglyphrange:withinselectedglyphrange:in:using:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/enumerateenclosingrects(forglyphrange:withinselectedglyphrange:in:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/enumerateenclosingrects%28forglyphrange%3Awithinselectedglyphrange%3Ain%3Ausing%3A%29.json'
content_hash: 'sha256:6d67fcdb3691e6d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# enumerateEnclosingRects(forGlyphRange:withinSelectedGlyphRange:in:using:)

<sub>Instance Method</sub>

Enumerates enclosing rectangles for the specified glyph range in a text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func enumerateEnclosingRects(forGlyphRange glyphRange: NSRange, withinSelectedGlyphRange selectedRange: NSRange, in textContainer: NSTextContainer, using block: @escaping (CGRect, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `glyphRange` — The glyph range for which to return enclosing rectangles.

- `selectedRange` — Selected glyphs within `glyphRange`, which can affect the size of the rectangles. If not interested in selection rectangles, pass `{NSNotFound, 0}` as the selected range.

- `textContainer` — The text container in which the glyphs are laid out.

- `block` — The block to apply to the glyph range. The block has two arguments: - **rect** — The current enclosing rectangle. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further processing of the array. The stop argument is an out-only argument. You should only set this Boolean to [true](../../swift/true.md) within the block.

## Discussion

These rectangles are always in container coordinates. They can be used to draw the text background or highlight for the given range of characters. The rectangles don’t necessarily enclose glyphs that draw outside their line fragment rectangles; use [- boundingRectForGlyphRange:inTextContainer:](<boundingrect(forglyphrange_in_).md>) to determine the area that contains all drawing performed for a range of glyphs.

If a selected range is given in the second argument, the rectangles returned are correct for drawing the selection.  Selection rectangles are generally more complicated than enclosing rectangles, and supplying a selected range determines whether the method does this extra work. This method does the minimum amount of work required to answer the question.

Performs glyph generation and layout if needed.

## See Also

### Performing advanced layout queries

- [- boundingRectForGlyphRange:inTextContainer:](<boundingrect(forglyphrange_in_).md>) — Returns the bounding rectangle for the specified glyphs in a container.
- [- characterIndexForPoint:inTextContainer:fractionOfDistanceBetweenInsertionPoints:](<characterindex(for_in_fractionofdistancebetweeninsertionpoints_).md>) — Returns the index of the character that lies beneath the specified point using the specified container’s coordinate system.
- [- characterRangeForGlyphRange:actualGlyphRange:](<characterrange(forglyphrange_actualglyphrange_).md>) — Returns the range of characters that correspond to the glyphs in the specified glyph range.
- [- enumerateLineFragmentsForGlyphRange:usingBlock:](<enumeratelinefragments(forglyphrange_using_).md>) — Enumerates line fragments intersecting with the specified glyph range.
- [- fractionOfDistanceThroughGlyphForPoint:inTextContainer:](<fractionofdistancethroughglyph(for_in_).md>) — Returns the fraction of the distance between the glyph at the specified point and the next glyph.
- [- getLineFragmentInsertionPointsForCharacterAtIndex:alternatePositions:inDisplayOrder:positions:characterIndexes:](<getlinefragmentinsertionpoints(forcharacterat_alternatepositions_indisplayorder_positions_characterindexes_).md>) — Returns insertion points in bulk for a specified line fragment.
- [- glyphIndexForPoint:inTextContainer:](<glyphindex(for_in_).md>) — Returns the index of the glyph at the specified location in a text container.
- [- glyphIndexForPoint:inTextContainer:fractionOfDistanceThroughGlyph:](<glyphindex(for_in_fractionofdistancethroughglyph_).md>) — Returns the index of the glyph at the specified point using the container’s coordinate system.
- [- glyphRangeForBoundingRect:inTextContainer:](<glyphrange(forboundingrect_in_).md>) — Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [- glyphRangeForBoundingRectWithoutAdditionalLayout:inTextContainer:](<glyphrange(forboundingrectwithoutadditionallayout_in_).md>) — Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [- glyphRangeForTextContainer:](<glyphrange(for_).md>) — Returns the range of glyphs lying within the specified text container.
- [- glyphRangeForCharacterRange:actualCharacterRange:](<glyphrange(forcharacterrange_actualcharacterrange_).md>) — Returns the range of glyphs that the specified range of characters generates.
- [- rangeOfNominallySpacedGlyphsContainingIndex:](<range(ofnominallyspacedglyphscontaining_).md>) — Returns the range of displayable glyphs that surround the glyph at the specified index.
