---
title: 'enumerateLineFragments(forGlyphRange:using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/enumeratelinefragments(forglyphrange:using:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/enumeratelinefragments(forglyphrange:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/enumeratelinefragments%28forglyphrange%3Ausing%3A%29.json'
content_hash: 'sha256:7b28212ff7088246'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# enumerateLineFragments(forGlyphRange:using:)

<sub>Instance Method</sub>

Enumerates line fragments intersecting with the specified glyph range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func enumerateLineFragments(forGlyphRange glyphRange: NSRange, using block: @escaping (CGRect, CGRect, NSTextContainer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `glyphRange` — The glyph range for which to return line fragment rectangles.

- `block` — The block to apply to the glyph range. The block has five arguments: - **rect** — The current line fragment rectangle. - **usedRect** — The portion of the line fragment rectangle that actually contains glyphs or other marks that are drawn (including the text container’s line fragment padding). - **textContainer** — The text container in which the glyphs are laid out. - **glyphRange** — The range of glyphs laid out in the current line fragment. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further processing of the array. The stop argument is an out-only argument. You should only set this Boolean to [true](../../swift/true.md) within the block.

## Discussion

This method causes glyph generation and layout for the line fragment containing the glyphs in the specified range, or if noncontiguous layout is not enabled, for all of the text up to and including that line fragment.

Line fragment rectangles are always in container coordinates.

## See Also

### Performing advanced layout queries

- [- boundingRectForGlyphRange:inTextContainer:](<boundingrect(forglyphrange_in_).md>) — Returns the bounding rectangle for the specified glyphs in a container.
- [- characterIndexForPoint:inTextContainer:fractionOfDistanceBetweenInsertionPoints:](<characterindex(for_in_fractionofdistancebetweeninsertionpoints_).md>) — Returns the index of the character that lies beneath the specified point using the specified container’s coordinate system.
- [- characterRangeForGlyphRange:actualGlyphRange:](<characterrange(forglyphrange_actualglyphrange_).md>) — Returns the range of characters that correspond to the glyphs in the specified glyph range.
- [- enumerateEnclosingRectsForGlyphRange:withinSelectedGlyphRange:inTextContainer:usingBlock:](<enumerateenclosingrects(forglyphrange_withinselectedglyphrange_in_using_).md>) — Enumerates enclosing rectangles for the specified glyph range in a text container.
- [- fractionOfDistanceThroughGlyphForPoint:inTextContainer:](<fractionofdistancethroughglyph(for_in_).md>) — Returns the fraction of the distance between the glyph at the specified point and the next glyph.
- [- getLineFragmentInsertionPointsForCharacterAtIndex:alternatePositions:inDisplayOrder:positions:characterIndexes:](<getlinefragmentinsertionpoints(forcharacterat_alternatepositions_indisplayorder_positions_characterindexes_).md>) — Returns insertion points in bulk for a specified line fragment.
- [- glyphIndexForPoint:inTextContainer:](<glyphindex(for_in_).md>) — Returns the index of the glyph at the specified location in a text container.
- [- glyphIndexForPoint:inTextContainer:fractionOfDistanceThroughGlyph:](<glyphindex(for_in_fractionofdistancethroughglyph_).md>) — Returns the index of the glyph at the specified point using the container’s coordinate system.
- [- glyphRangeForBoundingRect:inTextContainer:](<glyphrange(forboundingrect_in_).md>) — Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [- glyphRangeForBoundingRectWithoutAdditionalLayout:inTextContainer:](<glyphrange(forboundingrectwithoutadditionallayout_in_).md>) — Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [- glyphRangeForTextContainer:](<glyphrange(for_).md>) — Returns the range of glyphs lying within the specified text container.
- [- glyphRangeForCharacterRange:actualCharacterRange:](<glyphrange(forcharacterrange_actualcharacterrange_).md>) — Returns the range of glyphs that the specified range of characters generates.
- [- rangeOfNominallySpacedGlyphsContainingIndex:](<range(ofnominallyspacedglyphscontaining_).md>) — Returns the range of displayable glyphs that surround the glyph at the specified index.
