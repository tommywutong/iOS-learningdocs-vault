---
title: 'getLineFragmentInsertionPoints(forCharacterAt:alternatePositions:inDisplayOrder:positions:characterIndexes:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/getlinefragmentinsertionpoints(forcharacterat:alternatepositions:indisplayorder:positions:characterindexes:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/getlinefragmentinsertionpoints(forcharacterat:alternatepositions:indisplayorder:positions:characterindexes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/getlinefragmentinsertionpoints%28forcharacterat%3Aalternatepositions%3Aindisplayorder%3Apositions%3Acharacterindexes%3A%29.json'
content_hash: 'sha256:4be280f4e97520bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# getLineFragmentInsertionPoints(forCharacterAt:alternatePositions:inDisplayOrder:positions:characterIndexes:)

<sub>Instance Method</sub>

Returns insertion points in bulk for a specified line fragment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func getLineFragmentInsertionPoints(forCharacterAt charIndex: Int, alternatePositions aFlag: Bool, inDisplayOrder dFlag: Bool, positions: UnsafeMutablePointer<CGFloat>?, characterIndexes charIndexes: UnsafeMutablePointer<Int>?) -> Int
```

## Parameters

- `charIndex` — The character index of one character within the line fragment.

- `aFlag` — If [true](../../swift/true.md), returns alternate, rather than primary, insertion points.

- `dFlag` — If [true](../../swift/true.md), returns insertion points in display, rather than logical, order.

- `positions` — On output, the positions of the insertion points, in the order specified.

- `charIndexes` — On output, the indexes of the characters corresponding to the returned insertion points.

## Return Value

The number of insertion points returned.

## Discussion

The method allows clients to obtain all insertion points for a line fragment in one call. Each pointer passed in should either be `NULL` or else point to sufficient memory to hold as many elements as there are insertion points in the line fragment (which cannot be more than the number of characters + 1). The returned positions indicate a transverse offset relative to the line fragment rectangle’s origin. Internal caching is used to ensure that repeated calls to this method for the same line fragment (possibly with differing values for other arguments) are not significantly more expensive than a single call.

## See Also

### Related Documentation

- [rectArray(forCharacterRange:withinSelectedCharacterRange:in:rectCount:)](<../../appkit/nslayoutmanager/rectarray(forcharacterrange_withinselectedcharacterrange_in_rectcount_).md>) — Returns an array of rectangles and, by reference, the number of such rectangles, that define the region in the given container enclosing the given character range.
- [rectArray(forGlyphRange:withinSelectedGlyphRange:in:rectCount:)](<../../appkit/nslayoutmanager/rectarray(forglyphrange_withinselectedglyphrange_in_rectcount_).md>) — Returns an array of rectangles and, by reference, the number of such rectangles, that define the region in the given container enclosing the given glyph range.

### Performing advanced layout queries

- [- boundingRectForGlyphRange:inTextContainer:](<boundingrect(forglyphrange_in_).md>) — Returns the bounding rectangle for the specified glyphs in a container.
- [- characterIndexForPoint:inTextContainer:fractionOfDistanceBetweenInsertionPoints:](<characterindex(for_in_fractionofdistancebetweeninsertionpoints_).md>) — Returns the index of the character that lies beneath the specified point using the specified container’s coordinate system.
- [- characterRangeForGlyphRange:actualGlyphRange:](<characterrange(forglyphrange_actualglyphrange_).md>) — Returns the range of characters that correspond to the glyphs in the specified glyph range.
- [- enumerateEnclosingRectsForGlyphRange:withinSelectedGlyphRange:inTextContainer:usingBlock:](<enumerateenclosingrects(forglyphrange_withinselectedglyphrange_in_using_).md>) — Enumerates enclosing rectangles for the specified glyph range in a text container.
- [- enumerateLineFragmentsForGlyphRange:usingBlock:](<enumeratelinefragments(forglyphrange_using_).md>) — Enumerates line fragments intersecting with the specified glyph range.
- [- fractionOfDistanceThroughGlyphForPoint:inTextContainer:](<fractionofdistancethroughglyph(for_in_).md>) — Returns the fraction of the distance between the glyph at the specified point and the next glyph.
- [- glyphIndexForPoint:inTextContainer:](<glyphindex(for_in_).md>) — Returns the index of the glyph at the specified location in a text container.
- [- glyphIndexForPoint:inTextContainer:fractionOfDistanceThroughGlyph:](<glyphindex(for_in_fractionofdistancethroughglyph_).md>) — Returns the index of the glyph at the specified point using the container’s coordinate system.
- [- glyphRangeForBoundingRect:inTextContainer:](<glyphrange(forboundingrect_in_).md>) — Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [- glyphRangeForBoundingRectWithoutAdditionalLayout:inTextContainer:](<glyphrange(forboundingrectwithoutadditionallayout_in_).md>) — Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [- glyphRangeForTextContainer:](<glyphrange(for_).md>) — Returns the range of glyphs lying within the specified text container.
- [- glyphRangeForCharacterRange:actualCharacterRange:](<glyphrange(forcharacterrange_actualcharacterrange_).md>) — Returns the range of glyphs that the specified range of characters generates.
- [- rangeOfNominallySpacedGlyphsContainingIndex:](<range(ofnominallyspacedglyphscontaining_).md>) — Returns the range of displayable glyphs that surround the glyph at the specified index.
